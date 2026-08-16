# Chômage et création d'activité : cumul, actualisation, aides

> **État : `RÉDIGÉ`** pour les mécanismes et les arbitrages. Chiffres vérifiés sur les pages
> officielles France Travail et Urssaf le **2026-08-16**, et reportés dans
> `data/parametres.json` avec leur source. **Un point reste explicitement non confirmé** —
> l'assiette retenue pour un micro-entrepreneur — et il est signalé comme tel ci-dessous.

## Pourquoi ce fichier existe

C'est la question la plus fréquente et la plus mal traitée du web français : *« je touche le
chômage, est-ce que je peux créer mon entreprise ? »*. La réponse courte est oui. La réponse utile
est : **il y a trois dispositifs, deux d'entre eux s'excluent, et le choix est difficile à
défaire**. Sur une allocation qui peut représenter plusieurs dizaines de milliers d'euros de
droits, se tromper d'aiguillage coûte plus cher que toute autre décision de la création.

## Ce qu'il faut établir avant de répondre

Ces six éléments changent la réponse, pas seulement les chiffres.

1. **Le droit restant** — combien de jours d'allocation, à quel montant journalier.
2. **⚠️ La date de fin du contrat de travail.** Elle décide de l'application du plafond de 60 %
   (voir plus bas). C'est devenu la question la plus discriminante des six.
3. **L'activité est-elle déjà créée ?** Avant ou après l'inscription, avant ou après l'ouverture
   des droits : le traitement diffère.
4. **Le revenu attendu** — combien, et surtout **quand**.
5. **Le besoin de trésorerie au démarrage** — y a-t-il un investissement à financer maintenant ?
6. **La situation du foyer** — l'allocation joue-t-elle un rôle de filet pour d'autres personnes ?
   Ce n'est pas une question financière mais une question de tolérance au risque, et elle tranche
   souvent seule.

## Les trois dispositifs

### 1. Le maintien de l'ARE

Vous conservez une allocation **mensuelle**, réduite en fonction du revenu déclaré. La formule
affichée par France Travail est :

> **Allocation mensuelle − 70 % des rémunérations déclarées au titre des assurances sociales.**

Les jours non consommés sont **reportés**, ce qui allonge d'autant la durée du droit.

**⚠️ Deux plafonds s'appliquent, et le second est récent :**

- Le revenu de l'activité **plus** l'allocation ne peut excéder **la moyenne des salaires qui a
  servi au calcul de l'ARE**.
- **Pour les contrats de travail terminés après le 1ᵉʳ avril 2025, le cumul est limité à 60 % des
  droits restants** à la date de démarrage effectif de l'activité.

★ **Ce second plafond change l'arbitrage historique.** Avant lui, on pouvait dire que le maintien
« n'annule pas les droits, il les étale ». **Ce n'est plus vrai** pour les contrats terminés après
le 1ᵉʳ avril 2025 : au-delà de 60 % des droits restants, le reste n'est pas reporté, il est perdu.
Toute réponse qui reprend l'ancien raisonnement sans vérifier la date de fin de contrat est
aujourd'hui fausse.

Si les rémunérations ne sont pas encore connues, un **paiement provisoire de 70 % de l'allocation**
est effectué, avec régularisation ensuite.

### 2. L'ARCE

**60 % des droits ARE restants**, versés en capital, **après déduction de 3 %** au titre du
financement des retraites complémentaires — **à la place** de l'allocation mensuelle.

- **1ᵉʳ versement** : à la date de création (ou d'ouverture des droits si elle est postérieure).
- **2ᵉ versement** : les 50 % restants **six mois après**, à condition de justifier que l'activité
  est toujours exercée et de ne pas être en CDI à temps plein.
- ⚠️ **L'ARCE est assujettie à la CSG et à la CRDS.** À anticiper dans le plan de trésorerie.
- ⚠️ **L'ARCE exige d'avoir obtenu l'ACRE.** Pas d'ACRE, pas d'ARCE — et l'ACRE a désormais un
  délai de demande très court (voir ci-dessous). C'est un enchaînement, pas deux guichets séparés.

### 3. L'ACRE

Exonération partielle des cotisations sociales personnelles pendant les **12 premiers mois**
d'activité (maladie-maternité, retraite de base, invalidité-décès, allocations familiales).

**⚠️ Le taux a été divisé par deux en cours d'année 2026.** Le **décret n° 2026-69 du 6 février
2026** ramène l'exonération de **50 % à 25 %** pour les **micro-entreprises créées ou reprises à
compter du 1ᵉʳ juillet 2026**. Concrètement, le taux de cotisations minoré passe de 50 % à 75 % des
taux normaux.

⇒ **La date de création commande le taux :**

| Micro-entreprise créée… | Exonération |
|---|---|
| avant le 1ᵉʳ juillet 2026 | **50 %** |
| à compter du 1ᵉʳ juillet 2026 | **25 %** |

**La demande n'est pas automatique** : elle doit être déposée **auprès de l'Urssaf au plus tard le
60ᵉ jour suivant la date d'ouverture de l'activité**. Passé ce délai, l'ACRE est perdue — et
l'ARCE avec elle, puisqu'elle en dépend.

⚠️ Ne dites pas que « la demande n'est plus automatique depuis 2026 » : **pour les
micro-entrepreneurs, elle ne l'a jamais été** depuis 2020. Ce qui a changé, c'est la longueur de la
fenêtre et l'harmonisation des règles entre formes juridiques.

Le demandeur ne doit pas en avoir déjà bénéficié au cours des trois années précédentes.

## L'arbitrage, révisé

Depuis le plafonnement à 60 %, **maintien et ARCE convergent sur le montant total** : environ 60 %
des droits restants dans les deux cas. Ce qui les distingue n'est donc plus « combien », mais
**sous quelle forme** :

> **Le maintien verse un revenu plancher chaque mois. L'ARCE verse un capital tout de suite, et
> supprime le plancher.**

- **Maintien** si le revenu sera lent, irrégulier, ou si l'allocation joue un rôle de filet pour
  le foyer.
- **ARCE** s'il y a un investissement précis à financer maintenant, et que le revenu viendra vite.

La question qui tranche reste la même : **« que feriez-vous de ce capital que vous ne pouvez pas
faire sans ? »** Sans réponse concrète, l'ARCE échange un plancher contre une somme qu'on aurait
touchée de toute façon.

⚠️ Et vérifiez la date de fin de contrat **avant** de dérouler cet arbitrage : si elle est
antérieure au 1ᵉʳ avril 2025, le plafond ne s'applique pas et le raisonnement change.

## ⚠️ Le point qui reste non confirmé : l'assiette du micro-entrepreneur

La formule officielle déduit **70 % des rémunérations déclarées**. Pour un micro-entrepreneur, la
question est : **70 % de quoi ?** Du chiffre d'affaires brut, ou du chiffre d'affaires après
l'abattement forfaitaire ?

Une documentation secondaire indique que l'assiette serait le **chiffre d'affaires après
abattement**, avec des taux de 71 % (achat-revente, fourniture, logement), 50 % (BIC artisanales et
commerciales) et 34 % (BNC, professions libérales). **Je n'ai pas trouvé cette précision sur une
page officielle France Travail**, et ce dépôt n'admet pas les sources secondaires.

L'enjeu n'est pas cosmétique : en BNC, la différence entre les deux lectures est de l'ordre d'un
tiers du chiffre d'affaires sur la base de calcul.

➡️ La valeur est dans `data/parametres.json` sous
`chomage_et_creation.are_base_de_calcul_micro`, marquée `a_verifier`. **Posez la question au
conseiller et demandez la réponse par écrit.** Ne l'estimez pas.

## L'actualisation mensuelle : là où ça dérape

Créer une activité en percevant l'ARE impose de **déclarer chaque mois** l'activité et les revenus.

Deux erreurs très courantes, toutes deux coûteuses :

- **Croire qu'un mois sans encaissement est un mois sans déclaration.** L'activité se déclare même
  à zéro.
- **Changer de convention en cours de route** entre la date de facture et la date d'encaissement.
  La règle applicable se vérifie, elle ne se devine pas, et elle s'applique de la même façon tous
  les mois.

Les justificatifs sont traités à échéance **annuelle**, ou **trimestrielle** pour les
micro-entrepreneurs qui le souhaitent — l'option trimestrielle réduit l'ampleur des régularisations.

Une omission n'est pas un oubli administratif : c'est une **fausse déclaration**, avec récupération
des sommes et sanction possible. Dites-le clairement, sans dramatiser mais sans l'atténuer.

## Autres points à ne pas oublier

- **La couverture sociale** ne suit pas automatiquement le même chemin que l'allocation.
- **L'ordre des opérations compte** : s'inscrire, ouvrir les droits, créer, demander l'ACRE dans
  les 60 jours. La chronologie produit des effets, et elle ne se rejoue pas.
- **Le conseiller France Travail est la seule source qui engage l'organisme.** Ce fichier prépare
  l'entretien, il ne le remplace pas : préparer les questions par écrit, demander les réponses par
  écrit.

## Ce qu'il faut demander au rendez-vous

Ces cinq questions décident :

1. **Ma date de fin de contrat est-elle postérieure au 1ᵉʳ avril 2025 ?** Donc le plafond de 60 %
   s'applique-t-il à mon dossier ?
2. Sur quelle assiette exactement l'allocation est-elle réduite dans mon cas de micro-entreprise —
   chiffre d'affaires brut ou après abattement ?
3. Quel est mon reliquat de droits, en jours et en montant journalier, à aujourd'hui ?
4. Si je choisis le maintien, quelle date de fin de droits projetez-vous, plafond compris ?
5. Quelles formations ou certifications pouvez-vous financer, et par quelle procédure ?

## Sources

- France Travail, *Je crée, je reprends une entreprise* —
  <https://www.francetravail.fr/candidat/mes-droits-aux-aides-et-allocati/a-chaque-situation-son-allocatio/quelle-est-ma-situation-professi/je-reprends-une-activite-ou-une/je-cree-je-reprends-une-entrepri.html>
- France Travail, *ARE, ARCE, Acre : le guide complet 2026* —
  <https://www.francetravail.fr/actualites/a-laffiche/2026/are-arce-acre-creer-son-entrepri.html>
- France Travail, *Aide à la reprise et à la création d'entreprise (ARCE)* —
  <https://www.francetravail.fr/candidat/je-creereprends-une-entreprise/les-aides-financieres-creation-d/aide-a-la-reprise-et-a-la-creati.html>
- Urssaf, *L'Acre* — <https://www.urssaf.fr/accueil/exoneration-acre-createur.html>
- Service-public, *Arce* — <https://entreprendre.service-public.fr/vosdroits/F15252>

## Rappel de cadrage

Ce fichier alimente le skill `comptable`, un outil d'**aide à la décision**. Il ne remplace ni un
expert-comptable inscrit à l'Ordre, ni votre conseiller France Travail — qui est, lui, la seule
source qui engage l'organisme.
