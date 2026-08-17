# Taxonomie du domaine `comptabilite`

Le domaine `juridique` a été découpé au critère de [`taxonomie.md`](taxonomie.md) : cinq rôles issus de
cinq méthodes d'entrée distinctes. **Le domaine `comptabilite`, lui, ne l'a jamais été.** Il a hérité
d'une intuition de départ — *« entreprise d'un côté, particulier de l'autre »* — et personne n'y est
revenu quand les sujets se sont accumulés. Ce fichier applique enfin le critère.

## Ce que la division héritée ne voyait pas

`comptable` et `impots` répondent tous deux à la question *« combien, et selon quelles règles ? »* Ils
raisonnent par **régime** et par **exercice**. Cette maille est juste pour une déclaration ou une
clôture, et **muette sur trois questions qui n'ont rien à voir** :

| Question réelle | Ce que la division héritée en faisait |
|---|---|
| « ma banque me refuse un compte » | nulle part |
| « on me demande de me porter caution » | nulle part |
| « je ne pourrai pas payer l'échéance de ce mois » | nulle part |
| « où mettre mon épargne, et comment ne pas me faire avoir » | nulle part |

★ **Ce ne sont pas des trous de contenu, ce sont des trous de MÉTHODE.** Aucune quantité de fichiers
ajoutés dans `comptable` ne les aurait comblés, parce que la première question n'est pas la même :
`comptable` demande *« quel régime ? »*, ces situations demandent *« quelle échéance court ? »* et
*« quel horizon ? »*.

## Les cinq tests, appliqués

Rappel du critère : **langue d'entrée · première question · sources propres · ligne d'arrêt · volume
(6-8 fichiers)**. Quatre suffisent.

| Candidat | Langue d'entrée | Première question | Sources propres | Ligne d'arrêt | Volume | Verdict |
|---|:--:|:--:|:--:|:--:|:--:|---|
| `comptable` | ✅ | quel régime ? | impots.gouv, urssaf, BOFiP | monopole de l'Ordre | 10 | **existe** |
| `impots` | ✅ | quel foyer ? | impots.gouv, BOFiP | informer, jamais remplir | 10 | **existe** |
| **`financement`** | ✅ | quelle échéance court ? | CMF, Banque de France, médiateur du crédit | ⛔ pas de recommandation personnalisée | 8 | **✅ 5/5 → rôle** |
| **`patrimoine`** | ✅ | quel horizon, quel risque ? | **AMF**, Banque de France (éducation financière), ACPR | ⛔ pas de recommandation personnalisée | 8 | **✅ 5/5 → rôle** |
| ~~`banque`~~ | ✅ | — | mêmes que `financement` | — | 4 | **❌ absorbé par `financement`** |
| ~~`investissement`~~ | ✅ | — | mêmes que `patrimoine` | — | — | **❌ le nom invite l'acte réglementé** — voir plus bas |

★ **`banque` échoue sur la première question et sur le volume** : « la banque » est un
*interlocuteur*, pas une méthode. Les questions bancaires se répartissent entre un compte refusé, un
crédit rompu, une caution signée, un incident de paiement — toutes gouvernées par **une échéance**.
C'est `financement`.

★★ **`investissement` échoue sur son nom, pas sur son sujet.** Un rôle qui s'appelle
« investissement » sera sollicité pour *« qu'est-ce que je prends ? »*, c'est-à-dire précisément l'acte
réglementé. Le même contenu sous le nom **`patrimoine`**, avec une première question qui porte sur
l'**horizon** et le **risque** plutôt que sur le produit, oriente l'échange du bon côté de la ligne.
**Le nom d'un rôle n'est pas cosmétique : il fixe ce qu'on vient lui demander.**

## ⚖️ La frontière du conseil en investissement — révision d'une erreur

Ce dépôt avait d'abord interdit le **sujet** de l'investissement. **C'était une erreur d'analyse, et
elle est corrigée ici.** Ce que disent les textes, vérifié :

- **`L321-1` CMF n'énonce pas la définition** du conseil en investissement : il l'énumère parmi les
  services d'investissement, et le texte se clôt sur *« Un décret précise la définition de ces
  services. »* Ce sont les **instruments financiers de `L211-1`** qui délimitent le champ.
- Le statut réglementé s'attache à celui qui fournit le service **« à titre de profession
  habituelle »**, et le CIF de **`L541-1`** est défini par l'exercice **« à titre habituel »**.
- Ce qui est réprimé par **`L573-1`** est donc l'**exercice illégal d'une activité**, pas le fait de
  parler d'un sujet.

⇒ **La ligne ne passe pas entre les sujets, elle passe entre deux actes** :

| ✅ Information, éducation, pédagogie | ⛔ Conseil en investissement |
|---|---|
| comment fonctionne un PEA, une assurance-vie, un ETF | *« vu votre situation, prenez ceci »* |
| ce que des frais de 2 % font à une performance sur 20 ans | un arbitrage adapté à une personne |
| ce qu'est la diversification, la volatilité, la liquidité | un choix d'instrument financier précis |
| comment lire un document d'information réglementaire | une allocation recommandée |
| **comment reconnaître une arnaque, et vérifier un agrément** | une prédiction de marché |

★★ **L'AMF fait elle-même de l'éducation des investisseurs sa mission** : elle publie des guides
pédagogiques et des **listes noires**. Un rôle qui explique et qui met en garde est du même côté
qu'elle. ⚠️ Ce raisonnement est celui du dépôt, pas un avis juridique : la définition du service
figure au **décret** que nous n'avons pas encore lu article par article, et ce point est marqué
`a_verifier` dans le rôle `juriste`.

★ **Et le fichier le plus utile de ce rôle n'est pas celui qu'on imagine.** Pour quelqu'un
d'ordinaire, savoir **comment ne pas se faire escroquer** vaut plus que n'importe quelle comparaison
d'enveloppes : usurpation d'établissements agréés, faux conseillers, faux livrets, trading en ligne,
crypto. Refuser le sujet en bloc, comme ce dépôt l'a d'abord fait, **privait le lecteur de la seule
protection dont il avait besoin.**

## La structure retenue pour le domaine

```
plugins/comptabilite/skills/
├── comptable/     10 fichiers — l'entreprise : régime, obligations, comptes
├── impots/        10 fichiers — le particulier : ce qu'il déclare et ce qu'il paie
├── financement/    8 fichiers — l'argent de l'ACTIVITÉ : banque, crédit, trésorerie
└── patrimoine/     8 fichiers — l'argent PERSONNEL : enveloppes, frais, risque, arnaques
```

**La ligne de partage entre les quatre, en une phrase chacun :**

- `comptable` — *ce que l'entreprise doit tenir et déclarer.*
- `impots` — *ce que le foyer doit déclarer et payer.*
- `financement` — *l'argent qui manque à l'activité, et l'échéance qui court.*
- `patrimoine` — *l'argent qui dort, et ce qui le grignote ou le vole.*

⚠️ **Recouvrements assumés, et qui traite quoi :**

| Sujet à cheval | Traité par | Renvoie |
|---|---|---|
| Fiscalité d'un placement (PER, assurance-vie, PEA, RSU) | `impots` | `patrimoine` renvoie à `impots` |
| Mécanique d'un placement, frais, risque | `patrimoine` | `impots` renvoie à `patrimoine` |
| Comptabilisation des frais et intérêts bancaires | `comptable` | `financement` renvoie à `comptable` |
| Règles juridiques de la banque | `financement` | `juriste` renvoie à `financement` |
| Qui a le droit de conseiller, et les sanctions | `juriste` | les quatre y renvoient |
| Leviers légaux de réduction d'impôt — **la carte** | `financement` | pointe vers chaque fichier détaillé |

★ **La carte des leviers reste dans `financement` et non dans `impots`**, parce qu'elle se lit avec
une question de trésorerie (*« qu'est-ce que je peux faire cette année ? »*) et non de déclaration.
Et parce qu'elle doit porter la règle de lecture qui évite l'erreur la plus commune : **un levier qui
DÉCALE l'impôt n'est pas un levier qui le SUPPRIME.**

## Ce que la taxonomie refuse encore

- ⛔ **Un rôle par produit** (`assurance-vie`, `pea`, `crypto`) : ce sont des sujets, pas des
  méthodes. Ils vivent en fichiers.
- ⛔ **Un rôle « gestion de patrimoine »** au sens du métier : ce serait un rôle-profession, exactement
  l'erreur que [`taxonomie.md`](taxonomie.md) écarte pour un public généraliste.
- ⛔ **Un rôle « optimisation fiscale »** : le nom appelle le montage, et le montage appelle l'abus de
  droit. Les leviers sont une carte, pas une promesse.
- ⏳ **Envisagé, pas tranché** : un rôle `social` (retraite, prestations CAF, arrêts et invalidité).
  Sources propres évidentes, ligne d'arrêt nette, volume suffisant — mais il n'appartient probablement
  pas au domaine `comptabilite`.
