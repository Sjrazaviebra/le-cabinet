# le-cabinet

**Deux skills pour agents IA : un comptable et un avocat, en droit français.**
Entreprise **et** vie privée.

> 🚧 **En construction.** L'architecture est posée et les deux skills sont rédigés, mais les
> fichiers de référence sont encore vides et aucune valeur chiffrée n'a été vérifiée à la source.
> Le travail de rédaction se fait sur la branche [`dev`](../../tree/dev).
> Voir [`docs/avancement.md`](docs/avancement.md) pour l'état fichier par fichier.

> ⚖️ **Ces skills ne remplacent ni un expert-comptable inscrit à l'Ordre, ni un avocat inscrit à
> un barreau.** Ce sont des outils d'**aide à la décision** : ils structurent une question, posent
> les bonnes, et disent **où vérifier**. Pour tout acte engageant — statuts, contrat signé,
> déclaration fiscale, contentieux — consultez un professionnel couvert par une assurance
> responsabilité civile professionnelle.

---

## Les deux skills

| Skill | Invocation | Couvre |
|---|---|---|
| **Comptable** | `/comptable` | Formes juridiques, micro-entreprise, TVA, PCG et écritures, clôture et liasse, facturation, impôt sur le revenu, revenus financiers, chômage et création d'activité, paie. |
| **Avocat** | `/avocat` | Activités réglementées, sociétés et objet social, contrats et CGV, international, propriété intellectuelle, travail, consommation, RGPD, logement, famille, succession, procédure. |

Vous pouvez les appeler directement, ou laisser l'agent les charger quand la question s'y prête.

## ★ Le parti pris : aucun chiffre n'est écrit de mémoire

Le droit fiscal et social français change tous les ans, parfois en cours d'année. Un skill qui
récite un taux de l'an dernier avec assurance est **plus dangereux que pas de skill du tout** :
il produit une erreur confiante, que personne n'a de raison de vérifier, et sur laquelle des
décisions se construisent.

Donc, ici :

1. **Les fichiers de méthode ne contiennent aucune valeur volatile.** Ils portent le raisonnement,
   les questions à poser, les arbres de décision, et **l'adresse officielle où lire la valeur**.
2. **Les valeurs vivent dans `data/parametres.json`**, propre à chaque skill, chacune avec sa
   `source` (URL officielle) et sa `date_verifiee`.
3. **Le skill refuse d'affirmer une valeur périmée.** Au-delà de six mois, il le dit et renvoie à
   la source au lieu de deviner.

Sources admises, par ordre d'autorité : **Légifrance** · **BOFiP** · **impots.gouv.fr** ·
**urssaf.fr** · **service-public.fr** / **entreprendre.service-public.fr** · **France Travail** ·
**BPI Création** · les autorités compétentes (**AMF**, **ACPR**, **CNIL**, **DGCCRF**, **INPI**).
Un blog, un forum ou un comparateur n'est jamais une source.

**Chaque skill embarque ses propres données** — aucun lien symbolique entre eux. Chacun reste donc
installable seul, et se copie ou se zippe sans rien casser.

## Installation

### Depuis Claude Code (recommandé)

```
/plugin marketplace add Sjrazaviebra/le-cabinet
```

puis installez le domaine voulu, ou les deux :

```
/plugin install comptabilite@le-cabinet
/plugin install juridique@le-cabinet
```

### À la main

Copiez le dossier du rôle voulu dans vos skills personnels :

```bash
cp -r plugins/comptabilite/skills/comptable ~/.claude/skills/
cp -r plugins/juridique/skills/avocat ~/.claude/skills/
```

`/comptable` et `/avocat` sont alors disponibles.

## Structure

**Un plugin = un domaine. Un skill = un rôle.** Un domaine peut donc accueillir plusieurs rôles au
fil du temps — un fiscaliste à côté du comptable, un notaire à côté de l'avocat — sans rien casser
chez ceux qui l'ont déjà installé.

```
le-cabinet/
├── .claude-plugin/marketplace.json      ← le catalogue
└── plugins/
    ├── comptabilite/                    ← le DOMAINE
    │   ├── .claude-plugin/plugin.json
    │   └── skills/
    │       └── comptable/               ← le RÔLE → /comptable
    │           ├── SKILL.md             ← routeur et méthode
    │           ├── references/*.md      ← un fichier par sujet
    │           └── data/parametres.json ← les chiffres, sourcés et datés
    └── juridique/
        └── skills/
            └── avocat/                  ← /avocat
```

## Contribuer

Une contribution utile ici, c'est presque toujours **une source**. Si vous corrigez un chiffre,
joignez l'URL officielle et la date. Voir [`CONTRIBUTING.md`](CONTRIBUTING.md) — et
[`docs/avancement.md`](docs/avancement.md) pour savoir quel fichier est libre.

## Licence

MIT. Utilisation libre, y compris commerciale.
