# Épargne retraite : PER et déductibilité

> **État : `RÉDIGÉ`** pour les compartiments, le plafond de déduction et ses deux leviers (report,
> mutualisation), la fiscalité de sortie en capital et en rente, les cas de déblocage anticipé, le sort
> des versements non déduits, le raisonnement d'arbitrage et les cases de la déclaration.
> Vérifié le **2026-08-17** — CGI article 163 quatervicies sur Légifrance (**version en vigueur au
> 21/02/2026**, loi 2026-103 du 19 février 2026), pages service-public du **18/06/2026**, du
> **30/06/2026** et du **15/04/2026**, page impots.gouv.fr du **07/04/2026**, notice **2041-GX millésime
> 2026**.
> ⚠️ **Une réserve assumée** : la limite d'âge de 70 ans à la déductibilité est affirmée par
> service-public mais **introuvable dans le texte du CGI** — voir plus bas, l'entrée est en
> `a_verifier: true`.

## ★★ D'abord, le piège central : un PER ne fait pas gagner d'impôt, il le DÉCALE

C'est la phrase à dire avant toute autre, parce que **presque toute la communication sur le PER
s'arrête à la déduction**, c'est-à-dire à la moitié de l'opération.

- **À l'entrée**, le versement déduit fait économiser `versement × TMI de l'année du versement`.
- **À la sortie**, ce même versement **revient dans le revenu imposable** et est taxé au taux
  marginal de l'année de sortie.

⇒ **L'intérêt fiscal n'est pas la déduction : c'est l'ÉCART entre les deux taux marginaux.** À taux
marginal égal, l'opération est fiscalement neutre sur les versements — et même **légèrement
défavorable en cas de sortie en capital**, parce que l'abattement de 10 % des pensions ne s'y applique
pas (voir le tableau de sortie).

★★ **Et le taux marginal de sortie n'est pas celui qu'on a aujourd'hui à la retraite : c'est celui que
le retrait lui-même fabrique.** Un capital sorti en une fois s'ajoute aux pensions de l'année et peut
faire franchir une ou deux bornes du barème. Raisonner « je serai dans une tranche plus basse à la
retraite » sans tenir compte de cet effet est l'erreur la plus fréquente du sujet.

⇒ La distinction **TMI / taux moyen** et l'usage du TMI pour arbitrer une décision marginale sont
posés dans `impot-revenu.md` : **c'est la clé de lecture de tout ce fichier.**

⛔ **Ce fichier ne dit pas s'il faut ouvrir un PER, ni combien y verser.** Recommander un placement
adapté à une situation est un **conseil en investissement**, activité réglementée — voir
`activites-reglementees.md` du rôle `juriste`. Ce qui suit sert à **poser le calcul**, pas à trancher.

## Les trois formes, les trois compartiments

| Forme | Qui l'alimente | Ce qui la distingue fiscalement |
|---|---|---|
| **PER individuel (PERIN)** | le titulaire seul | versements volontaires, déductibles **par principe** et non déductibles **sur option** |
| **PER d'entreprise collectif (PERECO)** | salarié + employeur | accueille l'**épargne salariale** (intéressement, participation, abondement), **exonérée d'impôt sur le revenu** à l'entrée |
| **PER d'entreprise obligatoire (PERO)** | versements obligatoires employeur et/ou salarié | ⛔ **sortie en rente imposée** sur ce compartiment |

Tout PER, quelle que soit sa forme, est découpé en trois compartiments selon l'**origine** des fonds :
versements volontaires · épargne salariale · versements obligatoires.

★ **Le compartiment, et non le contrat, commande la fiscalité de sortie.** Un même PER peut donc sortir
en trois régimes différents. La première question utile n'est jamais « quel PER avez-vous ? » mais
**« d'où vient l'argent ? »**

⚠️ **Le compartiment des versements obligatoires est le plus contraint** : *« L'épargne issue des
versements obligatoires dans un PER d'entreprise est versée uniquement sous forme de rente. »* Seule
échappatoire : *« si le montant mensuel de la rente ne dépasse pas 110 €, la rente peut être convertie
en capital »*.

★ Côté employeur, l'abondement au PER d'entreprise collectif *« ne peut pas dépasser 3 fois le montant
que vous avez vous-même versé, ni être supérieur à 7 690 € »*. Le millésime de ce montant n'est pas
précisé par la page source : **à recouper avant de le citer comme le plafond d'une année donnée.**

## Le plafond de déduction : deux formules, et on retient la plus favorable

**Article 163 quatervicies du CGI**, version en vigueur au 21/02/2026, verbatim :

> *« une fraction égale à 10 % de ses revenus d'activité professionnelle […] retenus dans la limite de
> 8 fois le montant annuel du plafond mentionné à l'article L. 241-3 du code de la sécurité sociale ou,
> si elle est plus élevée, une somme égale à 10 % du montant annuel du plafond précité »*

Traduit : **le plus élevé de (10 % des revenus d'activité de l'année précédente, plafonnés) ou du
plancher.**

| Versements de… | Calculés sur les revenus de… | Maximum | Plancher |
|---|---|---|---|
| **2025** (déclarés en 2026) | 2024 (PASS **46 368 €**) | **37 094 €** | **4 637 €** |
| **2026** (à déclarer en 2027) | 2025 | **37 680 €** | **4 710 €** |

⚠️ **Le piège de millésime est ici**, et il est double : le plafond se calcule sur les revenus de
**l'année précédente**, et les deux jeux de montants circulent en même temps dans les documents
officiels. Vérifiez toujours **de quelle année de versement** parle le chiffre lu.

★ **Le plancher est acquis même sans aucun revenu d'activité.** Un conjoint sans profession, un
retraité, un primo-déclarant disposent donc d'une capacité de déduction. Ce n'est pas un détail : c'est
la matière première du levier suivant.

⛔ **Le plafond individuel est diminué** de l'« épargne retraite professionnelle » de l'année
précédente : cotisations aux régimes obligatoires d'entreprise, Madelin, et **abondement de l'employeur
exonéré dans la limite de 16 % du plafond annuel de la sécurité sociale (7 419 € en 2024)**, ainsi que
les jours de compte épargne-temps monétisés dans la limite de **10 jours**. **Un salarié bien couvert
par son entreprise a donc un plafond individuel plus faible qu'il ne le croit.**

★ **Le plafond n'a pas à être calculé à la main : il est imprimé sur l'avis d'imposition** sous
l'intitulé « plafond pour les cotisations versées en … ». On ne le recalcule que s'il est absent ou
erroné.

### ★★ Premier levier — le report des plafonds non utilisés passe de 3 ans à 5 ans

**Le CGI, version en vigueur au 21/02/2026 :** *« La différence, lorsqu'elle est positive, constatée au
titre d'une année […] peut être utilisée au cours de l'une des cinq années suivantes. »*

| Plafond de l'année… | Report | Utilisable jusqu'en… |
|---|---|---|
| **2024** | **3** ans | **2027** |
| **2025** | **3** ans | **2028** |
| **2026** et suivantes | **5** ans | — |

⚠️ **Deux pages officielles disent encore « trois années précédentes »** : la page impots.gouv.fr
« Épargne retraite » (07/04/2026) et la notice 2041-GX millésime 2026. **Elles ne sont pas fausses,
elles portent sur les versements de 2025**, qui relèvent encore du régime de 3 ans. Le texte de loi fait
foi pour les plafonds à partir de 2026. ⇒ **Ne conclure ni « la page est périmée », ni « le CGI ne
s'applique pas » : lire le millésime.**

★ Les cotisations s'imputent **d'abord sur le plafond de l'année**, puis sur les reliquats **du plus
ancien au plus récent** — ce qui préserve mécaniquement les reliquats les plus jeunes.

### ★★ Second levier — la mutualisation entre conjoints tient à UNE case cochée

**Le CGI, verbatim :** *« Les membres d'un couple marié ou les partenaires liés par un pacte civil de
solidarité […] soumis à imposition commune, peuvent déduire les cotisations ou primes mentionnées au 1,
dans une limite annuelle égale au total des montants déductibles pour chaque membre du couple ou chaque
partenaire du pacte. »*

**Et la notice 2041-GX dit comment l'obtenir :** *« Pour bénéficier de la mutualisation de leurs
plafonds de déduction, les intéressés doivent cocher la case **6QR** de la rubrique 6 de la déclaration
n° 2042. L'option ainsi exercée est annuelle. »*

★★ **C'est un droit qui se perd faute d'être connu.** Sans la case 6QR, le plafond inutilisé du conjoint
**reste inutilisable — même en déclaration commune**. Combiné avec le plancher, cela signifie qu'un
couple dont un seul membre a des revenus d'activité dispose d'une capacité de déduction égale au plafond
de celui qui travaille **plus le plancher de l'autre**.

- L'option s'applique à **toutes les périodes d'imposition commune**, y compris **l'année du mariage ou
  du Pacs** et **celle du décès**.
- ⛔ Elle **ne concerne pas les enfants rattachés** : *« Cette disposition ne concerne pas les autres
  membres du foyer fiscal (rattachés de droit ou sur option), tels que les enfants. »*
- ⛔ Si on mutualise, **ne rien porter** en 6PS / 6PT : l'administration calcule alors le plafond
  automatiquement.

### ★★ Le versement en trop est perdu, définitivement

**Notice 2041-GX, verbatim :**

> *« la fraction excédentaire des cotisations versées n'est pas déductible du revenu global. Il en est
> ainsi même si un autre membre du foyer fiscal n'a pas, en tout ou partie, utilisé lui-même ses propres
> capacités de déduction. Cette fraction excédentaire n'est pas non plus reportable sur une année
> ultérieure. »*

★★ **C'est le plafond qui se reporte, jamais le versement.** Verser au-delà de son plafond ne crée aucun
droit futur : l'excédent est **perdu comme avantage fiscal**, tout en restant **bloqué** dans le plan
jusqu'à la retraite ou un cas de déblocage. C'est la seule erreur de ce fichier qui soit **strictement
irréversible** — la déduction perdue ne se rattrape pas, contrairement à beaucoup d'erreurs fiscales
corrigibles par le service de correction ou une réclamation (`declaration-annuelle.md`).

⇒ **Le bon ordre est donc : lire son plafond sur l'avis d'imposition, cocher 6QR si couple, puis verser
— jamais l'inverse.**

## ★★ La sortie : la moitié de l'arbitrage

À la retraite, les versements volontaires se dénouent **au choix** : capital, rente viagère, ou les deux.

| | **Versements DÉDUITS** | **Versements NON déduits** |
|---|---|---|
| **Capital — part des versements** | barème de l'impôt sur le revenu, catégorie pensions, **sans l'abattement de 10 %**, **sans** prélèvements sociaux | **exonérée d'impôt sur le revenu et de prélèvements sociaux** |
| **Capital — part des gains** | PFU **12,8 %** + prélèvements sociaux = **31,4 %** en 2026 (**30 %** en 2025) | idem : **31,4 %** en 2026 |
| **Rente — impôt sur le revenu** | régime des **pensions de retraite**, avec l'abattement de **10 %** plafonné par foyer | régime des **rentes viagères à titre onéreux** : seule une fraction est imposable |
| **Rente — prélèvements sociaux** | **18,6 %** sur une fraction de la rente | **18,6 %** sur la fraction imposable |

**Les fractions de rente, selon l'âge au premier versement de la rente** (identiques dans les deux
colonnes, comme assiette de l'impôt ou des prélèvements sociaux) :

| Âge au premier versement | Fraction retenue |
|---|---|
| moins de **50** ans | **70 %** |
| de **50** à **59** ans | **50 %** |
| de **60** à **69** ans | **40 %** |
| **69** ans et plus | **30 %** |

★★ **L'abattement de 10 % joue sur la rente et PAS sur le capital.** À taux marginal identique, la
sortie en capital est donc **plus chère** que la rente sur la part des versements déduits. Personne ne
le dit à l'entrée, et c'est pourtant un des rares éléments chiffrés qui départage les deux sorties.

★ **Les prélèvements sociaux ont changé au 1er janvier 2026** : les produits de placement passent de
**17,2 %** à **18,6 %** (CSG **10,6 %** + CRDS **0,5 %** + prélèvement de solidarité **7,5 %**), ce qui
porte le PFU global de **30 %** à **31,4 %**. ⚠️ **Les revenus fonciers et les plus-values immobilières
restent à 17,2 %** — ne pas généraliser le nouveau taux. ⇒ `revenus-financiers.md` pour le PFU et
l'option pour le barème.

## ★ Celui qui n'a PAS déduit : la sortie n'est pas la même

La déduction est un **choix, versement par versement** : *« Au moment de chaque versement volontaire,
vous devez indiquer à votre gestionnaire de PER si vous choisissez la déduction de vos revenus
imposables. »*

Renoncer à la déduction change tout à la sortie : **la part des versements devient exonérée d'impôt sur
le revenu ET de prélèvements sociaux**, et seuls les gains sont taxés. Le plan cesse d'être un décalage
d'impôt pour devenir une simple enveloppe.

★ **Ce point est presque toujours ignoré, et il a une conséquence pratique** : quelqu'un dont le taux
marginal est nul ou faible ne « perd » rien en ne déduisant pas — il n'avait rien à gagner à l'entrée —
et **s'évite l'imposition de sortie**. ⚠️ En sens inverse, **la traçabilité devient essentielle** : c'est
le gestionnaire qui distingue les versements déduits des autres. **Conservez les attestations** — sans
elles, il n'y a rien pour prouver qu'un versement n'a pas été déduit.

## Le déblocage anticipé : sept cas, et deux régimes fiscaux

**Les six « accidents de la vie »**, tels qu'énoncés par service-public :

- décès de l'époux, épouse ou partenaire de Pacs du titulaire ;
- **invalidité de 2e ou 3e catégorie** du titulaire, de ses enfants, de son époux ou épouse, ou de son
  partenaire de Pacs ;
- affection grave, handicap ou accident d'une particulière gravité chez l'enfant à charge ;
- **surendettement** — *« c'est la commission de surendettement qui doit écrire à l'organisme
  gestionnaire du PER »* ;
- **expiration des droits à l'assurance chômage**, ou cessation de la fonction de mandataire social
  depuis au moins **2** ans sans contrat de travail et sans liquidation de pension ;
- cessation d'activité non salariée à la suite d'un **jugement de liquidation judiciaire**.

**Le septième cas** est l'**achat de la résidence principale** — régime fiscal entièrement différent.

★★ **Le régime des accidents de la vie est le seul cas où le PER cesse d'être un décalage et devient un
gain définitif** : *« La part du capital débloqué correspondant aux versements ayant alimenté le PER est
exonérée d'impôt sur le revenu et de prélèvements sociaux »*, et seuls les gains supportent les
prélèvements sociaux. **La déduction obtenue à l'entrée n'est jamais reprise.** C'est l'information la
plus utile de ce paragraphe, et elle est rarement dite.

★ **Le surendettement ne se demande pas soi-même** : la demande passe par la commission. Quelqu'un qui
ignore cela croit le déblocage fermé.

### ⚠️ La résidence principale est la sortie la plus chère de toutes

| | Versements déduits | Versements non déduits |
|---|---|---|
| Part des versements | **imposée au barème, sans l'abattement de 10 %**, exonérée de prélèvements sociaux | **exonérée** d'impôt sur le revenu et de prélèvements sociaux |
| Part des gains | PFU **31,4 %** (2026) | PFU **31,4 %** (2026) |

★★ **C'est le pire moment fiscal pour sortir des versements déduits** : le capital tombe en une fois,
dans une année où l'on est **encore en activité** — donc au taux marginal le plus haut de la vie — et il
peut à lui seul faire franchir une borne du barème. Le PER utilisé comme véhicule d'apport immobilier
**concentre le décalage d'impôt au plus mauvais endroit**. ⇒ Le dire est légitime : c'est un constat de
mécanique fiscale, pas un conseil de placement.

⚠️ **Et le compartiment obligatoire reste fermé** : *« achat de la résidence principale (mais, dans ce
cas, les droits issus de versements obligatoires restent bloqués) »*.

## ★ Le décès : le pivot est l'âge AU DÉCÈS

Le régime dépend d'abord de la **nature** du plan : un **PER bancaire** (compte-titres) entre dans
l'**actif successoral** et suit la fiscalité des successions. Un **PER assurantiel** suit des règles
proches de l'assurance-vie :

| Décès du titulaire | Traitement |
|---|---|
| **avant 70 ans** | abattement de **152 500 €** **par bénéficiaire** |
| **après 70 ans** | droits de succession après un abattement **global** de **30 500 €** partagé entre les bénéficiaires |

★★ **Le pivot est l'âge du titulaire AU DÉCÈS, pas son âge aux versements** — l'inverse de
l'assurance-vie. La croyance transposée depuis l'assurance-vie est donc fausse ici, et elle porte sur
des montants importants. ⇒ Le droit des successions lui-même relève du rôle `famille` ; ici, seule la
fiscalité est traitée.

## Comment poser le raisonnement, sans jamais recommander

Ce que le rôle `impots` peut faire, c'est **rendre le calcul visible** :

1. **Quel est le taux marginal de l'année du versement ?** C'est lui, et pas le taux moyen, qui mesure
   l'économie d'entrée (`impot-revenu.md`).
2. **Quel plafond est réellement disponible ?** Celui de l'avis d'imposition, plus les reliquats
   reportables, plus le plafond du conjoint **si 6QR est cochée**.
3. **Quel serait le taux marginal de l'année de sortie, retrait inclus ?** Pas le taux marginal actuel :
   celui que le retrait fabrique.
4. **Quelle sortie est envisagée ?** Capital sans abattement, rente avec abattement, déblocage anticipé
   exonéré, résidence principale au plein tarif : quatre fiscalités différentes.
5. **Quel est le coût de l'immobilisation ?** L'argent est bloqué jusqu'à la retraite hors cas de
   déblocage. **Ce n'est pas un paramètre fiscal**, mais il pèse plus que l'écart de taux marginal dans
   beaucoup de situations — et le signaler est de l'information, pas du conseil.

⛔ **Là où il faut s'arrêter** : dès que la question devient « est-ce que je devrais ? », « combien
verser ? », « quel contrat ? », ou dès qu'un rendement est comparé. C'est du **conseil en
investissement** — voir `activites-reglementees.md` du rôle `juriste`.

## Les obligations déclaratives et les cases

Tout se déclare à la **rubrique 6 « Charges déductibles »** de la déclaration **2042**, au vu de
l'attestation du gestionnaire.

| Case | Ce qu'on y porte |
|---|---|
| **6NS / 6NT / 6NU** | **cotisations volontaires versées sur le PERIN, le PERECO ou le PERO** |
| **6RS / 6RT / 6RU** | cotisations versées au PERP et produits assimilés |
| **6QS / 6QT / 6QU** | épargne retraite constituée dans le cadre de l'entreprise (versements obligatoires, abondement exonéré, jours de CET) |
| **6OS / 6OT / 6OU** | versements facultatifs des non-salariés déjà déduits du résultat professionnel (BIC, BNC, BA, article 62) |
| **6PS / 6PT / 6PU** | plafond **recalculé par le contribuable**, uniquement s'il est absent ou erroné sur l'avis |
| **6QR** | ★★ case à cocher — **mutualisation du plafond du couple**, option **annuelle** |
| **6QW** | case à cocher — **première domiciliation fiscale en France** (plafond complémentaire) |

⚠️ **Les montants portés en 6QS à 6QU et 6OS à 6OT diminuent le plafond de déduction de l'année
suivante.** Ce sont des cases d'information, pas des déductions supplémentaires — les confondre fait
surestimer sa capacité de versement de l'année d'après.

★ **L'attestation ne se joint pas à la déclaration**, mais doit être conservée pour être produite à la
demande de l'administration. **C'est elle qui prouve la déduction — ou l'absence de déduction.**

⚠️ **Le plafond doit être recalculé** en cas de **mariage, Pacs, divorce, séparation, rupture de Pacs ou
décès** survenu dans l'année, et pour un **primo-déclarant** précédemment rattaché au foyer de ses
parents.

## ⚠️ La réserve que je n'ai pas pu lever : la limite d'âge de 70 ans

**service-public écrit**, page du 18/06/2026 : *« Depuis le 1er janvier 2026, les versements effectués
sur votre PER après vos 70 ans sont toujours possibles, mais ne sont plus déductibles. »*

**Mais** : l'article 163 quatervicies du CGI, dans sa version en vigueur au 21/02/2026, **ne contient ni
« soixante-dix » ni « 70 ans »** — vérifié par lecture littérale du texte — et la page impots.gouv.fr
du 07/04/2026 ne mentionne aucune limite d'âge.

⇒ **La base légale n'a pas été localisée.** L'entrée est en `a_verifier: true`. ⛔ **Ne présentez pas
cette limite comme acquise, et ne dites pas non plus qu'elle n'existe pas** : dites qu'une source
officielle l'affirme, que le texte consulté ne la porte pas, et que **la vérification doit précéder tout
versement après 70 ans**.

## Ce qui reste à écrire — par ordre d'utilité

- ★★ Le **plafond de l'abattement de 10 %** sur les pensions (montant annuel par foyer fiscal) : il
  manque, et **sans lui l'arbitrage capital / rente ne se chiffre pas** jusqu'au bout. C'est le trou le
  plus gênant de ce fichier.
- ★★ Le **cas des travailleurs indépendants** : le plafond **Madelin** et la fraction de **15 %** de la
  quote-part de bénéfice, entrevus dans la notice 2041-GX mais non vérifiés ici. Le calcul du plafond
  n'est pas le même que pour un salarié, et c'est la population qui verse le plus.
- ★ Le **texte du code monétaire et financier** sur les cas de déblocage (article L224-4) : la liste
  utilisée ici vient de service-public, **pas du texte lui-même** — à confirmer pour l'exhaustivité.
- ★ Le **plafond complémentaire des personnes nouvellement domiciliées en France** (case 6QW) : la
  notice l'annonce comme le triple du plafond de droit commun, non vérifié ici.
- Le **transfert** entre plans (PERP, Perco, article 83 vers un PER) et ses conséquences fiscales.
- L'**option pour le barème progressif** en lieu et place du PFU sur la part des gains, et quand elle
  devient favorable → `revenus-financiers.md`.
- Le **PER d'un mineur** et l'articulation avec le rattachement au foyer fiscal des parents.
- La **sortie fractionnée** en plusieurs années, seul outil de lissage du taux marginal de sortie.

## Sources

- Plan d'épargne retraite (PER), page du 18/06/2026 —
  <https://www.service-public.gouv.fr/particuliers/vosdroits/F34982>
- Code général des impôts, article 163 quatervicies, version en vigueur au 21/02/2026 —
  <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053542827>
- Épargne retraite, page du 07/04/2026 — <https://www.impots.gouv.fr/particulier/epargne-retraite>
- Notice 2041-GX « Épargne retraite », millésime 2026 —
  <https://www.impots.gouv.fr/formulaire/2041-gx/epargne-retraite>
- Prélèvements sociaux sur les revenus du patrimoine et de placement, page du 30/06/2026 —
  <https://www.service-public.gouv.fr/particuliers/vosdroits/F2329>
- Déclarer les rentes viagères, page du 15/04/2026 —
  <https://www.service-public.gouv.fr/particuliers/vosdroits/F3173>
- Taux marginal et taux moyen → `impot-revenu.md`

## Rappel de cadrage

Ce fichier alimente le skill `impots`, un outil d'**aide à la décision**. Il ne remplace ni un
professionnel inscrit et assuré, ni l'administration compétente, et **il ne calcule aucun impôt**.
⚠️ Il traite la **fiscalité** d'un produit d'épargne, **jamais son opportunité** : recommander un
placement adapté à une situation est un **conseil en investissement**, activité réglementée — voir
`activites-reglementees.md` du rôle `juriste`. ⛔ **Aucune recommandation de souscription ne doit être
tirée de ce fichier**, y compris par déduction à partir des écarts de taux qu'il décrit.
