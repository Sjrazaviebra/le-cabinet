# -*- coding: utf-8 -*-
"""Contrôle de cohérence des paramètres du dépôt.

La promesse du dépôt n'a de valeur que si elle est vérifiable. Ce script la vérifie :

  1. toute valeur marquée comme vérifiée porte bien une `source` ET une `date_verifiee` ;
  2. aucune source n'est un domaine non admis ;
  3. aucune valeur vérifiée n'a dépassé la péremption (6 mois par défaut) ;
  4. chaque nombre cité dans un fichier .md se retrouve dans le parametres.json du rôle.

Le point 4 est le garde-fou contre la dérive : un chiffre écrit dans un .md et nulle part
ailleurs est exactement la faille par laquelle une valeur périmée survit.

Usage :  python scripts/verifier-parametres.py
Sortie  :  code 0 si tout passe, 1 sinon.
"""
import io, os, re, sys, json, datetime

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PEREMPTION_JOURS = 183
AUJOURD_HUI = datetime.date(2026, 8, 16)  # ⚠️ à passer en date.today() une fois en CI

DOMAINES_ADMIS = (
    "legifrance.gouv.fr", "bofip.impots.gouv.fr", "impots.gouv.fr", "urssaf.fr",
    "autoentrepreneur.urssaf.fr", "mon-entreprise.urssaf.fr",
    "service-public.fr", "service-public.gouv.fr",
    "entreprendre.service-public.fr", "entreprendre.service-public.gouv.fr",
    "bpifrance-creation.fr", "francetravail.fr", "amf-france.org",
    "acpr.banque-france.fr", "cnil.fr", "inpi.fr", "justice.fr",
    "immigration.interieur.gouv.fr", "administration-etrangers-en-france.interieur.gouv.fr",
    "france-visas.gouv.fr", "diplomatie.gouv.fr", "anil.org", "code.travail.gouv.fr",
    "travail-emploi.gouv.fr", "economie.gouv.fr", "ameli.fr", "defenseurdesdroits.fr",
    "arretonslesviolences.gouv.fr", "e-justice.europa.eu", "formalites.entreprises.gouv.fr",
)

# nombres qu'on ne cherche pas dans le JSON : années, numéros d'article, énumérations
IGNORE = re.compile(r"^(?:19|20)\d\d$|^[0-9]$|^1[0-9]$|^2[0-9]$")


def roles():
    base = os.path.join(RACINE, "plugins")
    for dom in sorted(os.listdir(base)):
        d = os.path.join(base, dom, "skills")
        if not os.path.isdir(d):
            continue
        for role in sorted(os.listdir(d)):
            yield dom, role, os.path.join(d, role)


def entrees(bloc):
    for section, contenu in bloc.items():
        if section == "_lisez_moi" or not isinstance(contenu, dict):
            continue
        for cle, val in contenu.items():
            if isinstance(val, dict):
                yield section, cle, val


def nombres(texte):
    """Nombres significatifs d'un .md, hors blocs de code, URL et références de textes.

    On ne cherche que les valeurs *normatives*. Une référence d'article (L321-1, art. 293 B,
    décret n° 2025-648) n'est pas une valeur : elle n'a rien à faire dans parametres.json.
    """
    texte = re.sub(r"```.*?```", " ", texte, flags=re.S)
    texte = re.sub(r"<https?://\S+>|https?://\S+", " ", texte)
    texte = re.sub(
        r"(?:article|articles|art\.?|n°|décret|loi|arrêté|ordonnance|CERFA)"
        r"\s*[LRD]?[\.\s-]*[\d\s-]+[A-Z]?", " ", texte, flags=re.I)
    texte = re.sub(r"\b[LRD]\d[\d-]*\b", " ", texte)
    texte = re.sub(r"\b\d{1,2}/\d{1,2}/\d{2,4}\b", " ", texte)
    texte = re.sub(r"\b\d{1,2}\s+(?:janvier|février|mars|avril|mai|juin|juillet|"
                   r"août|septembre|octobre|novembre|décembre)\b", " ", texte, flags=re.I)
    trouves = set()
    for brut in re.findall(r"\d[\d   ]*(?:,\d+)?", texte):
        n = brut.replace(" ", "").replace(" ", "").replace(" ", "").rstrip(",")
        if not n or IGNORE.match(n):
            continue
        trouves.add(n.replace(",", ".") if "," in n else n)
    return trouves


def main():
    erreurs, alertes, verifiees, ouvertes = [], [], 0, 0

    for dom, role, chemin in roles():
        pj = os.path.join(chemin, "data", "parametres.json")
        if not os.path.exists(pj):
            erreurs.append("%s/%s : parametres.json manquant" % (dom, role))
            continue
        bloc = json.load(open(pj, encoding="utf-8"))
        plat = json.dumps(bloc, ensure_ascii=False)

        for section, cle, val in entrees(bloc):
            ref = "%s/%s → %s.%s" % (dom, role, section, cle)
            if val.get("a_verifier") is False:
                verifiees += 1
                if not val.get("source"):
                    erreurs.append("%s : marquée vérifiée sans `source`" % ref)
                if not val.get("date_verifiee"):
                    erreurs.append("%s : marquée vérifiée sans `date_verifiee`" % ref)
                else:
                    try:
                        d = datetime.date.fromisoformat(val["date_verifiee"])
                        if (AUJOURD_HUI - d).days > PEREMPTION_JOURS:
                            alertes.append("%s : vérifiée le %s, périmée (> %d jours)"
                                           % (ref, val["date_verifiee"], PEREMPTION_JOURS))
                    except ValueError:
                        erreurs.append("%s : `date_verifiee` illisible" % ref)
                src = val.get("source", "")
                if src and not any(dom_ok in src for dom_ok in DOMAINES_ADMIS):
                    erreurs.append("%s : source non admise → %s" % (ref, src))
            else:
                ouvertes += 1

        refs = os.path.join(chemin, "references")
        for f in sorted(os.listdir(refs)) if os.path.isdir(refs) else []:
            texte = open(os.path.join(refs, f), encoding="utf-8").read()
            if "État : `À ÉCRIRE`" in texte:
                continue
            absents = sorted(n for n in nombres(texte) if n not in plat)
            if absents:
                alertes.append("%s/%s/%s : %d nombre(s) absent(s) du parametres.json → %s"
                               % (dom, role, f, len(absents), ", ".join(absents[:8])))

    print("  %d valeurs vérifiées · %d ouvertes" % (verifiees, ouvertes))
    for a in alertes:
        print("  ⚠️  %s" % a)
    for e in erreurs:
        print("  ⛔ %s" % e)
    print("  --- %d erreur(s), %d alerte(s) ---" % (len(erreurs), len(alertes)))
    return 1 if erreurs else 0


if __name__ == "__main__":
    sys.exit(main())
