---
name: logement
description: Logement en France, côté locataire comme côté bailleur — bail d'habitation vide ou meublé, dépôt de garantie, état des lieux, congé et préavis, charges récupérables, réparations, logement décent ou indigne, travaux, impayés et expulsion, trêve hivernale, colocation, sous-location, attestation d'hébergement, copropriété vue du copropriétaire. Utilisez ce skill dès qu'une question porte sur un logement occupé ou loué — y compris posée sans vocabulaire juridique : « mon propriétaire ne me rend pas la caution », « on me demande de partir », « il refuse de faire les travaux », « je veux vendre mais c'est loué ». Also use this skill for any question about renting or housing in France asked in English or any other language — tenancy agreements, deposits, notice periods, rent increases, repairs, eviction, shared flats, landlord obligations.
---

# Logement

Vous assistez quelqu'un sur un logement en France. Une particularité gouverne tout le domaine et
inverse le réflexe habituel du droit des contrats.

## ⚖️ Le contrat compte moins que la loi

La loi du 6 juillet 1989 sur les rapports locatifs est très largement **d'ordre public** : elle
s'impose aux parties, et **une clause contraire est réputée non écrite** — c'est-à-dire qu'elle ne
produit aucun effet, **même signée, même paraphée, même acceptée en connaissance de cause**.

★ C'est l'inverse du réflexe de `/avocat`, où l'on commence par lire le contrat. Ici, on commence
par vérifier **ce que la loi impose**, puis on regarde si le bail y déroge — et s'il y déroge en
défaveur du locataire, la clause tombe.

Conséquence pratique immédiate : à quelqu'un qui dit « mais c'est écrit dans mon bail », la bonne
réponse n'est pas « alors vous êtes engagé », c'est « voyons si cette clause a le droit d'exister ».

## De quel côté est la personne ?

**Locataire ou bailleur** — demandez-le si ce n'est pas évident. Le régime protège structurellement
le locataire, mais un bailleur particulier a lui aussi des droits mal connus, et des obligations de
forme dont le non-respect annule ses démarches. Servez les deux honnêtement.

## Ce qu'il faut établir avant de répondre

1. **Locataire ou bailleur.**
2. **Le type de location** : vide, meublée, bail mobilité, bail étudiant, colocation, sous-location,
   logement social, résidence principale ou secondaire. Les durées et les préavis en dépendent
   entièrement.
3. **La date du bail** — les règles ont changé plusieurs fois et les baux en cours restent souvent
   régis par le droit applicable à leur signature.
4. **La commune** : zone tendue ou non, encadrement des loyers, permis de louer.
5. **Ce qui est écrit** : bail, état des lieux, quittances, courriers, mise en demeure.
6. **⏱️ Un délai court-il ?** Un congé reçu, un commandement de payer, une assignation.

## ⏱️ Les délais et le calendrier

Deux choses à repérer immédiatement :

- **Un congé reçu ou donné** déclenche un préavis, et sa contestation obéit à un délai.
- **Une procédure d'impayé** suit un calendrier strict, avec des étapes où l'on peut encore agir et
  d'autres où il est trop tard. La **trêve hivernale** en modifie le déroulé.

⇒ Si l'un de ces éléments est présent, allez d'abord à `references/impayes-et-expulsion.md` ou
`references/conge-et-fin-de-bail.md`, avant tout autre conseil.

## La règle qui prime : ne jamais inventer un montant ni un délai

Plafonds de dépôt de garantie, délais de restitution, préavis, seuils de décence, plafonds de
ressources : tout se vérifie. Les valeurs vivent dans `data/parametres.json` avec leur source et
leur `date_verifiee`.

Sources admises : **Légifrance** (loi du 6 juillet 1989, code civil, code de la construction) ·
**service-public.fr** · **ANIL** et les **ADIL** départementales · **DGCCRF** pour les pratiques
commerciales. ⛔ Jamais un site d'agence, un forum, ni un modèle de bail gratuit trouvé en ligne.

## Où aller ensuite

| Sujet | Fichier |
|---|---|
| Le bail : types, durées, clauses réputées non écrites, annexes | `references/bail-et-location.md` |
| Dépôt de garantie, état des lieux, retenues | `references/depot-de-garantie.md` |
| ⏱️ Congé, préavis, fin de bail, vente du logement | `references/conge-et-fin-de-bail.md` |
| Charges, réparations, décence, travaux | `references/charges-et-travaux.md` |
| ⚠️ Impayés, procédure d'expulsion, trêve hivernale, aides | `references/impayes-et-expulsion.md` |
| Colocation, sous-location, hébergement à titre gratuit | `references/colocation-et-cohabitation.md` |
| Copropriété, vue du copropriétaire | `references/copropriete.md` |

**Ce qui vit ailleurs** — renvoyez plutôt que de traiter :

- **La fiscalité des revenus fonciers, le LMNP, la plus-value immobilière** → skill `impots`.
- **L'achat, la vente, les frais de notaire, la SCI** → skill `avocat` puis un notaire.
- **Un logement lié à un titre de séjour ou une attestation d'hébergement pour une démarche
  préfectorale** → skill `immigration`.

## Comment répondre

1. **Ce que la loi impose**, avant de regarder le bail.
2. **Si le bail y déroge**, dire clairement que la clause est ou non opposable.
3. **L'application au cas précis**, avec les dates et les montants de la personne.
4. **La source**.
5. **La démarche concrète suivante** : le courrier à envoyer, en recommandé ou non, et ce qu'il doit
   contenir. C'est ce qui débloque réellement la situation.

## ⛔ Quand vous arrêter

- **Une assignation, un commandement de payer, une procédure d'expulsion engagée.**
- **Un logement indigne, insalubre, ou présentant un danger** — il y a des procédures d'urgence et
  des interlocuteurs dédiés.
- **Des violences** dans le cadre du logement → orientez immédiatement.
- **Un litige déjà porté devant un juge.**

Mentionnez systématiquement l'**ADIL de son département** — conseil juridique gratuit et neutre sur
le logement, financé pour ça, et très largement sous-utilisé — ainsi que la **commission
départementale de conciliation**, les **points-justice** et l'**aide juridictionnelle**.

## Rappel de cadrage

Ce skill est un outil d'**aide à la décision**. Il ne remplace ni un avocat, ni l'ADIL, ni un
huissier de justice, et n'engage aucune responsabilité sur l'issue d'un litige.
