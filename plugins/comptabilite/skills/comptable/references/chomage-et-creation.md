# Chômage et création d'activité : cumul, actualisation, aides

> **État : `PARTIEL`** — la méthode et les arbitrages sont rédigés. **Aucune valeur chiffrée n'est
> encore vérifiée** : les taux, seuils et formules vivent dans `data/parametres.json`, tous marqués
> `a_verifier`. Tant qu'ils le sont, énoncez le raisonnement et **laissez le chiffre en blanc** en
> renvoyant à la source. Un raisonnement juste avec un trou explicite est utilisable ; un chiffre
> faux ne l'est pas.

## Pourquoi ce fichier existe

C'est la question la plus fréquente et la plus mal traitée du web français : *« je touche le
chômage, est-ce que je peux créer mon entreprise ? »*. La réponse courte est oui. La réponse utile
est : **il y a trois dispositifs, deux d'entre eux s'excluent, et le choix est difficile à
défaire**. Sur une allocation qui peut représenter plusieurs dizaines de milliers d'euros de
droits, se tromper d'aiguillage coûte plus cher que toute autre décision de la création.

## Ce qu'il faut établir avant de répondre

Ces cinq éléments changent la réponse, pas seulement les chiffres.

1. **Le droit restant** — combien de jours d'allocation, à quel montant journalier. C'est
   l'assiette de tout, y compris de l'ARCE.
2. **L'activité est-elle déjà créée ?** Avant ou après l'inscription, avant ou après l'ouverture
   des droits : le traitement diffère.
3. **Le revenu attendu** — combien, et surtout **quand**. C'est le calendrier, plus que le total,
   qui décide entre maintien et ARCE.
4. **Le besoin de trésorerie au démarrage** — y a-t-il un investissement à financer maintenant ?
5. **La situation du foyer** — l'allocation joue-t-elle un rôle de filet pour d'autres personnes ?
   Ce n'est pas une question financière mais une question de tolérance au risque, et elle tranche
   souvent seule.

Si ces éléments ont déjà été donnés, ne les redemandez pas. S'il en manque un et qu'il change la
recommandation, demandez celui-là uniquement.

## Les trois dispositifs

### 1. Le maintien de l'ARE

Vous gardez votre allocation **mensuelle**, réduite en fonction du revenu déclaré. Les jours non
consommés ne sont pas perdus : ils sont **reportés**, ce qui allonge d'autant la durée du droit.

C'est le point que la plupart des gens ne comprennent pas, et il est décisif : **le maintien ne
fait pas perdre les droits, il les étale.** Gagner peu au début ne « gaspille » donc pas
l'allocation.

- ➕ Un revenu plancher pendant toute la montée en charge.
- ➕ Le droit s'étire au lieu de se consommer.
- ➖ Aucun capital disponible pour investir maintenant.
- ➖ Une **déclaration mensuelle obligatoire** — c'est là que les ennuis arrivent, voir plus bas.

### 2. L'ARCE

Une partie du reliquat de droits est versée **en capital**, en deux fois, **à la place** de
l'allocation mensuelle.

- ➕ De la trésorerie immédiate pour investir.
- ➖ **Renonciation au versement mensuel.** Si l'activité ne décolle pas, il n'y a plus de filet.
- ➖ Le capital versé est inférieur au total que le maintien aurait permis de percevoir.

⚠️ **ARCE et maintien ne se cumulent pas.** C'est l'aiguillage principal, et il se prend une fois.

### 3. L'ACRE

D'une autre nature : ce n'est pas une allocation mais une **exonération partielle de cotisations
sociales** au démarrage, sous conditions. Elle se combine avec l'un ou l'autre des deux dispositifs
précédents — elle ne s'y substitue pas.

## L'arbitrage, en une phrase

> **Le maintien convient à une activité qui démarre lentement et irrégulièrement. L'ARCE convient
> à une activité qui a besoin de capital tout de suite et qui produira du revenu vite.**

Autrement dit : l'ARCE achète de la trésorerie avec de la sécurité. Si le projet n'exige pas
d'investissement au démarrage — ce qui est le cas de presque toutes les prestations
intellectuelles — l'ARCE vend le filet sans rien acheter en échange.

Posez donc la question dans ce sens : **« que feriez-vous de ce capital que vous ne pouvez pas
faire sans ? »** S'il n'y a pas de réponse concrète, le maintien est probablement le bon choix.

## ⚠️ Le point que presque tout le monde rate : l'assiette du micro-entrepreneur

Pour un micro-entrepreneur, la question n'est pas *« combien j'ai encaissé »* mais **sur quelle
assiette l'allocation est réduite** : le chiffre d'affaires brut, ou le chiffre d'affaires après
l'abattement forfaitaire ?

L'écart entre les deux est considérable — l'abattement représente une fraction importante du
chiffre d'affaires en prestation de services. Une réponse donnée sans avoir vérifié ce point précis
est une réponse fausse, même si tout le reste du raisonnement est juste.

➡️ Cette valeur est dans `data/parametres.json` sous
`chomage_et_creation.are_base_de_calcul_micro`, et elle est marquée `a_verifier`. Tant qu'elle
l'est : **dites-le** et renvoyez à France Travail. Ne l'estimez pas.

## L'actualisation mensuelle : là où ça dérape

Créer une activité en percevant l'ARE impose de **déclarer chaque mois** l'activité et les revenus.

Deux erreurs très courantes, toutes deux coûteuses :

- **Croire qu'un mois sans encaissement est un mois sans déclaration.** L'activité se déclare même
  à zéro.
- **Déclarer au moment de la facture plutôt qu'à l'encaissement**, ou l'inverse. La règle
  applicable se vérifie, elle ne se devine pas — et elle s'applique de la même façon tous les mois.

Une omission n'est pas un oubli administratif : c'est une **fausse déclaration**, avec récupération
des sommes et sanction possible. Dites-le clairement, sans dramatiser mais sans l'atténuer.

## Autres points à ne pas oublier

- **La couverture sociale** ne suit pas automatiquement le même chemin que l'allocation.
- **L'ordre des opérations compte** : s'inscrire, ouvrir les droits, créer. La chronologie produit
  des effets, et elle ne se rejoue pas.
- **Le conseiller France Travail est la seule source qui engage l'organisme.** Ce fichier prépare
  l'entretien, il ne le remplace pas : faire préparer les questions par écrit, et demander les
  réponses par écrit.

## Ce qu'il faut demander au rendez-vous

Une liste courte vaut mieux qu'une longue. Ces quatre-là décident :

1. Sur quelle assiette exactement mon allocation est-elle réduite, dans mon cas de micro-entreprise ?
2. Quel est mon reliquat de droits, en jours et en montant journalier, à aujourd'hui ?
3. Si je choisis le maintien, quelle date de fin de droits projetez-vous ?
4. Quelles formations ou certifications pouvez-vous financer, et par quelle procédure ?

## Sources

Le texte et le simulateur officiels font foi. Toute valeur qui en sort va dans
`data/parametres.json` avec sa date de vérification.

- <https://www.francetravail.fr/candidat/mes-droits-aux-aides-et-allocations/>
- <https://www.urssaf.fr/accueil/independant/creer-mon-entreprise/aide-creation-acre.html>
- <https://entreprendre.service-public.fr/>
- <https://bpifrance-creation.fr/>

## Rappel de cadrage

Ce fichier alimente le skill `comptable`, un outil d'**aide à la décision**. Il ne remplace ni un
expert-comptable inscrit à l'Ordre, ni votre conseiller France Travail — qui est, lui, la seule
source qui engage l'organisme.
