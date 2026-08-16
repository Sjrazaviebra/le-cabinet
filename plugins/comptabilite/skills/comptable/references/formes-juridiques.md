# Choisir et changer de forme juridique

> **État : `RÉDIGÉ`** pour les mécanismes structurants et la méthode de choix. Les valeurs
> chiffrées propres au régime micro sont dans `micro-entreprise.md` et
> `data/parametres.json`. Vérifié le **2026-08-16**.

## La question n'est pas « quelle forme », c'est « qu'est-ce qui va changer »

Personne ne choisit une forme juridique dans l'absolu. On choisit en fonction de quatre
paramètres, et **un seul suffit souvent à trancher** :

1. **Comment on veut être payé et protégé** — régime social.
2. **Comment le bénéfice est imposé** — IR ou IS.
3. **Ce qu'on veut pouvoir déduire** — forfait ou frais réels.
4. **Ce qu'on veut pouvoir faire plus tard** — embaucher, s'associer, lever, vendre.

Commencez par demander lequel de ces quatre points est **contraint** dans le projet. C'est presque
toujours celui-là qui décide, pas un comparatif général.

## Le paysage, en une lecture

| | **Entreprise individuelle** (dont micro) | **EURL** | **SASU** |
|---|---|---|---|
| Nature | pas de personne morale | société, associé unique | société, associé unique |
| Régime social du dirigeant | **travailleur indépendant** | **travailleur indépendant** (gérant majoritaire) | **assimilé-salarié** |
| Protection sociale | plus légère | plus légère | **plus complète** |
| Coût des cotisations | plus faible | plus faible | **plus élevé** |
| Imposition par défaut | **IR** | **IR** (option IS possible) | **IS** (option IR temporaire possible) |
| Déduction des charges | **forfait** en micro, réel hors micro | **réel** | **réel** |
| Embaucher | possible mais inadapté en micro | oui | oui |
| S'associer plus tard | non sans changer de forme | oui (devient SARL) | oui (devient SAS) |

★ **L'arbitrage social le plus structurant** : le président de SASU est **assimilé-salarié** — donc
mieux couvert, mais avec des cotisations sensiblement plus élevées. Le gérant majoritaire d'EURL et
l'entrepreneur individuel relèvent du **régime des travailleurs indépendants** — moins couverts,
moins coûteux. Il n'y a pas de bonne réponse en soi : il y a un arbitrage entre couverture et
trésorerie, et il dépend de la situation familiale autant que du chiffre d'affaires.

## Les trois pièges de raisonnement les plus fréquents

**1. Choisir sur la simplicité de création.** La micro se crée en une heure ; c'est vrai et c'est
sans importance. Ce qui compte est le coût **à trois ans**, pas le coût du premier jour. Une
création est un événement, une forme juridique est un régime permanent.

**2. Croire qu'on « transformera » plus tard.** On ne transforme pas une entreprise individuelle en
société : on **crée une société** et on **ferme l'entreprise individuelle**. C'est deux démarches,
avec un coût et une discontinuité. Le passage EURL → SARL ou SASU → SAS, lui, est une simple
modification statutaire, pas une création.

**3. Optimiser l'impôt avant d'avoir un revenu.** Tant qu'il n'y a pas de bénéfice, l'arbitrage
IR/IS est théorique. La première année, ce qui compte est **la trésorerie et le coût fixe**, pas le
taux marginal.

## Le cas particulier : vouloir embaucher

**La micro n'est pas conçue pour employer.** La raison est mécanique, pas administrative : le
régime repose sur un **abattement forfaitaire**, et un salaire versé **ne se déduit pas** d'un
forfait. On paierait donc de l'impôt et des cotisations sur un chiffre d'affaires dont une partie
part en salaires, sans jamais pouvoir la retrancher. À quoi s'ajoutent les plafonds de chiffre
d'affaires, qui plafonnent mécaniquement la croissance.

⇒ Si embaucher est un objectif **réel et daté**, la cible est une **société**. Si c'est une
possibilité lointaine, démarrer en micro reste légitime — **à condition de fixer le déclencheur
tout de suite**.

## Fixer le déclencheur de bascule — le vrai livrable de ce fichier

Une bascule subie coûte cher ; une bascule préparée ne coûte presque rien. Écrivez le déclencheur
**pendant que tout va bien**, avec un seuil vérifiable :

- **Charges réelles** > abattement forfaitaire, sur deux exercices → le régime réel devient plus
  favorable. *(C'est le déclencheur le plus fréquent, et le plus souvent manqué.)*
- **Première embauche** envisagée à moins de six mois.
- **Chiffre d'affaires** approchant les seuils sur deux années consécutives.
- **Un client** exige de contracter avec une personne morale.
- **Un associé** entre au capital.

Relisez cette liste **une fois par an, à la clôture**. C'est le seul moment où on a les chiffres et
où on n'est pas dans l'urgence.

## Ce qui ne dépend pas de la forme juridique

À dire tôt, parce que beaucoup de gens choisissent une forme en espérant régler ces points-là :

- **L'objet social ne protège de rien** s'il décrit une activité réglementée. → `activites-reglementees.md`
  du skill `avocat`.
- **La TVA** suit ses propres seuils et ses propres règles. → `tva.md`.
- **La responsabilité** : depuis la réforme du statut de l'entrepreneur individuel, le patrimoine
  personnel est en principe séparé du patrimoine professionnel — la protection ne dépend donc plus
  autant du choix société/EI qu'avant. ⚠️ Les **garanties personnelles données à une banque**
  passent par-dessus cette séparation, quelle que soit la forme.

## Où aller ensuite

- Seuils, abattements, cotisations et obligations du régime micro → `micro-entreprise.md`
- Articulation avec le chômage et les aides → `chomage-et-creation.md`
- TVA et clients étrangers → `tva.md`
- Rédaction de l'objet social et des statuts → skill `avocat`, `droit-des-societes.md`

## Sources

- Choisir son statut juridique, Urssaf — <https://www.urssaf.fr/accueil/choisir-statut-juridique.html>
- Comparatif des structures unipersonnelles, Bpifrance Création —
  <https://bpifrance-creation.fr/encyclopedie/structures-juridiques/entreprendre-seul/comparatif-structures-unipersonnelles>
- Comparaison EURL / SASU, Bpifrance Création —
  <https://bpifrance-creation.fr/encyclopedie/structures-juridiques/entreprendre-seul/comparaison-eurlsasu-entreprise-unipersonnelle>
- Comparateur de statut juridique, Urssaf —
  <https://mon-entreprise.urssaf.fr/simulateurs/comparaison-r%C3%A9gimes-sociaux>
- Formalités et guichet unique — <https://formalites.entreprises.gouv.fr/>

## Rappel de cadrage

Ce fichier alimente le skill `comptable`, un outil d'**aide à la décision**. Le choix d'une forme
juridique engage sur des années et se défait mal : faites-le valider par un expert-comptable
inscrit à l'Ordre avant de déposer quoi que ce soit.
