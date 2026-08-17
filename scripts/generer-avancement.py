# -*- coding: utf-8 -*-
"""Régénère docs/avancement.md à partir de l'état réel du dépôt.

Le tableau de bord d'un dépôt en construction n'a de valeur que s'il ne mente
jamais. Le générer plutôt que l'écrire à la main supprime la seule cause de
mensonge : l'oubli de mise à jour.

Usage : python scripts/generer-avancement.py
"""
import io, os, re, sys, json

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROCHAINS = [
    "`travail/prudhommes.md` — les délais propres au salaire, à la discrimination, au harcèlement.",
    "`impots/declaration-annuelle.md` — avant la saison déclarative.",
    "`logement/depot-de-garantie.md` et `conge-et-fin-de-bail.md`.",
    "`immigration/titres-de-sejour.md` et `demande-et-renouvellement.md`.",
    "`juriste/contrats-commerciaux.md` et `propriete-intellectuelle.md`.",
]


def etat_fichier(chemin):
    tete = open(chemin, encoding="utf-8").read(600)
    m = re.search(r"\*\*(?:Etat|État)\s*:\s*`([^`]+)`", tete)
    return m.group(1) if m else "À ÉCRIRE"


def main():
    corps, redigés, total_ok, total_td = [], [], 0, 0
    base = os.path.join(RACINE, "plugins")

    for dom in sorted(os.listdir(base)):
        skills = os.path.join(base, dom, "skills")
        if not os.path.isdir(skills):
            continue
        corps += ["## Domaine `%s`" % dom, ""]
        for role in sorted(os.listdir(skills)):
            r = os.path.join(skills, role)
            corps += ["### Rôle `/%s`" % role, "", "| Fichier | État |", "|---|---|",
                      "| `SKILL.md` | **RÉDIGÉ** |"]
            pj = json.load(open(os.path.join(r, "data", "parametres.json"), encoding="utf-8"))
            ok = td = 0
            for section, contenu in pj.items():
                if section == "_lisez_moi" or not isinstance(contenu, dict):
                    continue
                for _, v in contenu.items():
                    if isinstance(v, dict) and "a_verifier" in v:
                        if v["a_verifier"] is False:
                            ok += 1
                        else:
                            td += 1
            total_ok, total_td = total_ok + ok, total_td + td
            corps.append("| `data/parametres.json` | %s, %d à vérifier |"
                         % ("**%d vérifiée(s)**" % ok if ok else "squelette", td))
            refs = os.path.join(r, "references")
            for f in sorted(os.listdir(refs)) if os.path.isdir(refs) else []:
                e = etat_fichier(os.path.join(refs, f))
                if e != "À ÉCRIRE":
                    redigés.append("`%s/%s`" % (role, f[:-3]))
                corps.append("| `references/%s` | %s |" % (f, e if e == "À ÉCRIRE" else "**%s**" % e))
            corps.append("")

    tete = [
        "# Avancement", "",
        "**%d valeurs vérifiées et datées**, %d encore ouvertes. **%d rôles.**"
        % (total_ok, total_td, sum(1 for d in os.listdir(base)
                                   for _ in os.listdir(os.path.join(base, d, "skills")))),
        "",
        "Ce fichier est **généré** : `python scripts/generer-avancement.py`. Il ne peut donc pas",
        "se désynchroniser du dépôt.",
        "",
        "Le contrôle de cohérence est séparé : `python scripts/verifier-parametres.py` (0 erreur exigée).",
        "",
        "Un plugin = un **domaine**, un skill = un **rôle**. Critère : [taxonomie.md](taxonomie.md).",
        "",
    ]
    pied = ["## Ordre de rédaction", "",
            "**Rédigés** — %d fichiers : %s" % (len(redigés), " · ".join(sorted(redigés))), "",
            "**Prochains** :", ""]
    pied += ["%d. %s" % (i, x) for i, x in enumerate(PROCHAINS, 1)]
    pied.append("")

    sortie = os.path.join(RACINE, "docs", "avancement.md")
    open(sortie, "w", encoding="utf-8").write("\n".join(tete + corps + pied))
    print("  docs/avancement.md : %d valeurs vérifiées, %d ouvertes, %d fichiers rédigés"
          % (total_ok, total_td, len(redigés)))


if __name__ == "__main__":
    main()
