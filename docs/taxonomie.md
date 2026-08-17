# Taxonomie : quand un sujet devient un rôle

Ce dépôt suit une règle simple : **un plugin est un domaine, un skill est un rôle.** Ce document
explique comment on décide qu'un sujet mérite de devenir un rôle plutôt que de rester un fichier
de référence — pour que la décision soit reproductible, et pas affaire de goût.

## Ce qu'est un rôle, ici

Un rôle n'est pas un thème. C'est **une méthode d'entrée, une posture et des règles d'arrêt**.

Regardez la première question que pose chaque rôle existant — elles sont toutes différentes, et
c'est ça qui en fait des rôles :

| Rôle | Sa première question |
|---|---|
| `/juriste` | *Qui envers qui, et de quoi s'agit-il juridiquement ?* |
| `/immigration` | *Y a-t-il un délai qui court ?* |
| `/travail` | *Quelle convention collective ?* |
| `/logement` | *Que dit la loi, avant même de lire le bail ?* |
| `/famille` | *Y a-t-il un danger, et qu'est-ce qui relève du juge ?* |
| `/comptable` | *Quelle entreprise, quel régime ?* |
| `/impots` | *Quel foyer fiscal ?* |

Un sujet qui réutiliserait l'intake de son parent est un **fichier**, pas un rôle.

## Les cinq tests

Un sujet devient un rôle quand il en passe **au moins quatre sur cinq**.

**1. Le test de la langue d'entrée.** Les gens concernés formulent-ils leur problème **sans jamais
employer le vocabulaire du rôle parent** ? *« Ma carte expire »* n'est pas « juridique ». *« Je me
fais licencier »* n'est pas « avocat ». Si la description du parent ne peut pas honnêtement
déclencher sur leurs mots, il faut un rôle.

**2. Le test de la première question.** L'intake change-t-il vraiment ? Voir le tableau ci-dessus.

**3. Le test des sources.** Le sujet a-t-il un corpus officiel propre, inutile ailleurs ? CESEDA et
ANEF pour l'immigration, code.travail.gouv.fr et les conventions collectives pour le travail, l'ANIL
pour le logement.

**4. Le test de la ligne d'arrêt.** Les cas où il faut passer la main diffèrent-ils **en nature ou
en urgence** de ceux du parent ? OQTF, prescription prud'homale, trêve hivernale, violences
intrafamiliales. Si les règles d'arrêt du parent sur-protègent ou sous-protègent, il faut un rôle.

**5. Le test du volume.** Y a-t-il de quoi remplir **six à huit fichiers de référence** sans
dupliquer le parent ? En dessous, c'est un fichier.

### Deux corollaires

- **Un itinéraire n'est jamais un rôle.** « Créer ma boîte » traverse `comptable`, `avocat` et
  `immigration` ; « un décès » traverse `famille` et `impots`. Un parcours est un chemin **entre**
  rôles, et les chemins se multiplient sans fin. Ils vivent dans les renvois des SKILL.md.
- **Trois tests sur cinq : on attend.** On crée le rôle quand la demande le prouve, pas par
  anticipation.

## La règle structurelle : un fichier vit dans un seul rôle

Deux plugins peuvent être installés séparément. Un chemin relatif d'un rôle vers un autre casserait
donc chez la moitié des utilisateurs.

⇒ **Aucun fichier n'est partagé entre rôles.** Quand un sujet touche deux rôles, l'un le traite et
l'autre **renvoie par nom de rôle** — « la fiscalité de ce sujet vit dans le skill `impots` » — jamais
par chemin de fichier.

## Ce qu'on ne fait pas, et pourquoi

**Pas de rôles-professions** (`/notaire`, `/fiscaliste`, `/huissier`). C'est l'organigramme des
professions, pas la carte des questions. Quelqu'un qui a une question sur ses cryptos ne sait pas
s'il doit appeler un comptable ou un fiscaliste — et il n'a pas à le savoir. *(La posture
adversariale d'un contrôleur fiscal reste une bonne idée : elle deviendra un **fichier**
`simulation-controle.md`, pas un rôle.)*

**Pas de rôles-parcours** (`/createur`, `/expat`). Voir le corollaire ci-dessus.

## Rôles envisagés, pas encore créés

- **`/retraite`** et les **prestations sociales** (CAF, RSA, prime d'activité, APL, AAH). Ils
  passent les cinq tests, mais dans un **domaine à créer** : ni comptable ni juridique, la logique
  y est d'**obtenir un droit**, pas de se conformer à une obligation. Sources propres (CNAV, CAF,
  MSA). C'est le premier motif d'assistance dans les maisons France Services et il n'existe
  nulle part ici.
- **La consommation** reste un **fichier** de `/juriste` : même méthode, même posture, même issue —
  qualifier, mettre en demeure, saisir. Elle échoue au test 2.
