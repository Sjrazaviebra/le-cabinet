# La déclaration de revenus, comme un parcours

> **État : `RÉDIGÉ`** pour le calendrier, la déclaration automatique et la correction. **`À ÉCRIRE`**
> pour le détail des cases et des annexes. Vérifié le **2026-08-17** sur `impots.gouv.fr`.
> ⚠️ **Les dates changent chaque année** : elles vivent dans `data/parametres.json` avec leur
> millésime, jamais en dur dans le raisonnement.

## ⏱️ Ce qui est ouvert aujourd'hui, et personne ne le sait

Nous sommes **après** la période déclarative de 2026. Mais **le service de correction en ligne est
ouvert**, et c'est l'information la plus utile qu'on puisse donner à cette période de l'année : une
déclaration déjà déposée **se corrige en ligne**, sans réclamation, sans courrier, sans justifier.

⚠️ **Deux sources officielles ne donnent pas la même fenêtre** de correction pour les revenus 2025 :
la page des modalités annonce **de mi-août à mi-décembre 2026**, une actualité de service-public
annonce **du 29 juillet au 30 novembre 2026**. ⇒ **La fenêtre est ouverte, la date de clôture est à
lire sur impots.gouv.fr avant de s'y fier.** Nous ne trancherons pas entre deux sources officielles
qui se contredisent.

## Le calendrier 2026 (revenus 2025)

| Mode | Date limite |
|---|---|
| **Papier** | **mardi 19 mai 2026** à minuit |
| **En ligne** — départements **01 à 19** et **non-résidents** | **21 mai 2026** à 23 h 59 |
| **En ligne** — départements **20 à 54** | **28 mai 2026** à 23 h 59 |
| **En ligne** — départements **55 à 974** et **976** | **4 juin 2026** à 23 h 59 |

Les formulaires papier sont expédiés **courant avril** aux personnes ayant déclaré sur papier l'année
précédente.

★ **Le classement par département est une source d'erreur constante** : la date dépend du
**département de résidence**, pas du lieu de travail ni du lieu de naissance. Et la déclaration
**papier** a une date **antérieure à toutes les dates en ligne** — c'est contre-intuitif, et ça piège
ceux qui hésitent entre les deux modes.

## La déclaration automatique — un droit tacite, pas une dispense de vérifier

Aussi appelée **déclaration tacite** : l'administration valide la déclaration **sans que vous
intervieniez**.

**Conditions cumulatives** :

- la **déclaration préremplie contient tous vos revenus et charges** ;
- vous **n'avez signalé aucun changement de situation** en 2025 — adresse, situation familiale,
  création d'un prélèvement à la source.

**Elle n'est pas obligatoire** : on peut continuer de déclarer et de corriger comme avant. Et les
personnes éligibles peuvent la **corriger pendant toute la période déclarative**, jusqu'à leur date
limite départementale.

⚠️ **Ne présentez jamais la déclaration automatique comme « rien à faire ».** Elle veut dire *« si
vous ne dites rien, l'administration retient ce qu'elle a »*. Si un revenu manque, une charge n'a pas
été remontée, ou une réduction n'a pas été demandée, **le silence vaut acceptation d'un calcul
incomplet**. Le bon conseil est donc : **lire la déclaration préremplie, même quand on n'a rien à
changer.**

## Corriger après coup — et la limite qu'il faut connaître

Le **service de correction en ligne** permet de modifier une déclaration déjà déposée, **y compris
quand on a bénéficié de la déclaration automatique**.

**Mais certaines informations ne peuvent PAS être corrigées par ce service** :

- un **changement de situation familiale** — mariage, PACS, rupture de PACS, divorce, décès ;
- une **mise à jour de l'état civil** ;
- la **désignation d'un tiers de confiance** ;
- un **changement d'adresse** ;
- l'ajout ou la modification de l'**adresse d'un étudiant**.

⇒ Pour ces cas, la correction en ligne ne suffit pas : il faut passer par une **réclamation** ou par
la messagerie sécurisée. → `reclamation-et-controle.md`

★ **La distinction est structurante** : le service de correction traite les **chiffres**, pas
l'**état civil**. Beaucoup de gens croient leur correction faite alors qu'elle portait précisément
sur ce que le service refuse.

## Les formulaires

| Formulaire | Ce qu'il porte |
|---|---|
| **2042** | la déclaration principale |
| **2042-C** | déclaration complémentaire |
| **2042-C-PRO** | revenus des professions non salariées |
| **2042-RICI** | les **réductions et crédits d'impôt** les plus courants |

★ **Le 2042-RICI est l'annexe la plus oubliée**, et c'est celle qui fait baisser l'impôt. Quand
quelqu'un demande « comment payer moins », la première question utile n'est pas un montage : c'est
*« avez-vous rempli le RICI ? »*

## Ce qui reste à écrire

- Le détail des **cases** les plus fréquentes et des pièges de remplissage.
- La **première déclaration** : comment obtenir les formulaires, où les déposer.
- La déclaration en cas de **changement de situation** en cours d'année.
- Les **non-résidents** et leurs règles propres.
- La déclaration d'un micro-entrepreneur — ⚠️ articulation avec le skill `comptable`.

## Sources

- Les modalités de la déclaration de revenus en 2026 —
  <https://www.impots.gouv.fr/les-modalites-de-la-declaration-de-revenus-en-2026>
- Corriger une déclaration déjà déposée —
  <https://www.impots.gouv.fr/particulier/questions/je-veux-corriger-la-declaration-que-jai-deja-deposee-comment-proceder>
- Date limite de dépôt —
  <https://www.impots.gouv.fr/toutes-les-questions/particulier/quelle-date-dois-je-faire-ma-declaration>
- Déclaration de revenus annuelle, service-public —
  <https://www.service-public.gouv.fr/particuliers/vosdroits/F358>
- Formulaire n° 2042 — <https://www.impots.gouv.fr/formulaire/2042/declaration-des-revenus>

## Rappel de cadrage

Ce fichier alimente le skill `impots`, un outil d'**aide à la décision**. Il dit **où trouver
l'information et comment vérifier** — il ne remplit aucune déclaration à la place de quiconque et ne
certifie aucun calcul. Établir les déclarations d'autrui à titre habituel relève du monopole de
l'ordre des experts-comptables.
