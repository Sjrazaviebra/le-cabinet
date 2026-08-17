# Trésorerie et besoin en fonds de roulement

> **État : `PARTIEL`** — **couvert** : l'écart entre résultat et trésorerie, le BFR, le plan de
> trésorerie, les quatre outils de financement du poste client, le crédit inter-entreprises, la TVA
> comme piège de trésorerie, les acomptes, et quoi faire quand l'argent manque ce mois-ci.
> **Non couvert** : le **coût chiffré** de l'affacturage, de l'escompte et de l'assurance-crédit —
> ⚠️ **aucune source officielle ne le publie**, et ce fichier préfère un trou à un chiffre inventé ;
> l'**assurance-crédit** comme produit, faute de fiche officielle dédiée ; le recouvrement des
> impayés.
> Vérifié le **2026-08-17**. Fiches `entreprendre.service-public.gouv.fr` du 09/03/2026 (équilibre
> financier), 25/06/2026 (marchés publics), 08/07/2026 (financement bancaire et bonnes pratiques),
> 19/01/2026 (tableau de bord), 26/12/2025 (business plan), et **27/11/2024** (escompte, mobilisation
> de créance, solutions de trésorerie), **12/08/2024** (prêt inter-entreprises), **12/09/2023**
> (affacturage) — ⚠️ **ces trois dernières pages ont plus de six mois : à recouper.** Code général
> des impôts, article 269, version en vigueur au 01/01/2023.

## ★★ Le résultat et la trésorerie ne sont pas la même chose

Une facture émise est un **produit comptable**. Elle entre dans le résultat le jour de son émission —
et elle n'est **pas de l'argent**. Elle le devient au jour de l'encaissement, s'il arrive.

Deux comptes tenus dans deux unités différentes coexistent donc :

| | Le compte de résultat | Le plan de trésorerie |
|---|---|---|
| **Unité** | l'**engagement** : facture émise, achat engagé | l'**encaissement** et le **décaissement** réels |
| **Ce qu'il dit** | si l'activité est rentable | si l'entreprise peut payer **vendredi** |
| **Ce qu'il ignore** | le moment où l'argent bouge | si l'activité gagne de l'argent |

⇒ **Le décalage** : on paie ses fournisseurs, ses salaires et ses cotisations **avant** d'encaisser
ses clients. Ce décalage doit être financé, et ce financement s'appelle le BFR. Le mécanisme
comptable qui produit cet écart — comptabilité d'engagement contre comptabilité de trésorerie — vit
chez le rôle `comptable`, `comptabilite-generale.md` ; les mentions et l'émission de la facture
elle-même dans `facturation.md` du même rôle.

★★ **Et voici le piège que personne n'anticipe : la croissance CONSOMME de la trésorerie.** Chaque
vente supplémentaire allonge le poste clients avant d'alimenter le compte. **Plus on vend, plus le
BFR grossit.** L'entreprise la plus exposée n'est donc pas celle qui va mal — c'est celle qui va
bien, vite, avec un carnet de commandes plein. **On ne dépose pas le bilan faute de clients : on le
dépose faute d'argent le jour d'une échéance.**

## Le BFR, lu sans jargon

> « Besoin en fonds de roulement (BFR) = Stock + Créances clients – Dettes fournisseurs »

Trois lignes, une seule question : **combien d'argent le cycle d'exploitation immobilise en
permanence.**

- **Stock** — de l'argent transformé en marchandises qui ne sont pas encore vendues.
- **Créances clients** — du travail déjà livré, déjà facturé, **pas encore payé**.
- **Dettes fournisseurs** — en négatif, parce que **ce que je n'ai pas encore payé, mes fournisseurs
  me le financent**.

> « Si le BFR est positif, cela signifie que l'entreprise a besoin de trésorerie pour financer le
> décalage entre les décaissements et les encaissements. »

★ **Un BFR négatif n'est pas une anomalie, c'est un modèle** : les clients paient avant les
fournisseurs, et le cycle se finance tout seul. C'est ce que produisent l'abonnement, le prépayé et
l'acompte. **La question stratégique n'est pas « à quel prix je vends » mais « qui paie en
premier ».**

⚠️ **Ne pas confondre avec le fonds de roulement**, autre formule et autre sujet :
> « Fonds de roulement (FR) = Capitaux propres + Dettes - Actifs immobilisés »

Le FR mesure les ressources durables disponibles ; le BFR mesure ce que le cycle immobilise. **Un FR
positif qui ne couvre pas le BFR laisse quand même une trésorerie négative** — c'est la situation
classique de l'entreprise qui « a des fonds propres » et pas d'argent.

## Le plan de trésorerie

Il se tient **en date d'encaissement et de décaissement**, jamais en date de facture. C'est toute sa
différence avec le compte de résultat, et c'est la seule chose qui compte.

**La maille.** Le mensuel suffit pour voir venir ; il ne suffit pas pour survivre. Une rupture se
joue sur quelques jours autour d'une échéance. Pour une structure jeune, l'analyse des écarts entre
prévu et réalisé est recommandée « hebdomadairement ou mensuellement » — ⇒ **maille hebdomadaire dès
que la marge de manœuvre est courte.** Dans un prévisionnel de création, le budget se construit
« sur les 3 années à venir » et forme l'un des quatre tableaux du prévisionnel financier, avec le
compte de résultat, le bilan et le plan de financement.

### ★ Ce qu'il faut y mettre, et que personne n'y met

Les plans de trésorerie faux le sont presque toujours par **omission de sorties certaines** :

- ★★ **la TVA à décaisser** — voir plus bas, ce n'est pas une charge, et c'est la première cause de
  trou ;
- **les cotisations sociales** et leurs régularisations, dont le calendrier vit chez le rôle
  `comptable` ;
- **les échéances fiscales annuelles ou trimestrielles** — acomptes d'impôt sur les sociétés,
  cotisation foncière des entreprises, taxes assises sur la masse salariale : elles n'apparaissent
  jamais dans un chiffre d'affaires mensuel lissé ;
- **la saisonnalité** — un mois creux se paie deux mois plus tard, pas le mois même ;
- **le remboursement de l'avance** perçue sur un marché public : elle se rembourse (article
  R2191-11), donc elle **décale** la trésorerie, elle ne l'augmente pas définitivement ;
- **les retenues de garantie** et les échéances annuelles à prélèvement unique (assurances,
  abonnements, logiciels) ;
- **les décalages d'encaissement réels**, pas contractuels : la date à laquelle ce client-là paie,
  telle qu'observée, et non celle inscrite dans les conditions générales.

⚠️ **Un plan de trésorerie qui ne descend jamais sous zéro est probablement faux.** S'il n'y a aucun
point bas, c'est en général qu'une sortie certaine a été oubliée.

## Financer le poste client : quatre outils, trois questions

Pour chacun, seules trois questions décident : **qui avance l'argent, qui garde le risque d'impayé,
et le client le voit-il ?**

| | **Affacturage** | **Mobilisation de créance** (cession Dailly) | **Escompte** | **Assurance-crédit** |
|---|---|---|---|---|
| **Ce qui est cédé** | toutes créances professionnelles | toutes créances professionnelles | ⚠️ **effets de commerce uniquement** | rien — on assure |
| **Qui porte le risque d'impayé** | ★ **le factor** | **l'entreprise** | **l'entreprise** | l'assureur, dans les limites du contrat |
| **Gestion du poste clients** | acquise par le factor | conservée par l'entreprise | conservée par l'entreprise | conservée |
| **Le client le voit-il ?** | **oui** — le factor se fait payer directement | **selon la forme** : notifiée, l'établissement écrit au client ; simple, l'entreprise l'informe | oui, il a accepté l'effet | non |
| **Délai d'obtention** | 24 à 48 heures | dès l'émission de la facture | rapide | sans objet |
| **Coût officiellement chiffré** | ⚠️ **aucun** | **autour de 10 % du montant HT cédé** | ⚠️ **aucun** | ⚠️ **aucun** |

**Le mécanisme, en une phrase chacun.**

- **Affacturage** — l'entreprise cède ses créances à une société d'affacturage agréée comme
  **société de financement**, qui est subrogée dans ses droits et se fait payer elle-même auprès des
  clients. Réservé au **BtoB** : « toutes les créances qu'elle détient sur ses clients
  professionnels ».
- **Mobilisation de créance professionnelle** — l'entreprise **cède ou nantit** ses créances
  professionnelles auprès d'un établissement financier, par bordereau, dans le cadre des articles
  **L313-23 à L313-34** du code monétaire et financier. Elle **garde la gestion de sa relation
  client**, et le risque avec.
- **Escompte** — la banque avance le montant d'un **effet de commerce** non échu, contre
  rémunération.
- **Assurance-crédit** — un contrat d'assurance couvrant le défaut de paiement du client. La seule
  mention officielle trouvée est indirecte : la fiche affacturage indique que le **factor** se
  protège lui-même par « une assurance crédit et/ou d'un fonds de garantie ». ⚠️ **Aucune fiche
  officielle dédiée n'a été trouvée** ⇒ ni prime, ni taux de couverture, ni franchise ne sont écrits
  ici.

★★ **La comparaison utile n'est pas le prix, c'est le transfert de risque.** En affacturage, le
risque d'impayé passe au factor ; en mobilisation de créance comme en escompte, **il reste sur
l'entreprise** : « le risque d'impayé pèse donc sur l'entreprise qui a mobilisé ses créances », et à
l'escompte, si le client ne paie pas, « c'est à l'entreprise qui a réalisé l'escompte de payer le
montant de l'effet de commerce escompté à la banque ». **Deux produits de coût voisin n'achètent
donc pas la même chose** — et le moins cher peut ne rien financer du tout, puisqu'il faudra
rembourser.

★ **Une facture ordinaire ne s'escompte pas.** « Les créances pouvant être escomptées sont les effets
de commerce » — lettre de change, billet à ordre. Sans effet accepté par le client, l'escompte est
hors de portée : c'est l'affacturage ou la cession Dailly, pas la banque au comptoir. Croyance très
répandue, et elle fait perdre du temps au pire moment.

⚠️ **Effet sur la relation client, dit par la source elle-même** : la fiche affacturage cite en
inconvénients son coût, la **perte partielle de la relation avec la clientèle professionnelle** et
une **dégradation possible des relations clients**. Céder son poste clients, c'est céder qui relance
son client — et sur quel ton.

⛔ **Aucune source officielle ne documente l'« affacturage confidentiel » ou « non notifié ».** Ce
fichier ne l'affirme donc pas. Si un prestataire le propose, la question à poser par écrit est :
**qui écrit à mon client, et sous quel nom ?**

⛔ **Ce fichier ne nomme aucun prestataire, aucune société d'affacturage, aucun assureur-crédit, et
ne dit pas s'il faut y recourir.** Choisir un produit financier pour quelqu'un est un **conseil en
investissement** — voir `activites-reglementees.md` du rôle `juriste`.

⚠️ **Micro-entrepreneurs** : les fiches officielles sur l'affacturage **et** sur l'escompte affichent
toutes deux l'avertissement « **La page que vous consultez ne concerne pas les micro-entrepreneurs** ».
⇒ Ne pas présenter ces outils à un micro-entrepreneur comme des mécanismes documentés pour lui : le
point doit être vérifié auprès de l'établissement avant toute démarche.

### Et du côté banque, avant de céder quoi que ce soit

| Outil | Ce qu'il couvre |
|---|---|
| **Facilité de caisse** | un besoin « ponctuel et passager » — « ne peut être accordée que pour une durée ponctuelle » |
| **Découvert** | un besoin « ponctuel mais récurrent » — convention « généralement signée pour 1 an » |
| **Crédit de campagne** | les activités cycliques ou saisonnières, « une durée de 9 mois ou plus » |

★ **Le crédit de campagne est l'outil oublié des activités saisonnières**, qui empilent des découverts
là où un seul instrument correspond au besoin. ⚠️ Et un découvert **n'est pas une ressource stable** :
il se renégocie, et il se dénonce ⇒ `credit-et-rupture.md` du même rôle pour le préavis, qui est le
sujet le plus urgent de tout ce rôle.

## ★ Le crédit inter-entreprises : le vrai financeur, et son coût caché

Le premier financeur d'une petite structure n'est ni sa banque ni un factor : c'est **le délai qu'elle
accorde à ses clients, et celui qu'elle obtient de ses fournisseurs**. C'est du crédit, il ne porte
pas d'intérêt affiché, et **son coût est réel** : il se paie en BFR à financer, en temps de relance,
en risque de perte sèche si le client tombe, et en dépendance — celui qui vous paie tard décide de
votre calendrier.

**Les délais légaux de paiement, les pénalités de retard et l'indemnité forfaitaire de recouvrement
ne sont pas repris ici** : ils vivent chez le rôle `juriste`, `contrats-commerciaux.md`. C'est là
qu'il faut aller **avant** de chercher un financement, parce qu'un délai subi hors des règles n'est
pas un problème de trésorerie, c'est un droit à faire valoir.

⚠️ **Prêter de la trésorerie à une entreprise partenaire n'est pas libre.** Le prêt
inter-entreprises est encadré par les articles **L511-6** et **R511-2-1-1 à R511-2-1-3** du code
monétaire et financier :

- « La durée du prêt inter-entreprises **ne peut pas dépasser 2 ans**. »
- « L'entreprise prêteuse a ses **comptes certifiés** par un commissaire aux comptes. »
- « L'entreprise prêteuse ne consent des prêts qu'**à titre accessoire** (elle ne doit pas en faire
  une activité habituelle). »
- Un **lien économique** est exigé entre les deux entreprises, et le contrat doit être « déclaré
  auprès du service des impôts (SIE), via le formulaire n° 2062 dans un délai d'1 mois à compter de
  sa conclusion ».

★★ **L'exigence de comptes certifiés met ce dispositif hors de portée de la quasi-totalité des
TPE.** Autrement dit : **l'avance de trésorerie entre deux petites sociétés amies n'est pas un outil
disponible**, et l'improviser expose. Pour une société, le levier légal usuel est **l'avance en
compte courant d'associé** ou l'augmentation de capital, pas le prêt entre entreprises.

## ★★ La TVA : de l'argent qui n'a jamais appartenu à l'entreprise

La TVA collectée sur les ventes est **encaissée puis reversée**. Elle transite sur le compte
bancaire, elle n'entre jamais dans le patrimoine de l'entreprise, et elle **ne figure pas dans le
résultat**. Une trésorerie qui « paraît bonne » entre deux échéances de TVA n'est souvent que de la
TVA en attente de reversement.

⇒ **Dans le plan de trésorerie, la TVA à décaisser est une ligne à part**, calée sur ses propres
échéances. **Le détail du régime, des dates de déclaration et du calcul vit chez le rôle
`comptable`, `tva.md`.**

★★ **Et le piège qui referme les deux sujets : un acompte encaissé rend la TVA immédiatement
exigible.** Code général des impôts, article 269 :

> « Toutefois, en cas de versement préalable d'un acompte, la taxe devient exigible au moment de son
> encaissement, à concurrence du montant encaissé. »

Et pour les services, la fiche officielle est catégorique : « Une facture d'acompte de service
entraîne toujours l'exigibilité de la TVA pour le fournisseur. » ⇒ **Un acompte n'est donc pas
intégralement de la trésorerie disponible** : une part est déjà due, avant même la livraison ou
l'achèvement. ⚠️ La page qui l'énonce datant du 01/01/2023, **à recouper** — mais l'article 269
lui-même est cité ci-dessus dans sa version en vigueur.

## ★ Les acomptes : le levier le moins coûteux

Demander à être payé plus tôt ne coûte **aucune commission**, ne cède **aucune créance**, ne
transfère **aucun risque** et n'informe personne. C'est le seul levier de trésorerie gratuit — et
c'est celui qu'on ose le moins utiliser.

**Ce qu'il produit juridiquement, au-delà de l'argent** :
> « Clause d'acompte et d'arrhes : une fois qu'un acompte ou des arrhes ont été versés, il n'est plus
> possible de se défaire du contrat »

★ **L'acompte n'est donc pas qu'une avance de trésorerie : c'est un verrou d'engagement.** Il filtre
aussi les clients — celui qui refuse tout acompte est souvent celui qui paiera mal. ⚠️ **Acompte et
arrhes n'ont pas le même régime de restitution** : le point relève du rôle `juriste`.

### ★★ Dans un marché public, l'avance et les acomptes sont un droit, pas une négociation

C'est la partie la plus mal connue, et la plus directement monnayable :

| | Ce que dit le code de la commande publique |
|---|---|
| **Avance obligatoire** | « L'avance est **obligatoire** pour les marchés de l'État et des collectivités territoriales lorsque les 2 conditions suivantes sont réunies : Le montant initial du marché est supérieur à **50 000 € HT**. Le délai d'exécution du marché est supérieur à **2 mois**. » (art. R2191-3) |
| **Taux minimal, titulaire PME** | « **30 %** pour les marchés publics passés par l'État » · « **10 %** pour les marchés publics passés par les établissements publics administratifs de l'État » · « **10 %** pour les marchés publics passés par les collectivités territoriales » |
| **Calcul** | marché ≤ **12 mois** : « entre **5 %** et **30 %** du montant initial du marché TTC » ; au-delà : même fourchette appliquée à « 12 fois le montant initial TTC du marché divisé par la durée en mois » (art. R2191-7) |
| **Acomptes** | « Les acomptes doivent être versés **tous les 3 mois au maximum** » (art. R2191-20 à R2191-22) |
| **Acomptes PME et artisans** | « Cette périodicité est ramenée à **1 mois** » — marchés de travaux, et sur demande en fournitures ou services |

★ **Un titulaire PME qui attend la fin du chantier pour facturer se prive d'un acompte mensuel auquel
il a droit.** Personne au guichet ne le lui rappellera.

⚠️ Deux réserves honnêtes : **l'avance se rembourse** (article R2191-11) — elle décale la trésorerie,
elle ne l'augmente pas définitivement ; et **le taux minimal exact dépend de l'acheteur**, une
condition supplémentaire liée aux dépenses de fonctionnement de la collectivité étant apparue à la
lecture sans pouvoir être confirmée mot pour mot. **Vérifier le taux sur la fiche avant de l'annoncer
à un titulaire.**

## ⏱️ Il manque de l'argent CE MOIS-CI

**Le réflexe utile n'est pas de chercher un financement, c'est de décaler une sortie** — et cela se
demande **avant** l'échéance.

- **Étalements de dettes fiscales et sociales**, **médiation du crédit**, **commission des chefs des
  services financiers**, **mandat ad hoc** : gratuits ou confidentiels, et ils cessent d'être utiles
  une fois la situation figée ⇒ **`difficultes-et-mediation.md` du même rôle.**
- **Le délai de grâce judiciaire** : « L'entreprise qui a été assignée en paiement peut demander au
  juge un délai supplémentaire de 2 ans ». ⚠️ **Il ne s'applique ni aux effets de commerce, ni aux
  dettes fiscales et sociales** — pour celles-ci, ce sont les demandes d'étalement propres à
  l'Urssaf, à l'administration fiscale ou à la CCSF qui existent.

★ **Demander tôt coûte moins que subir tard.** Une demande d'étalement formulée trois semaines avant
l'échéance est un dossier de gestion ; la même après le prélèvement rejeté est un incident, avec ses
frais, son inscription et son effet sur la banque ⇒ `moyens-de-paiement.md`. ⚠️ Et si les dettes
échues ne peuvent plus être payées du tout, ce n'est plus un sujet de trésorerie : **la cessation des
paiements a un délai légal de déclaration** et engage la responsabilité du dirigeant → rôle
`juriste`.

## Ce qui reste à écrire

- ★★ **Le coût réel de l'affacturage, ligne par ligne** (commission d'affacturage, commission de
  financement, retenue de garantie) : **aucune source officielle ne le chiffre**. Le plus utile
  serait une **grille de questions à poser par écrit** au prestataire, plutôt qu'une fourchette non
  sourcée. **C'est le manque le plus gênant de ce fichier.**
- ★ **L'assurance-crédit** : aucune fiche officielle dédiée trouvée. À reprendre côté ACPR ou
  Banque de France — mécanisme, agrément de l'assureur, effet d'une réduction unilatérale de
  couverture sur un client (le vrai risque : la couverture tombe **quand** le client se dégrade).
- ★ **Le recouvrement des impayés** : relance, mise en demeure, procédure simplifiée, injonction de
  payer — utile ici parce que c'est **le levier de trésorerie qui ne coûte rien**, mais il faut le
  cadrer avec le rôle `juriste` pour ne pas le dédoubler.
- La **retenue de garantie** et la **caution de restitution d'avance** dans les marchés, publics et
  privés.
- Les **ratios de rotation** (créances clients, dettes fournisseurs, stocks) exprimés en jours : la
  seule façon de voir un BFR se dégrader **avant** la rupture. Aucun repère chiffré officiel n'a été
  trouvé, donc rien n'est écrit ici.
- L'**avance en compte courant d'associé** comme alternative légale au prêt inter-entreprises : une
  fiche officielle existe, elle n'a pas été exploitée dans ce fichier.
- L'**optimisation des stocks** comme levier de BFR, citée par la source sans aucun repère chiffré.

## Sources

- Surveiller l'équilibre financier et détecter les signaux d'alerte —
  <https://entreprendre.service-public.gouv.fr/vosdroits/F38186>
- Trouver des solutions pour améliorer la trésorerie de l'entreprise —
  <https://entreprendre.service-public.gouv.fr/vosdroits/F38483>
- Affacturage — <https://entreprendre.service-public.gouv.fr/vosdroits/F37403>
- Escompte bancaire — <https://entreprendre.service-public.gouv.fr/vosdroits/F38443>
- Mobilisation de créance professionnelle (cession Dailly) —
  <https://entreprendre.service-public.gouv.fr/vosdroits/F38332>
- Répondre à un besoin rapide de trésorerie par le financement bancaire —
  <https://entreprendre.service-public.gouv.fr/vosdroits/F22316>
- Prêt inter-entreprises : règles à respecter —
  <https://entreprendre.service-public.gouv.fr/vosdroits/F22988>
- Demander le paiement et facturer un marché public —
  <https://entreprendre.service-public.gouv.fr/vosdroits/F23386>
- Dates d'exigibilité en matière de TVA —
  <https://entreprendre.service-public.gouv.fr/vosdroits/F31412>
- Connaître les bonnes pratiques pour éviter les difficultés —
  <https://entreprendre.service-public.gouv.fr/vosdroits/F38525>
- Mettre en place un tableau de bord de gestion —
  <https://entreprendre.service-public.gouv.fr/vosdroits/F36048>
- Projet de création d'entreprise : concevoir un business plan —
  <https://entreprendre.service-public.gouv.fr/vosdroits/F35965>
- Code général des impôts, article 269 (exigibilité de la TVA, acomptes) —
  <https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006163045>

## Rappel de cadrage

Ce fichier alimente le skill `financement`, un outil d'**aide à la décision**. Il ne remplace ni un
expert-comptable inscrit à l'Ordre, ni un avocat, ni l'administration compétente.
⛔ Il ne recommande **aucun placement, produit ou prestataire** : choisir un produit financier pour
quelqu'un est un **conseil en investissement**, activité réglementée — voir
`activites-reglementees.md` du rôle `juriste`. ⚠️ **Et sur ce sujet, l'information la plus utile
n'est pas un produit : c'est qu'un décalage d'échéance se demande AVANT l'échéance, et qu'il est
gratuit.**
