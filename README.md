![le-cabinet](assets/banner.jpg)

<img src="assets/logo.png" alt="le-cabinet" width="96" align="left" hspace="12">

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

| Rôle | Invocation | Domaine | Couvre |
|---|---|---|---|
| **Comptable** | `/comptable` | `comptabilite` | L'entreprise : formes juridiques, micro-entreprise, TVA, écritures, clôture, facturation, paie, chômage et création. |
| **Impôts** | `/impots` | `comptabilite` | Le particulier : déclaration de revenus, barème, foyer fiscal, revenus financiers et crypto, immobilier, IFI, réclamation et contrôle. |
| **Avocat** | `/avocat` | `juridique` | Sociétés et objet social, contrats et CGV, international, propriété intellectuelle, activités réglementées, consommation, RGPD, procédure. |
| **Travail** | `/travail` | `juridique` | Convention collective, contrat, rémunération et heures, rupture et indemnités, prud'hommes, harcèlement et discrimination. |
| **Logement** | `/logement` | `juridique` | Bail, dépôt de garantie, congé, charges et travaux, impayés et expulsion, colocation, copropriété. |
| **Famille** | `/famille` | `juridique` | Couple et régimes, séparation, enfants et pension, succession, donation, protection des majeurs, violences. |
| **Immigration** | `/immigration` | `juridique` | Titres de séjour, renouvellement, changement de statut, droit au travail, famille, refus et recours, **naturalisation**. |

**Un rôle n'est pas un thème** : c'est une méthode d'entrée, une posture et des règles d'arrêt
propres. `/travail` commence par demander la convention collective, `/immigration` par chercher un
délai qui court, `/logement` par lire la loi avant le bail. Le critère qui décide qu'un sujet mérite
son propre rôle est écrit dans [`docs/taxonomie.md`](docs/taxonomie.md).

Vous pouvez les appeler directement, ou laisser l'agent les charger quand la question s'y prête.

**Ces skills sont rédigés en français, mais répondent dans votre langue.** Le droit français est
écrit en français et ses notions n'ont pas d'équivalent fidèle ailleurs — les skills gardent donc
le terme français avec une courte glose, parce que c'est ce mot-là qui figure sur les formulaires
et dans les courriers de l'administration.

*These skills are written in French but answer in your language. French legal and tax concepts have
no faithful equivalent elsewhere, so the French term is kept with a short gloss — that is the word
you will actually see on the forms.*

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
    │       ├── comptable/               ← le RÔLE → /comptable
    │       │   ├── SKILL.md             ← routeur, intake, règles d'arrêt
    │       │   ├── references/*.md      ← un fichier par sujet
    │       │   └── data/parametres.json ← les chiffres, sourcés et datés
    │       └── impots/                  ← /impots
    └── juridique/
        └── skills/
            ├── avocat/                  ← /avocat
            ├── travail/                 ← /travail
            ├── logement/                ← /logement
            ├── famille/                 ← /famille
            └── immigration/             ← /immigration
```

⚠️ **Aucun fichier n'est partagé entre deux rôles.** Les plugins s'installent séparément, donc un
chemin relatif d'un rôle vers un autre casserait. Quand un sujet touche deux rôles, l'un le traite
et l'autre **renvoie par nom de rôle** — « la fiscalité de ce sujet vit dans `impots` ».

## Contribuer

Une contribution utile ici, c'est presque toujours **une source**. Si vous corrigez un chiffre,
joignez l'URL officielle et la date. Voir [`CONTRIBUTING.md`](CONTRIBUTING.md) — et
[`docs/avancement.md`](docs/avancement.md) pour savoir quel fichier est libre.

## Licence

MIT. Utilisation libre, y compris commerciale.
