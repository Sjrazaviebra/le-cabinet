![le-cabinet — droit, fiscalité, entreprise et patrimoine français](assets/banner.jpg)

🇫🇷 **Français** · 🇬🇧 [English](README.en.md)

<!-- ⚠️ EN-TETE : banniere, puis logo FLOTTE DANS le titre ###, puis ligne DESSINEE EN TEXTE.
     Quatre impasses mesurees sur le moteur de rendu de GitHub avant d arriver la :
       - un titre en # ou ## porte une bordure dessinee sur TOUTE la largeur : avec un logo
         flottant, elle le TRAVERSE. Le ### n en a pas.
       - un <hr> ne sauve pas : c est un BLOC, sa bordure reprend toute la largeur et
         retraverse le logo. La seule ligne qui RESPECTE un flottant est du TEXTE, parce que
         le texte s ecoule dans la colonne restante.
       - un tableau donne un encadrement : GitHub borde les cellules et SUPPRIME style="border:0".
       - supprimer le titre marche, mais le README perd son plan.
     ⚠️ Longueur de la ligne FIXE (56 caracteres) : plus longue, elle se replie sur deux rangees.
     ⛔ Verifier a l ecran avant de toucher a ce bloc. -->
### <img src="assets/logo.png" align="left" width="124" alt=""> le-cabinet

────────────────────────────────────────────────────────<br>
**Neuf rôles pour agents IA — droit, fiscalité, financement, patrimoine.**<br>
Pour l'entreprise *et* pour la vie privée.

<br clear="left">

[![gate](https://github.com/Sjrazaviebra/le-cabinet/actions/workflows/gate.yml/badge.svg)](https://github.com/Sjrazaviebra/le-cabinet/actions/workflows/gate.yml)

> ✅ **Les neuf rôles sont complets** : chacun de leurs fichiers de référence est rédigé depuis les
> textes officiels. Chaque fichier porte son état en tête — `RÉDIGÉ` ou `PARTIEL` — et **dit
> lui-même ce qu'il ne couvre pas** : un fichier `PARTIEL` n'est pas un fichier inachevé qu'on
> cache, c'est un périmètre annoncé.
>
> **Les compteurs ne sont pas recopiés ici.** Ils vivent dans
> [`docs/avancement.md`](docs/avancement.md), qui est **généré** et dont la CI vérifie à chaque push
> qu'il est à jour. Un README qui annonce un chiffre à la main est un README qui mentira dans deux
> semaines.
>
> La rédaction se fait sur [`dev`](../../tree/dev) ; `main` porte les jalons taggés.
> Utilisation avec un autre agent que Claude → [`AGENTS.md`](AGENTS.md).
>
> ⚖️ **Ces skills ne remplacent ni un expert-comptable inscrit à l'Ordre, ni un avocat inscrit à
> un barreau.** Ce sont des outils d'**aide à la décision** : ils structurent une question, posent
> les bonnes, et disent **où vérifier**. Pour tout acte engageant — statuts, contrat signé,
> déclaration fiscale, contentieux — consultez un professionnel couvert par une assurance
> responsabilité civile professionnelle.

---

## Les neuf rôles

| Rôle | Invocation | Domaine | Couvre |
|---|---|---|---|
| **Comptable** | `/comptable` | `comptabilite` | L'entreprise : formes juridiques, micro-entreprise, TVA, écritures, clôture, facturation, paie, chômage et création. |
| **Impôts** | `/impots` | `comptabilite` | Le particulier : déclaration de revenus, barème, foyer fiscal, revenus financiers et crypto, immobilier, IFI, réclamation et contrôle. |
| **Juriste** | `/juriste` | `juridique` | Sociétés et objet social, contrats et CGV, international, propriété intellectuelle, activités réglementées, consommation, RGPD, procédure. |
| **Travail** | `/travail` | `juridique` | Convention collective, contrat, rémunération et heures, rupture et indemnités, prud'hommes, harcèlement et discrimination. |
| **Logement** | `/logement` | `juridique` | Bail, dépôt de garantie, congé, charges et travaux, impayés et expulsion, colocation, copropriété. |
| **Famille** | `/famille` | `juridique` | Couple et régimes, séparation, enfants et pension, succession, donation, protection des majeurs, violences. |
| **Immigration** | `/immigration` | `juridique` | Titres de séjour, renouvellement, changement de statut, droit au travail, famille, refus et recours, **naturalisation**. |
| **Financement** | `/financement` | `comptabilite` | L'argent de l'activité : compte pro et **droit au compte**, crédit et **rupture de crédit**, **caution du dirigeant**, trésorerie, **médiation du crédit**, assurances obligatoires, carte des leviers fiscaux légaux. |
| **Patrimoine** | `/patrimoine` | `comptabilite` | L'argent personnel : ⚠️ **reconnaître une arnaque et vérifier un agrément**, enveloppes et supports, frais, risque et horizon, épargne réglementée et garantie des dépôts, retraite, budget et **surendettement**. |

**Un rôle n'est pas un thème** : c'est une méthode d'entrée, une posture et des règles d'arrêt
propres. `/travail` commence par demander la convention collective, `/immigration` par chercher un
délai qui court, `/logement` par lire la loi avant le bail. Le critère qui décide qu'un sujet mérite
son propre rôle est écrit dans [`docs/taxonomie.md`](docs/taxonomie.md), et le découpage du domaine
comptabilité — y compris **deux candidats refusés et pourquoi** — dans
[`docs/taxonomie-comptabilite.md`](docs/taxonomie-comptabilite.md).

⛔ **`financement` et `patrimoine` informent, ils ne conseillent pas.** Ils n'émettent aucune
recommandation personnalisée portant sur un instrument financier — c'est le **conseil en
investissement**, service réglementé — et ne recommandent aucun établissement ni produit.

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

1. **`data/parametres.json` fait autorité.** Chaque valeur y porte sa `source` (URL officielle) et
   sa `date_verifiee`. En cas de divergence avec un fichier de méthode, **c'est le JSON qui gagne**.
2. **Un fichier de méthode peut citer une valeur, à une condition** : que la même valeur soit dans
   le `parametres.json` de son rôle, sourcée et datée. Un chiffre qui ne vit que dans un `.md` est
   un chiffre que personne ne pourra plus dater — c'est par là que la dérive commence.
3. **Le skill refuse d'affirmer une valeur périmée.** Au-delà de six mois, il le dit et renvoie à
   la source au lieu de deviner.
4. **Et cette promesse est vérifiable, pas déclarative** :

```bash
python scripts/verifier-parametres.py
```

Le script contrôle que toute valeur marquée vérifiée porte bien source **et** date, qu'aucune source
ne sort de la liste admise, qu'aucune valeur n'a dépassé la péremption, et que chaque nombre cité
dans un fichier rédigé se retrouve bien dans le `parametres.json` de son rôle. Il sort en erreur
sinon.

> ⚠️ **Ce dépôt s'est déjà trompé, et le dira toujours.** Une revue adversariale du 16 août 2026 a
> trouvé trois affirmations fausses publiées avec `a_verifier: false` : une prétendue rétroactivité
> de la TVA, un taux d'ACRE périmé, et un effet suspensif de recours inversé. Elles ont été
> corrigées, les notes de `parametres.json` gardent la trace de la correction, et le script
> ci-dessus est né de cet épisode. Une promesse d'exactitude qui ne documente pas ses erreurs n'est
> pas une promesse.

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

⚠️ **Les skills d'un plugin sont préfixés par le nom du plugin.** Installés ainsi, ils s'appellent
donc `/juridique:travail`, `/comptabilite:impots`, `/juridique:immigration`… La forme courte
`/travail` s'obtient par l'installation manuelle ci-dessous. Vous pouvez aussi laisser l'agent
charger le bon rôle tout seul : les descriptions sont écrites pour ça, en français **et** en
anglais.

### À la main

Copiez le dossier du rôle voulu dans vos skills personnels :

```bash
cp -r plugins/juridique/skills/travail ~/.claude/skills/
cp -r plugins/comptabilite/skills/impots ~/.claude/skills/
```

`/travail` et `/impots` sont alors disponibles.

## Structure

**Un plugin = un domaine. Un skill = un rôle.** Un domaine accueille plusieurs rôles et peut en
recevoir d'autres sans rien casser chez ceux qui l'ont déjà installé — mais **pas n'importe
lesquels** : le critère qui décide qu'un sujet mérite son propre rôle est écrit dans
[`docs/taxonomie.md`](docs/taxonomie.md), et il exclut délibérément les rôles calqués sur les
professions.

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
            ├── avocat/                  ← /juriste
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
