# Actionnariat salarié : actions gratuites, RSU, BSPCE, stock-options

> **État : `PARTIEL`** — couvert : les deux moments d'imposition, les actions gratuites, les BSPCE
> (conditions et ancienneté), les stock-options, les plans étrangers (devise, retenue à la source,
> crédit d'impôt), les obligations déclaratives et leurs cases, le piège de la valeur qui a baissé,
> le traitement social salarié. **Non couvert** : la **contribution patronale** (aucune page
> officielle fetchée ne la chiffre → laissée en `a_verifier`), le taux majoré de contribution
> salariale, et la qualification fiscale d'un plan **étranger** de RSU.
> Vérifié le **2026-08-17** sur impots.gouv.fr et sur les notices officielles du millésime
> **revenus 2025** (notices 2041-NOT, 2074-NOT, 2047-NOT du **15/04/2026**, formulaire 3916 de
> **mars 2026**, fiches impots.gouv.fr des **08/04/2026** et **17/07/2026**).
> ⚠️ La fiche service-public sur les actions gratuites porte « vérifié le **01/01/2026** » : plus de
> six mois, **à recouper**. ⛔ Le **BOFiP n'a pas pu être consulté** (pages non atteignables) : là où
> seule la doctrine tranche, c'est écrit.

## ★★ L'ossature : deux impositions, deux régimes, deux dates

C'est la confusion qui coûte le plus cher sur ce sujet. **Il n'y a pas un impôt, il y en a deux**, et
ils ne sont ni de la même nature, ni dus la même année.

| | **1. Le gain d'acquisition** | **2. La plus-value de cession** |
|---|---|---|
| **Quand** | à l'**acquisition définitive** des titres (fin de la période d'acquisition), ou à la **levée** de l'option | à la **vente** des titres |
| **Ce qui est imposé** | la valeur du titre au jour où il vous est définitivement acquis | valeur de vente **moins** valeur retenue à l'acquisition |
| **Nature** | un **revenu du travail** — c'est une rémunération, pas un placement | une **plus-value mobilière** |
| **Régime** | propre à chaque dispositif → voir ci-dessous | régime commun → `revenus-financiers.md` |
| **Déclenché par** | le **temps qui passe**, pas par une décision | **votre** décision de vendre |

★★ **Le premier étage se déclenche tout seul.** On ne choisit pas de subir le gain d'acquisition : il
naît à l'échéance du calendrier du plan, **même si on ne vend rien et qu'aucun euro n'entre sur le
compte**. C'est toute la différence avec la plus-value, et c'est la racine du piège traité plus bas.

⚠️ **Ne jamais raisonner « j'ai gagné X en tout ».** Les deux étages ont des assiettes, des taux, des
prélèvements sociaux et des cases **différents**. Un calcul global est nécessairement faux.

★ **La date qui commande le régime n'est pas celle que l'on croit** : pour les actions gratuites,
c'est la **date de la décision de l'assemblée générale** qui a autorisé l'attribution ; pour les
BSPCE et les options, la **date d'attribution**. Pas la date d'acquisition, pas la date de vente.
Quelqu'un qui vend en 2026 des actions issues d'un plan voté en 2016 relève du régime de 2016.

## ★★ Le basculement du 1er janvier 2026 : 17,2 % → 18,6 %

Deux pages officielles semblent se contredire sur les prélèvements sociaux. **Elles ne se
contredisent pas : c'est un calendrier.** La page « Les revenus mobiliers » du **08/04/2026** le dit :

> « À compter du 1er janvier 2026, le taux des prélèvements sociaux passent à 18,6 % sauf pour les
> produits suivants qui restent soumis au taux de 17,2 % »

La liste d'exception ne contient que des **produits d'épargne** (assurance-vie, certains CEL et PEL
anciens, PEP). **Les gains d'actionnariat salarié n'y sont pas.** D'où :

| Étage social | Taux | Composition |
|---|---|---|
| Prélèvements sociaux du **patrimoine**, jusqu'aux revenus **2025** | **17,2 %** | CSG **9,2 %** + CRDS **0,5 %** + prélèvement de solidarité **7,5 %** |
| Prélèvements sociaux du **patrimoine**, à compter du **1er janvier 2026** | **18,6 %** | CSG portée à **10,6 %**, CRDS et solidarité inchangées |
| CSG-CRDS sur les revenus d'**activité** | **9,7 %** | CSG **9,2 %** + CRDS **0,5 %** |

La notice 2041-NOT (revenus 2025) confirme la mécanique : les prélèvements sociaux « au taux de
17,2 % ou 18,6 % » sont composés de la CSG « au taux de 9,2 % ou de 10,6 % », de la CRDS et du
prélèvement de solidarité. **Le relèvement porte sur la CSG.**

★ **Conséquence concrète** : une acquisition définitive tombant en **2026** supporte les prélèvements
sociaux à **18,6 %** là où la même, en **2025**, les supportait à **17,2 %**. Sur les montants en jeu
dans ces plans, l'écart n'est pas anecdotique — et **il n'est dans aucune simulation faite en 2025**.

## Les attributions gratuites d'actions et les RSU

**Le cadre légal** (fiche service-public, page du 01/01/2026, à recouper) : la période d'acquisition
est fixée par l'assemblée générale mais ne peut être inférieure à **1 an**, et « le cumul de la
période d'acquisition et de la période de conservation ne peut pas être inférieur à **2 ans** ».

### Le gain d'acquisition : tout bascule à 300 000 €

Pour les attributions décidées à compter du **1er janvier 2018** :

| Fraction du gain | Impôt sur le revenu | Prélèvements sociaux | Contribution salariale |
|---|---|---|---|
| **jusqu'à 300 000 €** | barème progressif **après abattement de 50 %** | **17,2 %** (revenus 2025) / **18,6 %** (à compter de 2026), **sur le gain AVANT abattement** | — |
| **au-delà de 300 000 €** | barème progressif, **sans abattement**, en traitements et salaires | **9,7 %** (CSG-CRDS d'activité) | **10 %** |

★★ **Le contre-intuitif qui trompe tout le monde : au-delà du seuil, le taux social BAISSE.** On passe
de 17,2-18,6 % à 9,7 %. Ce n'est pas un cadeau : l'abattement de **50 %** disparaît **et** une
contribution salariale de **10 %** s'ajoute. Regarder le seul taux de prélèvements sociaux pour
juger de la marche fiscale au franchissement du seuil conduit à une conclusion inversée.

★ **L'abattement s'applique à l'impôt, pas aux prélèvements sociaux.** La notice est explicite : le
gain « avant abattement » est soumis aux prélèvements sociaux. L'assiette sociale est donc **le
double** de l'assiette fiscale sous le seuil.

⚠️ **Réserve sur la nature de l'abattement.** La fiche impots.gouv.fr du 17/07/2026 écrit
« abattement pour durée de détention de 50 % », tandis que la notice 2041-NOT renvoie, pour les
mêmes cases **1TZ à 1VZ**, aux « abattements applicables aux plus-values de cession de valeurs
mobilières », applicables « sous certaines conditions ». Ces deux formulations ne décrivent pas la
même mécanique. **L'abattement réellement applicable dépend de la date de décision de l'AGE** :
ne chiffrez pas sans avoir vérifié le régime du millésime concerné à la source.

**Un dirigeant de PME partant à la retraite** peut, sous conditions, substituer un abattement fixe de
**500 000 €** (article 150-0 D ter du CGI) à l'abattement proportionnel.

**Plans antérieurs** — pour les actions gratuites **et** les options **attribuées avant le
28 septembre 2012**, la notice 2041-NOT indique une taxation « à **18 %**, **30 %** ou **41 %** »
(cases 3VD à 3VF) selon le montant du gain, la date d'attribution et le délai de conservation, avec
option pour l'imposition en salaires (cases 3VJ ou 3VK). ★ **Un vieux plan ne suit pas le régime
actuel** : la première question à poser est toujours la date, jamais le montant.

### ⚠️ « RSU » n'est pas une catégorie fiscale française

Les pages officielles décrivent l'**attribution gratuite d'actions** encadrée par le droit français
(décision d'AGE, périodes minimales, sociétés par actions). Un plan de *restricted stock units* d'un
employeur étranger **n'entre dans ce régime que s'il en remplit les conditions**. À défaut, le gain
est un salaire ordinaire — sans abattement, sans seuil, dans le champ des cotisations. **Aucune page
fetchée le 2026-08-17 ne traite explicitement de cette qualification** : c'est le point à faire
trancher en premier par un professionnel, parce qu'il change tout le reste du calcul.

## Les BSPCE

### Les conditions que la société doit remplir

D'après la page « L'actionnariat salarié » du 08/04/2026, la société émettrice doit être :

- **non cotée**, ou cotée sur un marché réglementé ou organisé de l'Espace économique européen avec
  une **capitalisation boursière inférieure à 150 millions d'euros** ;
- **immatriculée depuis moins de 15 ans** ;
- détenue à **25 %** de son capital, « de manière continue », par des personnes physiques ou par des
  personnes morales elles-mêmes détenues à **75 %** au moins par des personnes physiques.

★ **La condition des 15 ans ferme la porte, définitivement.** Passé ce cap, l'entreprise ne peut plus
émettre de BSPCE — d'où leur concentration sur les jeunes sociétés. ⚠️ Et « de manière continue »
n'est pas décoratif : un tour de table qui casse la structure de détention met en cause le régime des
bons **déjà attribués**.

### ★ L'ancienneté qui change le taux : trois ans

C'est la particularité des BSPCE, et le seul cas où **votre ancienneté dans la société** commande
directement votre taux d'imposition.

| Millésime des bons | Ancienneté **≥ trois ans** | Ancienneté **< trois ans** |
|---|---|---|
| attribués **avant le 1er janvier 2018** | **19 %** (case 3SJ) | **30 %** (case 3SK) |
| attribués du **1er janvier 2018 au 31 décembre 2024** | **12,8 %** (case 3TJ) ou barème sur option (case 2OP) | **30 %** (case 3SK) |
| attribués **à compter du 1er janvier 2025** — gain de cession | **12,8 %** (case 3TL) ou barème sur option | **12,8 %**, quelle que soit l'ancienneté |
| attribués **à compter du 1er janvier 2025** — avantage salarial d'exercice | **12,8 %** (ligne 3PC), ou option pour les traitements et salaires (ligne 1AY ou 1BY) | **30 %** (ligne 3PE) |

Prélèvements sociaux : ceux du patrimoine (**17,2 %** / **18,6 %**). Abattement fixe de **500 000 €**
de l'article 150-0 D ter possible sous conditions (case 3TK, ou 3TM depuis 2025).

★★ **La réforme applicable aux bons attribués à compter du 1er janvier 2025 dédouble l'imposition.**
Avant, un seul gain à la cession. Depuis, il y a un **avantage salarial** taxé au titre de la
**souscription** (l'exercice du bon), puis un **gain de cession** taxé à la vente. Le premier étage
existe donc désormais **même sans vente** — les BSPCE rejoignent la logique des actions gratuites, et
avec elle le piège décrit plus bas.

★ **La notice précise ce que « ancienneté » veut dire** : si vous n'êtes **plus** salarié, ce qui
compte est d'avoir exercé son activité dans la société pendant au moins trois ans. Et pour l'avantage
salarial des bons attribués depuis 2025, l'ancienneté s'apprécie dans la société émettrice **ou dans
une de ses filiales**.

⛔ **Franchir ou non le troisième anniversaire avant d'exercer est une décision d'investissement et de
carrière**, pas une question fiscale. Ce fichier donne l'écart de taux ; il ne dit pas s'il faut
exercer, attendre ou vendre. Voir le rôle `juriste`, `activites-reglementees.md`.

## Les stock-options

Trois étages, pas deux — et le premier est presque toujours oublié.

1. **Le rabais.** « Un rabais de **20 %** au plus peut être décidé par la société » sur le prix de
   souscription. L'exonération d'impôt ne couvre que « la fraction du rabais qui ne dépasse pas
   **5 %** de la valeur des actions » ; le surplus, le **rabais excédentaire**, « est taxée l'année
   de la levée d'option comme un salaire ».
   ★ **C'est un impôt dû l'année de la levée, sur un avantage consenti des années plus tôt.**
2. **Le gain de levée.** Pour les options attribuées **à compter du 28 septembre 2012** : « Le gain
   de levée d'option est intégré au barème progressif de l'impôt sur le revenu, dans la catégorie des
   traitements et salaires. » CSG **9,2 %** et CRDS **0,5 %** au titre des revenus d'activité, plus
   une **contribution salariale de 10 %** pour les options attribuées depuis le 16 octobre 2007.
3. **La plus-value de cession** → régime commun, `revenus-financiers.md`.

**L'état individuel** que la société remet : vous êtes « dispensé de joindre à votre déclaration »
cet état, mais « vous devez le conserver et le présenter à l'administration sur demande de sa part ».
★ **Le conserver n'est pas une formalité** : c'est la seule pièce qui établit la décomposition entre
rabais, gain de levée et plus-value. Sans elle, un contrôle se règle sur la position de
l'administration. À archiver **avec** les relevés du plan, sans limite de durée utile.

★ **Nouveauté à connaître** : à compter du **15 février 2025**, le gain réalisé sur les instruments
d'intéressement des « **management packages** » relève du régime des plus-values mobilières, « avec
une limite tenant compte de la performance financière de la société » ; la fraction qui dépasse cette
limite retombe dans les traitements et salaires, avec la contribution salariale de **10 %**.

## Les plans étrangers

### La conversion de devise

La notice 2047-NOT est nette : les revenus encaissés en monnaie étrangère se déclarent

> « pour leur contre-valeur en euros, calculée d'après le cours du change à Paris au jour de
> l'encaissement (réception en espèces, inscription au crédit d'un compte...) »

★★ **Ce n'est pas un cours moyen annuel, et ce n'est pas le cours du jour de la vente.** Pour un gain
d'acquisition, la date de référence est celle de **l'acquisition définitive** ; pour la plus-value,
celle de la **cession**. Deux gains, deux dates, **deux cours de change**. Un relevé de broker
américain converti d'un bloc au taux du 31 décembre produit un montant faux dans les deux cases.

### La retenue à la source et le crédit d'impôt

**L'impôt étranger ne se déduit pas du revenu.** La notice 2047-NOT le dit sans ambiguïté : « le
revenu imposable en France est égal au revenu de source étrangère sans déduction de l'impôt
étranger ». Il faut donc déclarer le **brut**, puis réclamer un **crédit d'impôt**, qui est

> « égal à l'impôt effectivement supporté à l'étranger, dans la limite des taux prévus par les
> conventions, sans pouvoir excéder l'impôt français afférent à ce revenu »

⚠️ **Double plafond, et un trou entre les deux.** Si l'État source a retenu **plus** que le taux
conventionnel, l'excédent n'est **pas** récupérable en France. La notice indique la seule voie :
« l'usager pourra se rapprocher du pays en question, afin de se faire restituer la différence, selon
la procédure mise en place par cet État. » ★★ **C'est un droit qui se perd faute de le connaître** :
la démarche est étrangère, ses délais sont étrangers, et rien dans la déclaration française ne
signale qu'il y a de l'argent à récupérer ailleurs.

⚠️ Et si le crédit d'impôt excède l'impôt français afférent au revenu, **l'excédent est perdu** : il
ne se rembourse pas, ne se reporte pas.

## Les obligations déclaratives

| À déclarer | Formulaire | Cases |
|---|---|---|
| Gain d'acquisition, fraction sous le seuil de 300 000 € | 2042 C | **1TZ à 1VZ** |
| Gain d'acquisition, fraction au-delà du seuil | 2042 C | **1TT** et **1UT** |
| Gains de levée / d'acquisition attribués avant le 28 septembre 2012 | 2042 C | **3VD à 3VF** ; option salaires **3VJ**/**3VK** ; contribution salariale **3VN** |
| Gains de cession de BSPCE | 2042 C | **3SJ**, **3SK**, **3TJ**, **3TL** ; abattement fixe **3TK**/**3TM** |
| Avantage salarial d'exercice de BSPCE (bons depuis 2025) | 2042 C | **3PC** ou **3PE** ; option salaires **1AY**/**1BY** |
| Option globale pour le barème progressif | 2042 | **2OP** |
| Plus ou moins-values de cession | 2074, report en 2042 C | moins-value reportable en **3VH** |
| Revenus de source étrangère et crédit d'impôt | 2047, report en 2042 C | **8VL** (gains d'actionnariat salarié), assiette en **8PL** |
| Comptes détenus à l'étranger | 3916 - 3916 bis | cocher **8UU** |

⚠️ **Les codes de cases changent d'un millésime à l'autre.** Ceux ci-dessus sont relevés sur les
notices **revenus 2025**. Vérifiez sur la notice du millésime concerné avant de les citer.

★★ **Rien n'est prélevé à la source sur ces gains.** La notice 2047-NOT classe les plus-values et
gains d'actionnariat salarié parmi les « revenus hors du champ du prélèvement à la source ». Il n'y a
donc **aucun acompte** : l'impôt tombe en **solde**, l'année suivante. Quelqu'un dont les actions
sont définitivement acquises en septembre paie l'impôt correspondant près d'un an plus tard, sur un
revenu dont il n'a peut-être jamais vu la couleur. ★ **Corollaire pratique : provisionner
immédiatement**, et se souvenir que ce revenu peut aussi faire monter le **taux** de prélèvement à la
source appliqué au salaire l'année suivante → `impot-revenu.md` pour la distinction entre TMI et taux
moyen, et `declaration-annuelle.md` pour le calendrier.

### ⚠️ Le compte de titres à l'étranger : l'oubli le plus fréquent

Un plan d'employeur étranger loge presque toujours les titres chez un **teneur de compte étranger**.
Le formulaire 3916 vise « tout compte ouvert, détenu, clôturé ou utilisé à l'étranger, pendant tout
ou partie de l'année », **y compris sur simple procuration**, et la notice 2041-NOT prévient : « Vous
devez déclarer vos comptes bancaires et contrats d'assurance-vie à l'étranger **sous peine
d'amendes**. » **L'amende est due par compte non déclaré et par année.**

⛔ **Ne pas déduire de l'absence de gain qu'il n'y a rien à déclarer.** L'obligation porte sur
l'**existence** du compte, pas sur le fait d'y avoir gagné quelque chose. Un compte ouvert, jamais
alimenté puis fermé, est déclarable.

⚠️ **Piège de formulaire, constaté sur le 3916 de mars 2026** : la rubrique « nature du compte » ne
propose que trois cases — *compte bancaire*, *compte d'actifs numériques*, *contrat de capitalisation
ou placement de même nature*. **Il n'y a pas de case « compte de titres ».** Beaucoup en concluent,
à tort, que leur compte-titres étranger n'est pas visé. Le formulaire est pris sur le fondement de
l'article 1649 A du CGI, qui ne parle pas de comptes « bancaires » au sens courant.
⇒ **Montants des amendes, régularisation et détail de l'obligation : rôle `comptable`, fichier
`cas-plateformes-etrangeres.md`.** Ce fichier n'en duplique pas les chiffres.

## ★★ Le piège central : imposé sur un gain que l'on n'a plus

**Le mécanisme.** Le gain d'acquisition est figé à la valeur du titre **au jour de l'acquisition
définitive**. Cette valeur devient définitivement la base imposable. Ensuite, le titre vit sa vie —
et rien, dans le calcul du premier étage, ne redescend si le cours redescend.

Le scénario, banal :

1. les actions sont définitivement acquises ; le gain d'acquisition est né, taxable ;
2. le titre chute — marché, valorisation revue, société non cotée qui se refinance plus bas ;
3. le salarié vend, ou ne vend pas ;
4. **l'impôt et les prélèvements sociaux du premier étage restent dus sur la valeur d'origine**, et
   ils tombent en solde l'année suivante, sans qu'aucun prélèvement à la source ne les ait anticipés.

**Ce que le droit prévoit — et ce qu'il ne prévoit pas.** La notice 2074-NOT (revenus 2025) énumère
**limitativement** les cas où une moins-value peut s'imputer sur un gain d'actionnariat salarié :

> « Si vous avez également réalisé en 2025 un gain de levée d'option (uniquement pour les options
> attribuées avant le 20.06.2007) ou un gain lors de la cession de titres souscrits en exercice de
> bons de souscription de parts de créateur d'entreprise, vos moins-values sont imputables sur ces
> gains. Par conséquent, ne reportez à la case 3VH que le reliquat de moins-values qui n'a pas pu
> s'imputer sur ces gains. »

⇒ **Deux portes de sortie, et deux seulement** : les gains de levée d'options **attribuées avant le
20 juin 2007**, et les gains de cession de titres issus de **BSPCE**. ★★ **Le gain d'acquisition
d'actions gratuites n'est pas dans la liste.** Pour lui, la moins-value de cession reste une
moins-value mobilière ordinaire : imputable sur les **plus-values de même nature** de l'année, puis
reportable sur celles des **dix** années suivantes — et **sur rien d'autre**.

★★ **La conséquence est brutale et rarement dite** : sans autre cession gagnante, la moins-value ne
compense **jamais** l'impôt déjà payé sur le gain d'acquisition. Elle attend une plus-value qui peut
ne jamais venir. Le salarié qui n'a que ce plan-là dans son patrimoine a un impôt réellement payé et
une moins-value théoriquement reportable — les deux ne se rencontrent pas.

⚠️ **Réserve à énoncer telle quelle.** La notice est un document déclaratif, pas la doctrine. **Le
BOFiP n'a pas pu être consulté le 2026-08-17.** Avant de dire à quelqu'un qu'il n'a aucun recours :
vérifier la doctrine applicable à son millésime, et faire examiner la piste d'une **réclamation** si
la valeur retenue à l'acquisition est elle-même contestable (titre non coté, valorisation d'expert)
→ `reclamation-et-controle.md`. **Un « non » mal vérifié ferme un recours ; c'est exactement ce qu'un
outil d'aide à la décision ne doit pas faire.**

⛔ **Et ce qui ne relève pas de ce fichier** : vendre une partie des titres dès l'acquisition pour
couvrir l'impôt, conserver, ou couvrir la position sont des **décisions d'investissement**. Les
énoncer comme recommandation serait un conseil en investissement, activité réglementée → rôle
`juriste`, `activites-reglementees.md`.

## Le traitement social : ce qui passe où

| | Assiette | Ce qui s'applique |
|---|---|---|
| Gain d'acquisition, fraction ≤ **300 000 €** | gain **avant** abattement | prélèvements sociaux du **patrimoine** : **17,2 %** puis **18,6 %** |
| Gain d'acquisition, fraction > **300 000 €** | gain intégral | CSG-CRDS d'**activité** **9,7 %** + contribution salariale **10 %** |
| Gain de levée d'options (attribuées depuis le 28 septembre 2012) | gain de levée | CSG **9,2 %** + CRDS **0,5 %** + contribution salariale **10 %** |
| Gains BSPCE | gain | prélèvements sociaux du **patrimoine** |
| Plus-value de cession | plus-value | prélèvements sociaux du **patrimoine** |

★ **Ces gains ne passent pas par les cotisations sociales de droit commun** — ils sont soumis à des
**prélèvements sociaux** et, pour certains, à une **contribution salariale** spécifique. La
contrepartie est directe et souvent ignorée : **ils n'ouvrent aucun droit**. Pas de trimestre de
retraite, pas de base pour les indemnités journalières, pas d'assiette chômage. Un bonus de même
montant, lui, en ouvre. ★★ **À montant net égal, un gain d'actionnariat vaut moins qu'un salaire du
point de vue des droits sociaux** — c'est une information qui manque dans toutes les présentations de
plans, et elle change la lecture d'une négociation salariale.

⚠️ **Un taux dont l'assiette n'a pas pu être identifiée** : la notice 2041-NOT indique que « certains
gains sont soumis à une contribution salariale au taux de **10 %** ou **30 %** ». **Aucune page
officielle fetchée le 2026-08-17 ne dit à quels gains s'applique le taux de 30 %.** Il n'est donc pas
annoncé ici comme applicable à tel dispositif : trou assumé, à combler au BOFiP.

⛔ **La contribution patronale n'est pas chiffrée dans ce fichier.** Elle existe, elle relève du code
de la sécurité sociale et de l'URSSAF, **et aucune source admise fetchée le 2026-08-17 n'en donne le
taux, l'assiette ni l'exonération éventuelle pour les PME.** Elle est laissée en `a_verifier` dans
les paramètres. Deux choses peuvent être dites sans risque : c'est un coût **employeur**, il ne réduit
pas le net du bénéficiaire ; et c'est souvent lui qui explique qu'un plan soit plafonné ou réservé.
**Ne pas la chiffrer de mémoire.**

## Ce qui reste à écrire

Par ordre d'utilité :

1. ★★ **La contribution patronale** : taux, assiette, base de calcul, et l'exonération applicable
   aux jeunes entreprises. C'est le trou le plus visible du fichier, et la question revient dès qu'un
   dirigeant conçoit un plan. Source à ouvrir : `urssaf.fr` et le code de la sécurité sociale.
2. ★★ **La confirmation BOFiP du sort de la moins-value** quand le titre a baissé — le point le plus
   lourd de conséquences de tout le fichier, aujourd'hui appuyé sur la seule notice 2074-NOT.
3. ★ **La qualification d'un plan étranger de RSU** au regard du régime français des attributions
   gratuites : conditions à remplir, et régime applicable à défaut.
4. ★ **L'assiette du taux de contribution salariale de 30 %.**
5. Le régime des **management packages** (à compter du 15 février 2025) : la « limite tenant compte
   de la performance financière », comment elle se calcule, et ce qui bascule au-delà.
6. Le sort des titres en cas de **départ de l'entreprise**, de **décès**, de **donation**, et
   l'articulation avec le **PEA** ou l'apport à une holding.
7. Le **transfert du domicile fiscal hors de France** avec des gains non encore imposés
   (déclarations 2074-ETD et 2074-ETS, mentionnées par la notice) et la répartition du gain entre
   États en cas de mobilité pendant la période d'acquisition.
8. L'**IFI** et les titres issus de ces plans → `impots-locaux-et-ifi.md`.

## Sources

Pages et documents **réellement fetchés** le 2026-08-17 :

- Attribution d'actions gratuites (page du 01/01/2026, à recouper) —
  <https://www.service-public.gouv.fr/particuliers/vosdroits/F2911>
- L'actionnariat salarié (08/04/2026) — <https://www.impots.gouv.fr/particulier/lactionnariat-salarie>
- Gain d'acquisition d'actions gratuites (17/07/2026) —
  <https://www.impots.gouv.fr/particulier/questions/mon-entreprise-ma-attribue-des-actions-gratuites-comment-sera-impose-le-gain>
- Imposition des gains de BSPCE (17/07/2026) —
  <https://www.impots.gouv.fr/particulier/questions/jai-vendu-des-bons-de-souscription-de-parts-de-createurs-dentreprise-ou-bspce>
- Gain de levée de stock-options (17/07/2026) —
  <https://www.impots.gouv.fr/particulier/questions/jai-des-stock-options-comment-est-impose-le-gain-levee-doptions>
- Les revenus mobiliers, taux des prélèvements sociaux (08/04/2026) —
  <https://www.impots.gouv.fr/particulier/les-revenus-mobiliers>
- Notice 2041-NOT, déclaration des revenus 2025 (15/04/2026) —
  <https://www.impots.gouv.fr/sites/default/files/formulaires/2042/2026/2042_5477.pdf>
- Notice 2074-NOT, plus et moins-values, revenus 2025 (15/04/2026) —
  <https://www.impots.gouv.fr/sites/default/files/formulaires/2074/2026/2074_5500.pdf>
- Notice 2047-NOT, revenus encaissés à l'étranger, revenus 2025 (15/04/2026) —
  <https://www.impots.gouv.fr/sites/default/files/formulaires/2047/2026/2047_5490.pdf>
- Formulaire 3916 - 3916 bis, comptes à l'étranger (mars 2026) —
  <https://www.impots.gouv.fr/sites/default/files/formulaires/3916/2026/3916_5454.pdf>
- Fiche du formulaire 3916 (23/03/2026) —
  <https://www.impots.gouv.fr/formulaire/3916/declaration-par-un-resident-dun-compte-letranger-ou-dun-contrat-de-capitalisation-o>

⛔ **Non consulté** : le **BOFiP**, dont les pages n'ont pas pu être atteintes le 2026-08-17. Les
points qui en dépendent sont signalés comme tels dans le corps du fichier.

## Rappel de cadrage

Ce fichier alimente le skill `impots`, un outil d'**aide à la décision**. Il ne remplace ni un
expert-comptable inscrit à l'Ordre, ni un avocat fiscaliste, ni l'administration compétente, et
n'engage aucune responsabilité sur un calcul ou une déclaration.

⚠️ **Il traite la fiscalité de ces gains, jamais l'opportunité d'exercer, de conserver ou de céder.**
Recommander une opération adaptée à la situation d'une personne est un **conseil en investissement**,
activité réglementée → rôle `juriste`, `activites-reglementees.md`.

★ **Sur ce sujet, la première utilité n'est pas le taux.** C'est de dire qu'il y a **deux**
impositions et non une, que la première se déclenche **sans vente et sans prélèvement à la source**,
et qu'un **compte de titres étranger se déclare même sans gain**. Le reste vient après.
