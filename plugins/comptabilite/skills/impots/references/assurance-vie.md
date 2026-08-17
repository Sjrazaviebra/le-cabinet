# Assurance-vie : rachats, ancienneté, succession

> **État : `RÉDIGÉ`** pour le périmètre du stub : régime des rachats et calcul de la part taxable,
> seuil des 8 ans, taux selon l'ancienneté **et** la date des versements, abattement annuel,
> prélèvements sociaux, exonérations totales, régime successoral et clause bénéficiaire.
> Vérifié le **2026-08-17**. Sources : fiches service-public **vérifiées le 15/04/2026** (imposition
> des produits) et **le 30/06/2026** (prélèvements sociaux) · page impots.gouv.fr du **08/04/2026** ·
> **notice officielle 2705-A-NOT-SD, millésime 10/2025** (fiscalité au décès) · CGI article 125-0 A
> sur Légifrance, **version en vigueur depuis le 01/01/2022** · doctrine BOFiP de **06/2021** et
> **06/2022**. ⚠️ La notice 2705-A et la doctrine BOFiP ont **plus de six mois** : les montants qu'elles
> portent sont **à recouper avant tout usage chiffré**. Une page impots.gouv.fr utilisée pour
> l'exonération du conjoint date de **07/2022** — même réserve, signalée sur place.

## ⛔ Avant tout : ce fichier ne dit pas s'il faut souscrire, arbitrer ou racheter

Il dit **comment un rachat est imposé** et **comment un capital-décès est taxé**. Recommander un
placement adapté à une situation, ou conseiller de racheter plutôt que d'attendre, est un **conseil en
investissement** : activité réglementée ⇒ voir `activites-reglementees.md` du skill `juriste`.

## ★★ Le point qui commande tout : deux dates, pas une

La quasi-totalité des erreurs sur ce sujet vient de là. Deux paramètres **indépendants** décident du
régime, et il faut les deux :

- **L'ancienneté DU CONTRAT** — comptée depuis sa souscription.
- **La DATE de chaque versement** — avant ou à partir du **27 septembre 2017**.

★★ **Première conséquence contre-intuitive** : les 8 ans se comptent sur le **contrat**, pas sur
l'argent.
Le CGI parle de la « durée du contrat » — « 7,5 % lorsque la durée du contrat a été égale ou
supérieure à [...] huit ans pour les contrats souscrits à compter du 1er janvier 1990 ». **Un
versement fait hier sur un contrat ouvert il y a douze ans est immédiatement dans le régime des plus
de 8 ans.** C'est ce qui rend un vieux contrat précieux — et ce qui fait qu'un contrat fermé puis
rouvert repart de zéro.

★★ **Deuxième conséquence contre-intuitive** : **un seul contrat peut relever des deux régimes en même
temps**, une part de ses produits sous l'ancien, une autre sous le nouveau. « Tous les contrats ne
sont pas soumis au même régime » est déjà vrai **à l'intérieur d'un même contrat**.

⚠️ Et pour les contrats les plus anciens, souscrits entre **1983** et **1989**, le seuil du taux
réduit est de **6** ans, pas 8 — le texte le dit expressément.

## Le rachat : seule la part de produits est imposable

**Tant qu'on ne rachète rien, rien n'est imposable à l'impôt sur le revenu.** L'imposition se
déclenche au rachat, partiel ou total.

★★ **Un rachat partiel n'est JAMAIS imposé sur son montant total.** Il est composé, à proportion, de
capital (non imposable) et de produits (imposables). La doctrine BOFiP donne la formule :

> « Montant du rachat partiel − [total des primes versées à la date du rachat partiel × (montant du
> rachat partiel / valeur de rachat totale à la date du rachat partiel)] »

⇒ Autrement dit, la part imposable du rachat est **la même proportion que celle des gains dans la
valeur totale du contrat** au jour du rachat. **La croyance inverse — « si je retire, je suis taxé sur
tout » — empêche des gens de toucher à une épargne dont ils ont besoin.**

## Les taux : le tableau à double entrée

| Ancienneté du contrat | Primes versées **avant le 27 septembre 2017** | Primes versées **à partir du 27 septembre 2017** |
|---|---|---|
| Moins de 4 ans | **35 %** | **12,8 %** |
| De 4 à 8 ans | **15 %** | **12,8 %** |
| Plus de 8 ans | **7,5 %** | **7,5 %** jusqu'au seuil de primes de **150 000 €**, **12,8 %** au-delà |

**Deux mécaniques différentes derrière ces chiffres :**

- **Primes antérieures au 27 septembre 2017** : prélèvement forfaitaire **libératoire**, sur option —
  l'impôt est soldé.
- **Primes du 27 septembre 2017 ou après** : l'assureur prélève d'abord un prélèvement forfaitaire
  **non libératoire**, qui n'est qu'un **acompte**. Les produits sont ensuite portés sur la
  déclaration de revenus, et « l'excédent éventuel vous est restitué ».

### ★ Le seuil de 150 000 € : vérifié, et il ne dit pas ce qu'on croit

Il ne porte **ni sur la valeur du contrat, ni sur les gains**, mais sur les **primes versées**. La
doctrine est explicite : sont prises en compte les « primes versées à compter du 27 septembre 2017 et
qui, **au 31 décembre de l'année qui précède le fait générateur** de l'imposition des produits
concernés, **n'ont pas déjà fait l'objet d'un remboursement en capital** ». Et l'appréciation est
globale : « Le montant de 150 000 € est calculé pour **l'ensemble de vos contrats** d'assurance vie,
si vous en détenez plusieurs. »

★★ **Le piège** : les primes **antérieures** au 27 septembre 2017 **consomment le seuil**. Ce n'est
pas une enveloppe neuve réservée aux versements récents. La fraction des produits qui reste à 7,5 %
s'obtient par le prorata donné par la doctrine :

> produits × (150 000 € − primes antérieures au 27/09/2017 non remboursées) / primes versées à
> compter du 27/09/2017 non remboursées

⇒ Quelqu'un qui détient déjà 150 000 € de primes anciennes n'a **aucune** fraction à 7,5 % sur ses
versements nouveaux, même avec un contrat de vingt ans.

## L'abattement annuel après 8 ans, et l'arbitrage prélèvement / barème

Après 8 ans, les produits ne sont imposés qu'**après** un abattement annuel :

| Situation | Abattement annuel sur les produits |
|---|---|
| Célibataire, veuf ou divorcé | **4 600 €** |
| Marié ou pacsé soumis à imposition commune | **9 200 €** |

Il vaut « pour l'ensemble des bons ou contrats détenus par un même contribuable » : **un seul
abattement par foyer et par an**, pas un par contrat.

★ **L'assureur ne l'applique pas.** Il prélève son acompte sur les produits **bruts** ; l'abattement
joue au moment de la déclaration, et le trop-perçu revient ensuite. **Un rachat de janvier peut donc
laisser 7,5 % immobilisés jusqu'à la régularisation de l'année suivante** — utile à savoir quand on
rachète pour un besoin de trésorerie daté.

★ **L'ordre d'imputation n'est pas neutre** : l'abattement s'impute **d'abord** sur les produits des
primes versées jusqu'au 26 septembre 2017, **ensuite** sur ceux des primes postérieures.

### L'option pour le barème progressif

Elle existe au rachat comme pour les autres revenus financiers. ⚠️ **Elle est globale pour l'ensemble
des revenus de capitaux mobiliers et plus-values du foyer** : on ne l'exerce pas pour un rachat
d'assurance-vie tout seul. ⇒ **L'arbitrage prélèvement forfaitaire / barème, ses conditions et son
caractère irrévocable sont traités dans `revenus-financiers.md`** — ne le refaites pas ici.

### ★ La dispense d'acompte, un droit qui se perd faute d'être demandé

Le prélèvement forfaitaire **non libératoire** peut être évité d'avance. Condition : un **revenu
fiscal de référence de l'avant-dernière année inférieur à 25 000 €** (personne seule) ou **50 000 €**
(couple). ⚠️ **La demande se fait auprès de l'assureur, avant le rachat, au plus tard le 30 novembre
de l'année précédant celle du paiement.** Passé ce point, l'acompte est prélevé et il faut attendre la
déclaration pour récupérer le trop-versé.

## ★★ Les prélèvements sociaux : dus même quand l'impôt ne l'est pas

C'est **la** phrase à retenir de ce fichier :

> « Les gains tirés d'un contrat d'assurance-vie sont **toujours** soumis aux prélèvements sociaux
> (CSG, CRDS) au taux de **17,2 %**. »

Décomposition : **CSG 9,2 %** + **CRDS 0,5 %** + **prélèvement de solidarité 7,5 %**.

Et la doctrine ferme la porte : « **Il n'est pas tenu compte de cet abattement pour la détermination
des prélèvements sociaux.** »

★★ **⇒ « Après 8 ans, l'assurance-vie est exonérée » est FAUX.** Ce qui est vrai : après 8 ans,
l'**impôt sur le revenu** est réduit et effacé jusqu'à l'abattement. Les **17,2 %** restent dus, sur
la totalité des produits, abattement compris. Même chose pour les exonérations pour licenciement ou
invalidité ci-dessous : elles portent sur l'impôt, **pas** sur les prélèvements sociaux. Quelqu'un
qui a budgété « zéro prélèvement » se trompe d'environ un sixième des gains.

⚠️ **Piège d'actualité à ne pas retourner** : la fiche sur les prélèvements sociaux affiche pour 2026
un taux de **18,6 %** dans le **cas général des produits de placement** (CSG portée à **10,6 %**),
mais son tableau « Assurance vie » **conserve 9,2 % de CSG, soit 17,2 %**. ⛔ **N'appliquez pas 18,6 %
à un rachat d'assurance-vie.** Cette divergence est récente : **recoupez-la** au prochain millésime,
c'est exactement le genre d'écart qui produit un calcul faux énoncé avec assurance.

## Les exonérations totales d'impôt

Le CGI prévoit une exonération **quelle que soit la durée du contrat** :

> « Les produits en cause sont exonérés, quelle que soit la durée du contrat, lorsque celui-ci se
> dénoue par le versement d'une rente viagère ou que ce dénouement résulte du **licenciement** du
> bénéficiaire des produits ou de sa **mise à la retraite anticipée** ou de son **invalidité** ou de
> **celle de son conjoint** [...] »

S'y ajoute la **liquidation judiciaire**. L'invalidité visée est celle de **deuxième ou troisième
catégorie** de la sécurité sociale.

★ **L'événement peut frapper le conjoint ou le partenaire de Pacs**, pas seulement le titulaire du
contrat. C'est la moitié du dispositif qu'on oublie : un contrat au nom d'une personne peut être
racheté en franchise d'impôt parce que **son conjoint** a été licencié.

⚠️ ★★ **Mais l'exonération se PERD si le rachat est tardif** : le rachat doit intervenir **avant la
fin de l'année qui suit celle de l'événement**. Un licenciement de mars laisse jusqu'au 31 décembre
de l'année suivante — pas davantage. **C'est un droit à échéance, et personne ne le rappelle au
guichet.**

⚠️ Rappel : ces exonérations ne touchent **pas** les prélèvements sociaux de 17,2 %.

## Le décès : un régime successoral entièrement à part

⚠️ **Ce n'est pas le même impôt que le rachat.** Au décès, on ne taxe plus des produits : on taxe un
capital transmis, selon des règles propres, **hors barème des droits de succession** dans le cas
principal. Deux régimes selon **l'âge de l'assuré au moment de CHAQUE versement** — pas au décès.

### Primes versées avant 70 ans — prélèvement de l'article 990 I

| Élément | Valeur |
|---|---|
| Abattement | **152 500 € par bénéficiaire** |
| Taux sur la part taxable ≤ **700 000 €** | **20 %** |
| Taux au-delà | **31,25 %** |

★ **Le seuil de 700 000 € s'apprécie sur « la fraction de la part taxable de chaque bénéficiaire »** —
donc **après** l'abattement et **bénéficiaire par bénéficiaire**, pas sur le capital global du
contrat. Multiplier les bénéficiaires multiplie les abattements : c'est le cœur du régime.

★★ **Et le régime des contrats les plus anciens est différent** — la source d'erreur numéro un du
sujet. Pour un contrat **souscrit avant le 20 novembre 1991 et non modifié substantiellement
depuis**, la notice officielle indique **« Exonération »** pure et simple pour les primes versées
**jusqu'au 12 octobre 1998 inclus**, et cela **« quel que soit l'âge de l'assuré »**. ⇒ **Le seuil des
70 ans ne s'y applique pas**, et aucune déclaration n'est à déposer. ★ Précision décisive de la même
notice : « la seule prorogation de la durée du contrat **ne peut pas** être analysée comme une
modification substantielle » — l'antériorité survit à une prorogation.

### Primes versées après 70 ans — droits de mutation, article 757 B

Les primes versées après le 70ᵉ anniversaire sortent du prélèvement et rentrent dans les **droits de
mutation par décès**, après un abattement de **30 500 €**.

⚠️ **Cet abattement n'a pas la même nature que les 152 500 €** : « L'abattement de 30 500 € est
**global** et s'applique à l'ensemble des contrats souscrits par le défunt. » Il se **partage** entre
les bénéficiaires, il ne se multiplie pas. En revanche « l'abattement en fonction du lien de parenté
entre le défunt et le bénéficiaire peut **s'ajouter** à l'abattement de 30 500 € » ⇒ barème et
abattements familiaux dans `succession.md` du skill `famille`.

★★ **Ce sont les PRIMES qui sont taxées, pas le capital versé.** Les **produits** attachés aux primes
versées après 70 ans échappent aux droits de succession. Et la notice ajoute une sécurité : « Dans
l'hypothèse où les capitaux à verser [...] au titre des primes versées après le 70ᵉ anniversaire de
l'assuré sont **inférieurs** à ces primes, l'assiette des droits est limitée à ces capitaux. » Un
contrat en perte ne fait donc pas payer de droits sur de l'argent qui n'existe plus.

⚠️ **Le PER ne suit pas cette règle** : pour un plan d'épargne retraite non dénoué, la notice retient
l'âge de l'assuré **au jour du décès**, et non la date des versements. ⇒ **`epargne-retraite-per.md`**,
n'appliquez pas mécaniquement le raisonnement de l'assurance-vie.

### Le conjoint et le partenaire pacsé

> « Le conjoint survivant et le partenaire lié au défunt par un PACS sont **exonérés** de ce
> prélèvement, comme pour les droits de succession lorsque le décès est survenu après le 22 août
> 2007. »

⚠️ **Page source publiée le 12/07/2016 et modifiée le 04/07/2022 : plus de six mois, à recouper.**
⛔ **Le concubin n'est pas concerné** — aucune exonération de ce type, quelle que soit la durée de vie
commune.

★ **Ne confondez pas deux choses différentes** : l'exonération **de fond** (issue de la loi du 22 août
2007) et la **dispense de formalité** — la notice dispense de déclaration les avoirs versés « à
compter du 1er janvier 2018 [...] au conjoint survivant ou au partenaire lié au défunt par un Pacs,
sous réserve qu'ils aient leur domicile en France ». La seconde ne crée pas la première.

### La clause bénéficiaire

C'est elle qui désigne qui reçoit, et elle **ne se lit pas dans le testament**. ⇒ **Le droit civil de
la clause bénéficiaire — rédaction, acceptation, révocation, primes manifestement exagérées,
articulation avec la réserve héréditaire — relève du skill `famille`** (`donation.md` et
`succession.md`). Ici, seule la **fiscalité** est traitée.

★ Ce que la fiscalité impose de dire quand même : **le nombre et l'identité des bénéficiaires changent
l'impôt**, puisque l'abattement de 152 500 € est **par bénéficiaire** et que celui de 30 500 € est
**global**. Une clause écrite sans y penser ne coûte rien au civil et peut coûter cher au fiscal.

## ⏱️ La déclaration au décès, et le blocage des fonds

La **déclaration partielle de succession – assurance-vie n° 2705-A** se dépose au service chargé de
l'enregistrement du dernier domicile du défunt.

| Point | Règle |
|---|---|
| Délai (France métropolitaine) | **6 mois** suivant le décès ; un retard « peut donner lieu au paiement de pénalités » |
| Délais spéciaux outre-mer | **6**, **12** ou **24 mois** selon le département et le lieu du décès |
| Nombre de formulaires | **un par organisme d'assurance**, déposés en même temps |
| Aucune déclaration à déposer | contrats d'avant le 20 novembre 1991 non modifiés substantiellement ; primes versées **avant** le 70ᵉ anniversaire |

★★ **Le point le plus utile de cette section, et il est pratique, pas fiscal.** Quand une déclaration
est due, l'administration délivre un certificat sur le formulaire lui-même :

> « Vous devez obligatoirement présenter ce certificat à l'organisme d'assurance afin d'obtenir le
> versement du capital qui vous est dû. [...] Dès lors, l'organisme d'assurance **ne peut pas refuser
> le déblocage des fonds** lorsque le bénéficiaire présente le formulaire 2705-A complété par
> l'administration. »

⇒ **C'est l'argument opposable à un assureur qui fait attendre un bénéficiaire.**

★ La notice recommande aussi de demander à l'assureur de **payer les droits directement** au service
de l'enregistrement : dans ce cas aucun certificat n'est nécessaire et le traitement est plus rapide.

★ **Dispense de certificat** quand les sommes dues n'excèdent pas **7 600 €** et reviennent à des
successibles en ligne directe non domiciliés à l'étranger — mais elle est « subordonnée à la
condition que le bénéficiaire de l'assurance dépose une **demande écrite** ». **Sans la demande, pas
de dispense.**

## Ce qui reste à écrire

**Les plus utiles d'abord :**

- ★★ **Les primes manifestement exagérées** : le seul mécanisme qui fait rentrer l'assurance-vie dans
  la succession civile, et la contestation la plus fréquente entre héritiers. Le civil est au skill
  `famille` ; **sa conséquence fiscale** manque ici.
- ★★ **Recouper le taux des prélèvements sociaux au millésime suivant** : la divergence 17,2 % /
  18,6 % relevée plus haut est le point le plus périssable du fichier, et le plus susceptible de
  produire un calcul faux.
- ★ **L'exonération de l'article 796-0 ter** pour le frère ou la sœur veuf, célibataire, âgé ou
  invalide ayant cohabité avec le défunt : citée par impots.gouv.fr, **volontairement non chiffrée
  ici** faute d'avoir obtenu le texte verbatim (conditions d'âge et de durée de cohabitation). À
  vérifier sur Légifrance avant de l'énoncer.
- ★ **Le contrat en unités de compte contre le fonds en euros** : le moment où les prélèvements
  sociaux sont prélevés diffère (au fil de l'eau ou au rachat). **Non vérifié** : la fiche consultée
  renvoie à l'établissement sans le trancher.
- **Le contrat non réclamé** : recherche Ciclade, prescription, transfert à la Caisse des dépôts —
  fiches service-public identifiées mais non exploitées.
- **La sortie en rente viagère** et son imposition propre (le CGI l'exonère au titre des produits,
  mais la rente elle-même est imposable).
- **Le contrat de capitalisation**, régime voisin mais successoralement différent.
- **La situation internationale** : non-résident, contrat souscrit à l'étranger, convention fiscale.
  ⛔ Sujet à arrêter et à renvoyer, pas à traiter au jugé.

## Sources

Pages réellement consultées le **2026-08-17** :

- Imposition des revenus d'un contrat d'assurance-vie (fiche vérifiée le 15/04/2026) —
  <https://www.service-public.gouv.fr/particuliers/vosdroits/F22414>
- Prélèvements sociaux sur les revenus du patrimoine et de placement (fiche vérifiée le 30/06/2026) —
  <https://www.service-public.gouv.fr/particuliers/vosdroits/F2329>
- L'assurance-vie et le PEA, impots.gouv.fr (page du 08/04/2026) —
  <https://www.impots.gouv.fr/particulier/lassurance-vie-et-le-pea-0>
- Notice **2705-A-NOT-SD**, millésime **10/2025** — déclaration partielle de succession
  assurance-vie (source des montants du décès) —
  <https://www.impots.gouv.fr/sites/default/files/formulaires/2705-sd/2025/2705-sd_4290.pdf>
- Je suis bénéficiaire d'une assurance-vie, comment la déclarer ? —
  <https://www.impots.gouv.fr/particulier/questions/je-suis-beneficiaire-dune-assurance-vie-comment-la-declarer>
- Je suis bénéficiaire d'une assurance-vie, comment sont imposées les primes ? (publiée le
  12/07/2016, modifiée le 04/07/2022 — **à recouper**) —
  <https://www.impots.gouv.fr/international-particulier/questions/je-suis-beneficiaire-dune-assurance-vie-comment-sont-imposees>
- Code général des impôts, article 125-0 A (version en vigueur depuis le 01/01/2022) —
  <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000041464342/>
- BOFiP, réforme de l'imposition des produits attachés aux primes versées depuis le 27/09/2017
  (BOI-RPPM-RCM-20-15, doc du 21/06/2021) — <https://bofip.impots.gouv.fr/doctrine/pgp/11224-PGP>
- BOFiP, détermination du produit imposable et rachat partiel (BOI-RPPM-RCM-20-10-20-50, doc du
  30/06/2022) — <https://bofip.impots.gouv.fr/doctrine/pgp/3951-PGP>
- BOFiP, revenus de capitaux mobiliers, modalités d'imposition (BOI-RPPM-RCM-20) —
  <https://bofip.impots.gouv.fr/doctrine/pgp/3775-PGP>

⚠️ **Ce que je n'ai pas trouvé** : il **n'existe pas de fiche service-public consacrée à la fiscalité
de l'assurance-vie au décès**. Tous les montants successoraux de ce fichier viennent donc de la
**notice officielle du formulaire 2705-A** et d'une page impots.gouv.fr de 2022. C'est la raison pour
laquelle le rôle `famille` n'a pu rien chiffrer : la valeur est là, mais pas là où on la cherche.

## Rappel de cadrage

Ce fichier alimente le skill `impots`, un outil d'**aide à la décision**. Il ne remplace ni un
expert-comptable inscrit à l'Ordre, ni un notaire, ni un avocat fiscaliste, ni le service chargé de
l'enregistrement. ⚠️ Il traite la **fiscalité** d'un placement, **jamais son opportunité** :
recommander un placement, un arbitrage ou un rachat adapté à une situation est un **conseil en
investissement**, activité réglementée ⇒ `activites-reglementees.md` du skill `juriste`.
