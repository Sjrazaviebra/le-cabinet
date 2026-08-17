# Contributions sur les hauts revenus : CEHR et CDHR

> **État : `PARTIEL`.** Vérifié le **2026-08-17**.
> **Couvert** : la CEHR entièrement (seuils, assiette, taux, recouvrement, mécanisme de lissage) ;
> la CDHR pour le millésime **revenus 2025** (mécanisme, seuils, décote, revenus exceptionnels,
> acompte, pénalités) ; le fait qu'elle **reste en vigueur pour les revenus 2026** et sa condition de
> fin ; l'articulation avec le barème et avec le PFU.
> **Non couvert** : les **paramètres chiffrés de la CDHR pour les revenus 2026**. La loi de finances
> pour 2026 a modifié l'assiette de l'article 224 du CGI et le détail n'a **pas** pu être lu sur la
> page Légifrance de la loi → ces entrées sont en `a_verifier: true`, `valeur: null`. Aucune doctrine
> **BOFiP** consacrée à la CDHR n'a été trouvée.
> **Âge des pages** : fiche service-public du **15/04/2026** · fiche revenu fiscal de référence du
> **01/01/2026** · **FAQ CDHR d'impots.gouv.fr du 24/12/2025 → plus de six mois, à recouper** ·
> BOFiP `BOI-IR-CHR` du **11/07/2017**, ancien mais l'article 223 sexies du CGI est **inchangé depuis
> le 01/01/2018** (version en vigueur vérifiée sur Légifrance).
> ⚠️ **C'est le sujet le plus mouvant du rôle : revérifiez chaque valeur et son millésime avant tout
> usage.** Ces contributions se rejouent à chaque loi de finances.

## ⏱️ D'abord : l'échéance

**La CDHR se paie AVANT d'être déclarée.** Un **acompte de 95 %** du montant que le contribuable
**estime lui-même** doit être versé **entre le 1er et le 15 décembre de l'année des revenus**, avant
toute déclaration de revenus.

⇒ **Pour les revenus 2026, l'acompte et sa déclaration se font entre le 1er et le 15 décembre 2026**
(fiche service-public du 15/04/2026, et article 2 de la loi de finances pour 2026 : « La contribution
mentionnée au I de l'article 224 du code général des impôts donne lieu au versement d'un acompte
entre le 1er et le 15 décembre »).

⛔ **Aucune déclaration rectificative n'est possible.** Pour la campagne des revenus 2025, la FAQ
officielle est explicite : « La validation de la déclaration et du paiement est définitive. Les
éléments déclarés ne peuvent plus être modifiés. Vous ne pouvez pas faire de déclaration
rectificative. » Seul un **versement complémentaire** restait ouvert, jusqu'au 24 décembre 2025.

## Deux contributions distinctes — ne pas les confondre

| | **CEHR** | **CDHR** |
|---|---|---|
| Nature | des **tranches** en plus de l'impôt | un **plancher** d'imposition |
| Texte | article 223 sexies du CGI | article 224 du CGI |
| Créée par | loi de finances pour 2012 | article 10 de la loi de finances pour 2025 |
| Assiette | le **revenu fiscal de référence** | le **RFR « retraité »** |
| Taux | 3 % et 4 % sur des fractions | comble l'écart jusqu'à **20 %** du revenu |
| Personnes à charge | **sans effet sur les seuils** | **1 500 €** par personne à charge, en déduction |
| Paiement | avec l'impôt sur le revenu, sur l'avis | **acompte de 95 % en décembre** |

**Verbatim de la FAQ officielle** : « Ces deux contributions sont distinctes et peuvent être, ou non,
cumulatives. » Et surtout : « **le RFR à prendre en compte pour la CDHR et la CEHR n'est pas le
même.** »

★ **Même seuil d'entrée, assiette différente.** Les deux se déclenchent à 250 000 € / 500 000 €, ce
qui fait croire à un seul dispositif. Deux calculs distincts sont à mener.

---

## 1. La CEHR — contribution exceptionnelle sur les hauts revenus

### Seuils d'assujettissement

| Situation | Seuil de revenu fiscal de référence |
|---|---|
| Célibataire, veuf, séparé, divorcé | **250 000 €** |
| Couple marié ou pacsé, imposition commune | **500 000 €** |

★ **Verbatim de la fiche : « Ces seuils d'imposition n'augmentent pas si vous avez une ou plusieurs
personnes à charge. »** Le **quotient familial ne joue aucun rôle** ici. C'est contre-intuitif pour
qui a l'habitude de raisonner par parts (⇒ `impot-revenu.md`) : sur la CEHR, une famille de quatre
enfants est traitée exactement comme une personne seule sans enfant.

### Taux par tranche

| Fraction du revenu fiscal de référence | Personne seule | Couple |
|---|---|---|
| jusqu'à **250 000 €** | 0 % | 0 % |
| de **250 000 €** à **500 000 €** | **3 %** | 0 % |
| de **500 000 €** à **1 000 000 €** | **4 %** | **3 %** |
| au-delà de **1 000 000 €** | **4 %** | **4 %** |

⇒ Comme pour le barème, **seule la fraction qui dépasse une borne est frappée** : franchir 250 000 €
d'un euro ne coûte pas 3 % de tout le revenu. La logique tranche par tranche est expliquée dans
`impot-revenu.md`.

### Comment elle se paie

**Il n'existe aucun acompte de CEHR.** Elle est déclarée, contrôlée et recouvrée « selon les mêmes
règles et sous les mêmes garanties et sanctions qu'en matière d'impôt sur le revenu », et **son
montant figure sur l'avis d'impôt sur le revenu**. Rien de spécifique à déclarer.

## ★★ L'assiette n'est PAS le revenu imposable — c'est le revenu fiscal de référence

**C'est là que tout le monde se trompe**, et l'erreur est toujours dans le même sens : on se croit
hors du champ parce qu'on a regardé son revenu imposable.

Le RFR **part du revenu net imposable, puis y RÉINTÈGRE** (fiche service-public du 01/01/2026) :

- certains **revenus exonérés** d'impôt ;
- certains **revenus soumis à un prélèvement libératoire**, par exemple des revenus de capitaux
  mobiliers ;
- certains **abattements** déduits, par exemple l'**abattement de 40 % sur les dividendes** ;
- certaines **charges déductibles du revenu global**, la fiche citant les **cotisations et primes
  d'épargne-retraite** déduites du revenu global ;
- les **plus-values immobilières taxables**.

★★ **Conséquence qui change une décision : une déduction qui fait baisser l'impôt ne fait pas
forcément baisser le RFR.** Quelqu'un qui verse massivement sur un plan d'épargne retraite en
espérant repasser sous 250 000 € peut baisser son impôt sans sortir du champ de la CEHR. ⚠️ La liste
exacte est fixée par l'article 1417, IV, 1° du CGI : **à recouper sur le texte avant d'en tirer une
décision**, la fiche ne donne que des exemples.

★ **Le RFR ne se limite pas au barème.** Des revenus imposés à un taux forfaitaire y entrent. ⇒
**choisir le PFU ne met pas à l'abri de la CEHR.**

⇒ **Où le lire** : le RFR figure sur la **1re et la 3e page de l'avis d'impôt sur le revenu**. C'est
la seule valeur à regarder pour savoir si l'on est dans le champ — pas le revenu imposable.

## ★ Le lissage de la CEHR : le cas du revenu exceptionnel

**Article 223 sexies, II du CGI** — un **système de lissage**, aussi appelé **mécanisme du
quotient**, atténue la contribution quand le revenu a fait un pic.

**Trois conditions cumulatives** (verbatim `BOI-IR-CHR`) :

1. « le contribuable doit avoir bénéficié, au titre de chacune des deux années précédant celle de
   l'imposition, d'un revenu fiscal de référence inférieur ou égal au seuil d'imposition » ;
2. « le revenu fiscal de référence de l'année d'imposition doit être supérieur ou égal à **une fois
   et demie** la moyenne des revenus fiscaux de référence des deux années précédentes » ;
3. « le contribuable doit avoir été passible de l'impôt sur le revenu au titre des deux années
   précédentes pour plus de la moitié de ses revenus ».

**Calcul** (verbatim `BOI-IR-CHR`) : « **Base = [(RFR N) – (MoyRFR N-1/N-2)] / 2 + (MoyRFR
N-1/N-2)** » puis « **Cotisation RFR N = (Barème CHR x Base) x 2** ». La fraction qui excède la
moyenne est divisée par deux, ajoutée à la moyenne, et la cotisation supplémentaire obtenue est
multipliée par deux.

⛔ **La première condition tue la plupart des demandes** : il faut avoir été **sous le seuil les deux
années précédentes**. Le lissage est fait pour le **pic isolé** — une cession, une indemnité, un
bonus exceptionnel — **pas** pour lisser la vie d'un contribuable habituellement au-dessus du seuil.

⚠️ **Et il ne s'applique pas tout seul** : « Pour en bénéficier, vous devez adresser votre demande à
votre centre des finances publiques. » ★ **Un droit qui se perd faute d'être demandé** : personne ne
le proposera au guichet, et il ne figure pas comme une case à cocher dans la déclaration.

---

## 2. La CDHR — contribution différentielle sur les hauts revenus

### Est-elle encore en vigueur ? Oui — et sa fin n'est pas une date

- Créée par l'**article 10 de la loi de finances pour 2025**, avec une portée d'abord limitée à une
  seule année : « Les I et II du présent article sont applicables à l'imposition des revenus de
  l'année 2025. »
- **Prorogée et modifiée par l'article 2 de la loi de finances pour 2026.** La fiche service-public
  du 15/04/2026 le dit : « **Elle s'applique pour l'imposition des revenus de 2025 et de 2026.** »

★★ **Sa fin est conditionnelle, pas calendaire** : « Cette contribution doit s'appliquer jusqu'à
l'imposition des revenus de l'année pour laquelle sera constaté un déficit du budget national
inférieur à 3 % du produit intérieur brut (PIB). » Confirmé par l'article 2, IV, A de la loi de
finances pour 2026.

⇒ **Personne ne peut dire aujourd'hui quel sera le dernier millésime concerné.** ⛔ Ne présentez
jamais la CDHR comme « une mesure de 2025 » ni comme « supprimée » : elle est **reconduite tant que
le déficit reste au-dessus de 3 % du PIB**.

### Le mécanisme : un plancher, pas une tranche de plus

La CDHR « assure une imposition minimale de **20 %** des plus hauts revenus ». On y est redevable si,
**cumulativement** : on est résident fiscal français, le RFR retraité du foyer dépasse **250 000 €**
(personne seule) ou **500 000 €** (imposition commune), **et** le **taux moyen d'imposition est
inférieur à 20 %**.

**La contribution est la différence positive entre deux termes** (schéma officiel de la FAQ) :

| Terme | Contenu |
|---|---|
| **A** — le plancher | **RFR retraité × 20 %**, diminué de la **décote** éventuelle |
| **B** — ce qui est déjà payé | **impôt sur le revenu recalculé + CEHR non lissée**, majorés de **1 500 €** par personne à charge et de **12 500 €** pour une imposition commune |

**CDHR = A − B**, si le résultat est positif.

★ **Le terme B retient la CEHR *non lissée*.** Le lissage éventuellement obtenu sur la CEHR n'est
donc **pas** répercuté dans le calcul de la CDHR : les deux mécanismes ne s'empilent pas comme on
l'attendrait.

★ **Les 1 500 € et 12 500 € sont en déduction, donc ils réduisent la contribution** — c'est
l'inverse exact de la CEHR, dont les seuils ignorent les personnes à charge.

### La décote d'entrée dans le dispositif

« Afin d'atténuer l'effet de seuil lié à l'entrée dans le champ de cette nouvelle contribution, un
mécanisme de décote est prévu lorsque le revenu fiscal annuel est inférieur à **330 000 €** pour une
personne seule, et à **660 000 €** pour un couple. »

**Formule officielle** : `Décote = RFR retraité × 20 % − [82,5 % × (RFR retraité − abattement)]`,
l'abattement valant **250 000 €** (personne seule) ou **500 000 €** (couple).

⇒ Les bornes sont calibrées : la décote **annule** la contribution au niveau du seuil d'entrée et
**s'éteint exactement à la borne haute**. Entre les deux, la contribution monte progressivement. Il
n'y a donc **pas de marche brutale** à 250 000 €.

⚠️ **Ces valeurs sont celles du millésime revenus 2025.** Voir plus bas.

### ★★ Pourquoi elle surprend : elle frappe quelqu'un qui a déjà payé

**Parce qu'il a payé au forfait plutôt qu'au barème.**

Le **PFU** est « constitué de l'impôt sur le revenu (**12,8 %**) » — détail dans
`revenus-financiers.md`. Un contribuable dont le revenu vient surtout de placements et de plus-values
imposés au PFU a donc un impôt sur le revenu **proche de 12,8 % de son revenu**, alors que le barème
progressif monterait beaucoup plus haut. Son **taux moyen** passe sous les 20 % du plancher — et la
CDHR **comble l'écart**.

⇒ **Le PFU n'est pas une échappatoire au-delà de ces seuils : il devient le déclencheur.** La CDHR ne
frappe pas ceux qui n'ont rien payé, elle frappe ceux dont l'imposition est **forfaitaire et donc
plate**. C'est exactement ce que le dispositif cherche.

⚠️ **Attention à la nuance** : le plancher de 20 % se mesure sur l'**impôt sur le revenu** et la
CEHR. Les **prélèvements sociaux ne figurent pas dans le terme B** : quelqu'un qui raisonne sur son
prélèvement global au PFU se croira largement au-dessus de 20 % et sera surpris. ⇒ voir
`revenus-financiers.md` pour la décomposition du PFU.

### ★ Le revenu exceptionnel : retenu pour le quart

**C'est le cas pratique le plus utile du fichier** — une cession, une indemnité.

**Verbatim FAQ** : « Les revenus exceptionnels qui, par leur nature, ne sont pas susceptibles d'être
recueillis annuellement et dont le montant dépasse la moyenne des revenus nets d'après lesquels le
contribuable a été soumis à l'impôt sur le revenu au titre des trois dernières années sont retenus
pour **le quart** de leur montant dans le calcul de l'assiette de la CDHR. »

Et le schéma officiel précise que, symétriquement, « l'IR se rapportant aux revenus exceptionnels est
retenu pour le quart de son montant » dans le terme B.

**Deux régimes selon le mode d'imposition du revenu exceptionnel** :

- **imposé au barème progressif** → « bénéficient du système du quotient ». Des rubriques
  spécifiques existent pour les **gains de cession de valeurs mobilières** ; pour les autres
  catégories, la FAQ renvoie à **votre service des impôts** ;
- **imposé à taux proportionnel** → des rubriques spécifiques existent aussi dans le parcours en
  ligne.

⚠️ **Rien n'est automatique** : il faut porter ces revenus dans les **rubriques dédiées** du parcours
en ligne. Un revenu de cession saisi comme un revenu ordinaire sera compté **en entier**.

★ **Et le déclencheur n'est pas la nature seule** : il faut aussi que le montant **dépasse la moyenne
des revenus nets des trois dernières années**. Une indemnité modeste au regard des revenus habituels
n'ouvre pas droit à ce quart.

## ⏱️ 3. Acompte, calendrier, pénalités

| | CEHR | CDHR |
|---|---|---|
| Acompte | **aucun** | **95 %** du montant estimé par le contribuable |
| Quand | — | **du 1er au 15 décembre** de l'année des revenus |
| Comment | rien à faire | en ligne, espace particulier, service « Prélèvement à la source » |
| Régularisation | avis d'impôt | à la déclaration de revenus du printemps suivant |

**Détails vérifiés sur la campagne des revenus 2025**, à titre de modèle du fonctionnement :

- l'acompte se paie **obligatoirement par prélèvement** sur un compte bancaire ; « il n'est pas
  possible de valider la déclaration sans autoriser le prélèvement » — donc **ni paiement séparé, ni
  délai de paiement** ;
- si la simulation donne **zéro**, aucune déclaration d'acompte n'est exigée ; si le montant est nul
  ou **inférieur à 5 €**, la déclaration est simplement historisée ;
- les revenus non connus à la date de la déclaration **doivent être estimés**, un versement
  complémentaire restant possible ensuite (jusqu'au 24 décembre 2025 pour cette campagne) ;
- le **simulateur officiel d'impôt sur le revenu a été adapté** pour calculer la CDHR en mode non
  authentifié (lien donné dans la FAQ citée en sources) ; il ne permet pas de payer ;
- l'acompte de CDHR **n'a aucun effet sur le taux de prélèvement à la source**.

### ⚠️ La pénalité, et son asymétrie

**Verbatim FAQ** : « Des pénalités prenant la forme d'une majoration de **20 %** sont prévues : en
cas de défaut ou de retard de paiement ; lorsque l'acompte versé s'avère inférieur de plus de
**20 %** à 95 % du montant de la contribution réellement due. »

★★ **Le risque n'est pas symétrique.** Sous-estimer de plus d'un cinquième déclenche une majoration ;
un **excédent est simplement régularisé** à la taxation. ⇒ **En cas de doute sur un revenu de fin
d'année, l'estimation prudente est l'estimation HAUTE.** La situation est appréciée après la campagne
déclarative du printemps suivant, donc plusieurs mois après le versement.

## 4. Articulation avec le barème et avec le PFU — en une phrase chacun

- **Barème progressif** : la CEHR **s'ajoute** à l'impôt calculé au barème, sur une assiette
  différente (le RFR) et sans quotient familial. La CDHR, elle, **ne s'ajoute pas** mécaniquement :
  elle ne se déclenche que si l'impôt déjà dû, barème compris, laisse le taux moyen sous 20 %. ⇒ plus
  votre revenu est imposé au barème, moins la CDHR a de chances de mordre.
- **PFU** : neutre pour l'entrée dans le champ (les revenus concernés sont dans le RFR), mais
  **déclencheur** de la CDHR, puisqu'il produit un taux moyen d'impôt sur le revenu bas. ⇒
  `revenus-financiers.md`.
- **Les trois se cumulent** : impôt sur le revenu, puis CEHR, puis CDHR pour la part qui manque au
  plancher.

## ⚠️ 5. Ce qui n'est PAS confirmé pour le millésime revenus 2026

L'article 2 de la loi de finances pour 2026 **modifie le II de l'article 224 du CGI**, c'est-à-dire la
**définition même du revenu retraité** qui sert d'assiette à la CDHR. Le détail de ces retraitements
n'a **pas** pu être lu sur la page Légifrance de la loi lors de la vérification du 2026-08-17.

⛔ **En conséquence** :

- **ne réutilisez pas** la liste des retraitements de la FAQ de décembre 2025 pour les revenus 2026 ;
- les **bornes de décote** et les **majorations forfaitaires** citées plus haut sont établies pour les
  **revenus 2025** ; elles sont en `a_verifier: true` avec `valeur: null` pour 2026 ;
- **aucune doctrine BOFiP** consacrée à la CDHR n'a été trouvée. La doctrine **opposable** manque
  donc, alors qu'elle existe pour la CEHR (`BOI-IR-CHR`). C'est une différence de solidité entre les
  deux parties de ce fichier, et elle doit être dite.

Ce qui **est** confirmé pour 2026 : le principe, le maintien du dispositif, la condition de fin, le
calendrier de l'acompte et son taux de 95 %.

## Ce qui reste à écrire — par ordre d'utilité

- ★★ **Les retraitements exacts du « RFR retraité » de la CDHR pour les revenus 2026**, à lire dans
  la version consolidée de l'article 224 du CGI sur Légifrance. **C'est le trou le plus grave du
  fichier** : sans cette liste, on ne peut pas dire à quelqu'un s'il est dans le champ.
- ★★ **La liste limitative de l'article 1417, IV, 1° du CGI** — ce qui entre exactement dans le RFR.
  Elle commande l'assiette des **deux** contributions et sert aussi aux exonérations de fiscalité
  locale (⇒ `impots-locaux-et-ifi.md`).
- ★ **Le sort d'un changement de situation en cours d'année** pour la CEHR : l'article 223 sexies, II
  prévoit des ajustements du lissage en cas de mariage, divorce, séparation ou décès. Le détail n'est
  pas dans ce fichier.
- ★ **La procédure de demande de lissage** de la CEHR : forme de la demande, délai, voie de
  réclamation si elle est refusée (⇒ `reclamation-et-controle.md`).
- Le **veuvage en cours d'année** pour la CDHR : la FAQ indique qu'il faut mettre à jour sa situation
  puis ne déclarer que les revenus postérieurs au décès — à détailler.
- Le traitement des **revenus de source étrangère** et des **crédits d'impôt conventionnels** dans les
  deux termes de la CDHR (la FAQ précise que les crédits conventionnels sont neutralisés dans l'impôt
  retenu au second terme).
- Les **rubriques exactes** du parcours en ligne pour un revenu exceptionnel.
- L'existence ou non d'une **CEHR pour les non-résidents** et l'effet des conventions fiscales.

## Sources

- Qui doit payer la contribution exceptionnelle sur les hauts revenus (mise à jour 15/04/2026) —
  <https://www.service-public.gouv.fr/particuliers/vosdroits/F31130>
- Qu'est-ce que le revenu fiscal de référence (mise à jour 01/01/2026) —
  <https://www.service-public.gouv.fr/particuliers/vosdroits/F13216>
- Impôt sur le revenu, revenus d'épargne et de placement — taux du PFU (mise à jour 15/04/2026) —
  <https://www.service-public.gouv.fr/particuliers/vosdroits/F2613>
- Vérifier son assujettissement à la CDHR, outil service-public —
  <https://www.service-public.gouv.fr/particuliers/vosdroits/R74498>
- Code général des impôts, article 223 sexies — version en vigueur depuis le 01/01/2018 —
  <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000036427364>
- Code général des impôts, section de l'article 223 sexies —
  <https://www.legifrance.gouv.fr/codes/id/LEGISCTA000025049019/>
- Code général des impôts, articles 1415 à 1417 (revenu fiscal de référence) —
  <https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006162661/>
- Article 10 de la loi de finances pour 2025, créant l'article 224 du CGI —
  <https://www.legifrance.gouv.fr/jorf/article_jo/JORFARTI000051168037>
- Loi de finances pour 2026 (article 2, prorogation et modification de la CDHR) —
  <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053508155>
- BOFiP, `BOI-IR-CHR` — contribution exceptionnelle sur les hauts revenus (11/07/2017) —
  <https://bofip.impots.gouv.fr/bofip/7804-PGP>
- Actualité CDHR, impots.gouv.fr (publiée le 01/12/2025, modifiée le 22/12/2025) —
  <https://www.impots.gouv.fr/actualite/contribution-differentielle-sur-les-hauts-revenus-cdhr>
- FAQ CDHR, impots.gouv.fr (24/12/2025), schéma de calcul officiel inclus —
  <https://www.impots.gouv.fr/sites/default/files/media/1_metier/1_particulier/EV/1_declarer/111_cdhr/faq_cdhr.pdf>

## Rappel de cadrage

Ce fichier alimente le skill `impots`, un outil d'**aide à la décision**. Il ne remplace ni un
professionnel inscrit et assuré, ni l'administration compétente, et **il ne calcule aucune
contribution**. ⚠️ Il traite la **fiscalité** d'un placement, **jamais son opportunité** :
recommander un placement adapté à une situation est un **conseil en investissement**, activité
réglementée — voir `activites-reglementees.md` du skill `juriste`. ⛔ **Et sur ce sujet précisément,
la prudence est renforcée** : la CDHR a changé entre sa création et le millésime suivant, sa fin
dépend d'une condition macroéconomique, et un acompte mal estimé se paie d'une majoration. Renvoyez
au texte en vigueur et, en cas de montant significatif, à un avocat fiscaliste ou un
expert-comptable.
