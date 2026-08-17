# Revenus financiers, crypto, dividendes

> **État : `RÉDIGÉ`** pour le PFU et sa décomposition, l'option globale pour le barème, les dividendes
> et la dispense de prélèvement à la source, les plus-values de valeurs mobilières et le report des
> moins-values, le PEA et le PEA-PME, les livrets réglementés, les actifs numériques et les obligations
> déclaratives. **`À ÉCRIRE`** : le compte à terme, les obligations et titres de créance pris un par un,
> les revenus financiers de source étrangère.
> Vérifié le **2026-08-17** — pages service-public du **15/04/2026**, **22/05/2026**, **30/06/2026**,
> **09/07/2026** et **01/08/2026** ; pages impots.gouv.fr du **08/04/2026** et du **17/07/2026**.
> ⚠️ Une seule source a plus de six mois : l'actualité sur les comptes d'actifs numériques détenus à
> l'étranger, **page du 06/05/2024, à recouper**.
>
> ⛔ **Ce fichier ne traite pas** : l'assurance-vie → `assurance-vie.md` · les actions gratuites, RSU et
> BSPCE → `actions-rsu-bspce.md` · le plan d'épargne retraite → `epargne-retraite-per.md`. La
> distinction **TMI / taux moyen**, utilisée partout ci-dessous, est posée dans `impot-revenu.md`.

## ★★ Le « PFU à 30 % » n'est plus à 30 %

C'est la première chose à corriger, et elle fausse tous les calculs faits de mémoire.

| Revenus | Impôt sur le revenu | Prélèvements sociaux | **Total** |
|---|---|---|---|
| **2025** (déclarés au printemps 2026) | **12,8 %** | **17,2 %** | **30 %** |
| **2026** (à déclarer en 2027) | **12,8 %** | **18,6 %** | **31,4 %** |

**Verbatim, service-public :** « La plus-value réalisée est soumise au prélèvement forfaitaire unique
au taux de **31,4 %** (12,8 % d'impôt sur le revenu et 18,6 % de prélèvements sociaux). »

La hausse porte **entièrement sur la CSG**, passée de **9,2 %** à **10,6 %**. Décomposition des
**18,6 %** : CSG **10,6 %** + CRDS **0,5 %** + prélèvement de solidarité **7,5 %**.

★★ **Un gain réalisé aujourd'hui relève déjà du taux à 31,4 %.** Quelqu'un qui arbitre en août 2026 en
appliquant le chiffre qu'il croit connaître sous-estime sa charge **sur toute son assiette**.

⚠️ **Et le taux n'est pas le même pour tout le patrimoine** : les revenus fonciers et les plus-values
immobilières **restent à 17,2 %** (CSG 9,2 %). ⇒ `immobilier-fiscal.md`. Ne transposez pas 18,6 % à
l'immobilier.

**Ce que le PFU couvre** : les revenus de placements financiers — dividendes et revenus distribués,
intérêts et produits de placement à revenu fixe, plus-values de cession de valeurs mobilières,
plus-values de cession d'actifs numériques.

## ★★ L'option pour le barème est GLOBALE — on ne choisit pas placement par placement

**C'est l'erreur de raisonnement la plus fréquente du sujet.** Beaucoup de gens croient pouvoir garder
le PFU sur leurs plus-values et prendre le barème sur leurs dividendes. **C'est impossible.**

**Verbatim, impots.gouv.fr** : l'option s'applique à « l'ensemble de vos revenus de capitaux mobiliers
et de vos plus-values de cession de valeurs mobilières », « en cochant la **case 2OP** de votre
déclaration ».

⇒ **Une seule case, pour tout le foyer fiscal, pour toute l'année.** L'option est donc :

- **globale** — tous les revenus mobiliers et toutes les plus-values mobilières du foyer, ensemble ;
- **expresse** — sans la case cochée, c'est le PFU qui s'applique **par défaut** ;
- **annuelle** — elle se reprend, ou non, chaque année.

★★ **Et le verrou a sauté.** Verbatim impots.gouv.fr : « à partir de 2026, **le caractère irrévocable de
cette option a été supprimé** ». Service-public le confirme pour les revenus 2026 : « vous pourrez
renoncer à votre option pour le barème progressif (**dans le délai de réclamation ou en cours de
contrôle**), si celle-ci vous est finalement défavorable ».

⇒ **Une option 2OP malheureuse n'est plus une erreur définitive** : elle se défait par réclamation.
C'est exactement le genre d'information que personne ne donne au guichet, et elle change la façon
d'aborder un doute. ⚠️ **Mais cela vaut pour les revenus 2026 et suivants** : jusqu'aux revenus 2025,
l'option était bien irrévocable. La date des revenus commande la réponse.

### À partir de quel TMI l'option devient-elle intéressante

★★ **Les prélèvements sociaux sont dus dans les deux cas, au même taux.** L'arbitrage ne porte donc que
sur la ligne **12,8 %** d'impôt sur le revenu. Tout le reste est du bruit.

Au barème, deux avantages apparaissent — et **seulement** au barème :

- un **abattement de 40 %** sur les dividendes ;
- une fraction de CSG **déductible du revenu imposable à hauteur de 6,8 %**.

D'où la base réellement imposée, et le TMI d'équilibre avec les 12,8 % du PFU :

| Revenu | Base imposable au barème | Impôt = TMI × base | TMI d'équilibre |
|---|---|---|---|
| **Dividende** | **53,2 %** du brut (abattement de **40 %**, puis **6,8** de CSG déductible) | | **≈ 24 %** |
| **Intérêts** | **93,2 %** du brut (**6,8** de CSG déductible, aucun abattement) | | **≈ 13,7 %** |

⚠️ **Ces deux taux d'équilibre sont un calcul dérivé des taux officiels, pas un chiffre publié** : ils
sont en `a_verifier: true` dans `data/parametres.json`. Ce sont les **taux** qui sont sourcés.

★★ **Mais la conclusion, elle, est nette** : aucune tranche du barème ne se situe entre **13,7 %** et
**24 %**. Le barème passe de **11 %** à **30 %** directement. Donc :

- **TMI 0 % ou 11 %** → **l'option barème gagne**, pour les dividendes comme pour les intérêts ;
- **TMI 30 % et au-delà** → **le PFU gagne**, dans les deux cas.

★ **Les plus-values n'ont ni abattement ni équivalent des 40 %** (sauf titres acquis avant le
1er janvier 2018, voir plus bas) : leur base au barème est proche du gain entier, ce qui rapproche leur
point d'équilibre du taux de **12,8 %** lui-même. **Elles tirent donc l'arbitrage vers le PFU**, et
comme l'option est globale, elles tirent avec elles les dividendes du même foyer.

⚠️ **Trois réserves qu'un calcul sur le seul TMI ignore** : opter pour le barème **augmente le revenu
imposable**, donc le **revenu fiscal de référence** — qui conditionne lui-même d'autres seuils ; l'effet
se combine au plafonnement du quotient familial et à la décote (`impot-revenu.md`) ; et un foyer proche
d'une borne de tranche peut basculer. ⇒ **Le TMI donne le sens, pas le montant.**

## Les dividendes : le prélèvement à la source n'est pas l'impôt

La banque prélève **12,8 %** au moment du versement. Verbatim impots.gouv.fr : ce prélèvement
forfaitaire non libératoire « constitue une **avance** d'impôt sur le revenu ».

★ **Ce n'est donc pas de l'argent perdu** : il s'impute sur l'impôt final et l'excédent est restitué.
Beaucoup de gens croient payer deux fois, ou croient au contraire que tout est soldé et ne déclarent
plus rien. **Les deux sont faux.**

### La dispense — et le piège des deux jeux de seuils

On peut demander à en être dispensé si le **revenu fiscal de référence de l'avant-dernière année** est
inférieur à :

| Nature du revenu | Célibataire | Couple marié ou pacsé |
|---|---|---|
| **Revenus distribués (dividendes)** | **50 000 €** | **75 000 €** |
| **Placements à revenu fixe (intérêts)** | **25 000 €** | **50 000 €** |

★ **Deux jeux de seuils, pas un.** Les seuils des intérêts sont **deux fois plus bas**. Appliquer le
seuil des dividendes à un livret imposable est une erreur courante — et elle se voit tout de suite.

⛔ **La demande se fait auprès de l'ÉTABLISSEMENT FINANCIER, pas auprès des impôts**, et verbatim :
« la demande est à adresser à l'établissement financier qui vous verse les revenus **au plus tard le
30 novembre de l'année précédant celle du paiement** ». ★ **Passé le 30 novembre, rien ne rattrape
l'année suivante.** C'est une échéance qui n'est jamais rappelée, et qui ne se répare pas — mais elle
ne coûte que de la trésorerie, puisque le prélèvement reste un acompte.

## Les plus-values de cession de valeurs mobilières

**Calcul** : prix de vente − prix d'achat. Les moins-values de même nature se déduisent des plus-values
de l'année.

★★ **Ce qui reste après cette déduction ne se perd pas — à une condition.** Verbatim service-public :
« s'il vous reste un excédent de moins-value, vous pourrez le déduire des plus-values que vous
réaliserez **au cours des 10 années suivantes** ». **Et la page précise qu'une déclaration est
nécessaire pour conserver ce droit.**

⛔ **Une moins-value non déclarée l'année où elle est subie est un droit perdu**, alors même qu'aucun
impôt n'était dû cette année-là. C'est la mécanique la plus coûteuse et la plus silencieuse du sujet :
on ne déclare pas, parce qu'on ne doit rien — et on paie dix ans plus tard. **Quand quelqu'un dit
« j'ai perdu de l'argent en bourse cette année », la première question utile est : l'avez-vous
déclaré ?**

★ **L'abattement pour durée de détention existe encore, mais très étroitement** : il suppose l'option
pour le barème **et** des titres acquis **avant le 1er janvier 2018**. Verbatim : « les prélèvements
sociaux s'appliqueront sur la **totalité** de la plus-value, abattement inclus ». ⇒ **il réduit l'impôt
sur le revenu, jamais les prélèvements sociaux.**

## Le PEA : c'est la durée qui décide, et le retrait qui punit

| | Plafond de **versements** |
|---|---|
| **PEA** | **150 000 €** |
| **PEA-PME-ETI** | **225 000 €** |
| **PEA d'un majeur rattaché au foyer de ses parents** | **20 000 €** |

★ **Le PEA-PME n'ajoute PAS son plafond au PEA.** Verbatim : « la somme totale versée sur ces deux
plans par un même titulaire ne peut pas dépasser **225 000 €** ». Un PEA rempli au plafond ne laisse au
PEA-PME que la différence. **C'est une enveloppe commune, pas un cumul** — croyance fausse très
répandue. Il est par ailleurs interdit de détenir plusieurs PEA classiques, ou plusieurs PEA-PME.

**Le régime fiscal se joue sur une seule borne :**

- **après 5 ans** — verbatim : « les gains de votre PEA sont **exonérés** d'impôt sur le revenu » ;
- **avant 5 ans** — le gain net est imposé à **12,8 %** (ou au barème sur option), **et** verbatim :
  « tout retrait (total ou partiel) avant la fin de la 5e année du PEA **entraîne la clôture du
  plan** ».

★★ **L'exonération porte sur l'IMPÔT SUR LE REVENU, pas sur les prélèvements sociaux.** « Les gains du
PEA sont soumis aux prélèvements sociaux (CSG, CRDS) », y compris après 5 ans. **« PEA = zéro impôt »
est faux**, et c'est la phrase qu'on entend le plus. ⚠️ **La fiche PEA ne donne pas le taux des
prélèvements sociaux applicables ni la date à laquelle il s'apprécie** : l'entrée est en
`a_verifier: true` dans `data/parametres.json`. ⛔ **N'annoncez pas 18,6 % sur cette base.**

★ **Trois situations permettent un retrait anticipé sans clôture** : **licenciement**, **invalidité**,
**mise à la retraite anticipée** — du titulaire **ou de son époux ou partenaire de PACS**. L'extension
au conjoint est presque toujours ignorée.

⚠️ **Le PEA ne protège pas tout ce qu'on y loge** : les revenus de **titres non cotés** qui dépassent
**10 %** de leur valeur d'acquisition sont imposés à **12,8 %**.

## Les livrets réglementés : quatre exonérés, deux qui ne le sont pas

| Produit | Plafond | Fiscalité |
|---|---|---|
| **Livret A** | **22 950 €** | exonéré d'IR **et** de prélèvements sociaux |
| **LDDS** | **12 000 €** | exonéré d'IR **et** de prélèvements sociaux |
| **LEP** | **10 000 €** | exonéré d'IR **et** de prélèvements sociaux |
| **Livret jeune** | **1 600 €** | exonéré d'IR **et** de prélèvements sociaux |
| **PEL** | **61 200 €** | ⛔ **imposé** à l'IR (plan ouvert à partir de 2018) et aux prélèvements sociaux |
| **CEL** | **15 300 €** | ⛔ **imposé** à l'IR depuis 2018 et aux prélèvements sociaux |

★★ **Le PEL n'est pas un livret défiscalisé.** C'est la croyance fausse la plus tenace de la liste : les
plans ouverts avant 2018 bénéficiaient d'une exonération temporaire, ceux ouverts depuis sont imposés
**dès le premier euro d'intérêt**. Même chose pour le CEL. ⇒ **La date d'ouverture du plan est la
question à poser, pas le type de produit.**

## Les actifs numériques (crypto)

**Régime des cessions occasionnelles — article 150 VH bis du CGI.** Verbatim impots.gouv.fr :
« prélèvement forfaitaire unique (PFU) de **31,4 %** », soit « **12,8 %** d'impôt + **18,6 %** de
prélèvements sociaux ».

★ **Un seuil de tolérance qui se mesure sur les PRIX, pas sur les gains.** Verbatim : « les opérations
portant sur des cessions d'actifs numériques dont la **somme des prix** n'excède pas **305 €** au cours
d'une année d'imposition sont exonérées ». ⚠️ Ce n'est pas un abattement sur le bénéfice : c'est le
**total vendu** sur l'année qui doit rester sous **305 €**.

★★ **L'option pour le barème est SÉPARÉE de l'option globale 2OP, et elle reste définitive.** Elle
s'exerce en cochant la **case 3CN**, ouverte depuis l'imposition des revenus 2023, et verbatim :
« cette option est **définitive** ». ⇒ **Deux options, deux cases, deux régimes de révocabilité** : le
2OP a perdu son irrévocabilité pour 2026, la 3CN ne l'a pas perdue. ⛔ **Ne raisonnez jamais sur la
crypto avec ce que vous savez du 2OP.**

★★ **Et les moins-values crypto ne se reportent pas.** Verbatim : « elle n'est pas imputable sur les
plus-values de cession d'autres biens et elle **ne se reporte pas sur les années suivantes** ». Elles
ne s'imputent que sur les plus-values de même nature **de la même année**.

⇒ **Asymétrie majeure avec les valeurs mobilières, qui se reportent 10 ans.** Une perte crypto non
compensée dans l'année est **définitivement perdue**. Quelqu'un qui transpose son réflexe boursier se
trompe complètement.

### ★ Occasionnel ou habituel : la frontière qui change de régime

Le PFU de l'article 150 VH bis ne vaut que pour les cessions réalisées « à titre **occasionnel**
directement par des personnes physiques ». Au-delà, on quitte le forfait :

| Situation | Catégorie |
|---|---|
| achat-revente « dans le cadre d'une activité commerciale » | **BIC** |
| « opérations d'achat, de vente ou d'échange » s'apparentant à une activité professionnelle sans en constituer l'activité principale | **BNC** |

⛔ **La source ne chiffre pas la frontière** — ni en nombre d'opérations, ni en volume. Elle est
appréciée au cas par cas. **Ne la tranchez jamais vous-même** : le basculement change l'assiette, le
taux, les cotisations et les obligations comptables. ⇒ Fréquence élevée, outils automatisés, effet de
levier, revenus principalement tirés de cette activité : c'est un point d'arrêt, à porter au skill
`comptable` et à un professionnel.

### ⛔ Les comptes détenus à l'étranger : l'amende est PAR COMPTE

Les comptes d'actifs numériques ouverts sur des **plateformes étrangères** doivent être déclarés
(article **1649 bis C** du CGI), sur l'imprimé **3916-bis**, joint à la déclaration de revenus.

| Manquement | Amende |
|---|---|
| compte d'actifs numériques non déclaré | **750 € par compte** |
| idem, si la valeur du compte dépasse **50 000 €** à un moment quelconque de l'année | **1 500 € par compte** |
| compte **bancaire** non déclaré | **1 500 € par compte** |
| compte **bancaire** dans un État sans convention fiscale avec la France | **10 000 € par compte** |
| rappels d'impôt résultant du défaut de déclaration | majoration de **80 %** |

★★ **« Par compte » est le mot qui coûte.** Cinq plateformes oubliées, ce sont cinq amendes. Et le
seuil de **50 000 €** s'apprécie **à un moment quelconque de l'année** : un pic en cours d'année suffit
à doubler l'amende, même si le compte est vide au 31 décembre.

⚠️ **Ne confondez pas les deux barèmes** : un compte d'actifs numériques et un compte bancaire ne
relèvent pas du même montant. ⚠️ **La page d'où vient le mode déclaratif date du 06/05/2024** — plus de
six mois : **à recouper avant de s'y fier.**

## Les obligations déclaratives

| Formulaire ou case | Ce qu'il porte |
|---|---|
| **2042** | déclaration principale — revenus de capitaux mobiliers |
| **2042-C** | déclaration complémentaire ; lignes **3AN** (plus-value) et **3BN** (moins-value) pour les actifs numériques |
| **2074** | plus-values de valeurs mobilières **calculées par le contribuable lui-même** |
| **2086** | plus ou moins-values de cessions d'actifs numériques, à joindre à la déclaration |
| **2087** | plus ou moins-values d'actifs numériques (imprimé distinct du 2086) |
| **3916-bis** | comptes d'actifs numériques détenus à l'étranger |
| **case 2OP** | option globale pour le barème (revenus mobiliers + plus-values mobilières) |
| **case 3CN** | option pour le barème, **propre aux actifs numériques** |

★ **L'imprimé fiscal unique (IFU)** est le récapitulatif que l'établissement payeur adresse chaque
année ; service-public le range parmi les « justificatifs remis par les établissements payeurs
(formulaire IFU) ». **C'est la pièce à confronter à la déclaration préremplie** — le préremplissage
vient de là, et il peut être incomplet quand plusieurs établissements sont en jeu. ⚠️ **Le numéro de
formulaire de l'IFU n'a pas été confirmé sur une page officielle** : il n'est donc pas écrit ici.

⚠️ **Les numéros de cases changent d'une année sur l'autre.** Vérifiez-les sur la notice du millésime
concerné, jamais de mémoire. ⇒ `declaration-annuelle.md` pour le calendrier et le service de
correction.

## ⛔ La ligne rouge de ce fichier

Tout ce qui précède décrit **comment un revenu est imposé**. Rien de ce qui précède ne dit **s'il faut
ouvrir, vendre ou arbitrer un placement**.

**Recommander un placement adapté à la situation d'une personne est un conseil en investissement, une
activité réglementée.** ⇒ rôle `juriste`, `activites-reglementees.md`.

⛔ **Concrètement, on ne répond pas à** : « est-ce que je devrais ouvrir un PEA ? », « faut-il que je
vende avant la fin de l'année ? », « quel produit choisir ? ». **On répond à** : « comment ce gain
serait-il imposé ? », « quelle case correspond à cette opération ? », « qu'est-ce que je perds si je ne
déclare pas ? ».

★ **La bonne reformulation est presque toujours possible.** Une question de placement contient souvent
une vraie question fiscale — et y répondre est utile, précis, et dans le cadre.

## Ce qui reste à écrire

- ★★ **La cohérence PS entre les enveloppes** : le taux et la **date d'appréciation** des prélèvements
  sociaux sur le **PEA** ne sont pas donnés par la fiche PEA. C'est le trou le plus gênant du fichier,
  parce qu'il touche l'enveloppe la plus utilisée.
- ★ **Le numéro de formulaire de l'IFU** et son contenu case par case : c'est la pièce que les gens ont
  réellement en main quand ils posent leur question.
- ★ **La différence exacte entre les imprimés 2086 et 2087** : les deux existent pour les actifs
  numériques, la source ne dit pas qui remplit lequel.
- Les **intérêts** produits par produit : compte à terme, obligations, titres de créance, comptes sur
  livret bancaires non réglementés.
- Le **PEA-PME-ETI** au fond : titres éligibles, et articulation des retraits avec le PEA classique.
- Les **conditions de revenu** d'ouverture du **LEP**, et ce qui se passe quand on les dépasse.
- Les **revenus financiers de source étrangère** : crédit d'impôt conventionnel et l'imprimé dédié aux
  revenus encaissés hors de France. ⛔ Point d'arrêt du `SKILL.md` — situation internationale.
- Le régime **professionnel** des actifs numériques (BIC/BNC) une fois la frontière franchie —
  ⚠️ articulation avec le skill `comptable`.
- Le **minage** et le **staking**, qui ne relèvent pas du régime de cession.

## Sources

- Revenus d'épargne et de placement —
  <https://www.service-public.gouv.fr/particuliers/vosdroits/F2613>
- Plus-values sur valeurs mobilières —
  <https://www.service-public.gouv.fr/particuliers/vosdroits/F21618>
- Imposition des revenus d'un PEA —
  <https://www.service-public.gouv.fr/particuliers/vosdroits/F22449>
- Plan d'épargne en actions (PEA) —
  <https://www.service-public.gouv.fr/particuliers/vosdroits/F2385>
- Comparatif des livrets et plans d'épargne —
  <https://www.service-public.gouv.fr/particuliers/vosdroits/F34393>
- Déclaration des comptes ouverts à l'étranger —
  <https://www.service-public.gouv.fr/particuliers/vosdroits/F34342>
- CSG, CRDS et prélèvements sociaux sur les revenus du patrimoine —
  <https://www.service-public.gouv.fr/particuliers/vosdroits/F2329>
- Barème de l'impôt sur le revenu —
  <https://www.service-public.gouv.fr/particuliers/vosdroits/F1419>
- Les revenus mobiliers — <https://www.impots.gouv.fr/particulier/les-revenus-mobiliers>
- Revenus de capitaux mobiliers et plus-values mobilières —
  <https://www.impots.gouv.fr/particulier/revenus-de-capitaux-mobiliers>
- Les cessions mobilières — <https://www.impots.gouv.fr/particulier/les-cessions-mobilieres>
- Déclarer les plus ou moins-values sur cessions d'actifs numériques —
  <https://www.impots.gouv.fr/particulier/questions/comment-declarer-les-plus-ou-moins-values-sur-cessions-dactifs-numeriques>
- Comptes d'actifs numériques détenus à l'étranger (page du 06/05/2024, à recouper) —
  <https://www.impots.gouv.fr/actualite/modalites-de-declaration-des-comptes-dactifs-numeriques-detenus-letranger>
- Formulaire n° 2086 —
  <https://www.impots.gouv.fr/formulaire/2086/declaration-des-plus-ou-moins-values-de-cessions-dactifs-numeriques>

## Rappel de cadrage

Ce fichier alimente le skill `impots`, un outil d'**aide à la décision**. Il ne remplace ni un
professionnel inscrit et assuré, ni l'administration compétente, et **il ne calcule aucun impôt** : les
taux servent à comprendre un sens d'arbitrage, pas à produire un montant. ⚠️ **Taux, seuils et plafonds
changent chaque année, et les prélèvements sociaux viennent précisément de changer** — vérifiez le
millésime avant de vous en servir. ⛔ **Et jamais de recommandation de placement : ce fichier dit
comment un gain est imposé, jamais s'il faut le réaliser.**
