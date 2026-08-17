# Droit des sociétés : la vie de la société

> **État : `PARTIEL`.** **`RÉDIGÉ`** pour l'associé unique, les assemblées et l'approbation des
> comptes, le dépôt et la confidentialité des comptes, les pouvoirs et la révocation du dirigeant, sa
> responsabilité civile et fiscale, les conventions réglementées, les clauses statutaires de la SAS,
> la cession de parts et d'actions, la perte de la moitié du capital, et la dissolution de la société
> unipersonnelle. **`À ÉCRIRE`** pour l'augmentation de capital, la liquidation ordinaire, le pacte
> d'associés et la rédaction de l'objet social — voir `Ce qui reste à écrire`.
> Vérifié le **2026-08-17** sur Légifrance (code de commerce, code civil, code pénal, CGI, LPF),
> version en vigueur relevée article par article, et sur une page
> `entreprendre.service-public.gouv.fr` **vérifiée le 11/06/2025** (à recouper) et une page **du
> 06/02/2026**.

⚠️ **Ce fichier ne traite pas du CHOIX de la forme juridique** (EI / EURL / SASU, régime social,
IR ou IS) : c'est le rôle `comptable`, fichier `formes-juridiques.md`. Ici, la société existe déjà —
on parle de **ce qui l'engage année après année**.

## ⏱️ D'abord : le calendrier annuel qu'on oublie

C'est la partie la plus rentable du fichier. Trois échéances, et **deux horloges différentes**.

| Étape | Délai | Texte |
|---|---|---|
| Approbation des comptes par les associés / l'associé unique | **6 mois** à compter de la clôture | `L223-26` (SARL), `L223-31` (EURL), `L227-9` (SAS/SASU) |
| Dépôt au greffe, support papier | **1 mois** après l'approbation | `L232-22` (SARL), `L232-23` (sociétés par actions) |
| Dépôt au greffe, voie électronique | **2 mois** après l'approbation | idem |
| Convocation de l'assemblée en SARL | **15 jours** avant, par lettre recommandée (**8 jours** si l'assemblée est convoquée après le décès du gérant unique) | `R223-20` |

**Article L223-26, alinéa 1 (version en vigueur au 01/01/2025)** :

> « Le rapport de gestion, l'inventaire et les comptes annuels établis par les gérants, sont soumis à
> l'approbation des associés réunis en assemblée, dans le délai de six mois à compter de la clôture de
> l'exercice sous réserve de prolongation de ce délai par décision de justice. »

★★ **Le raccourci de l'associé unique est un piège de calendrier.** Quand l'associé unique est aussi
le seul dirigeant, le dépôt des comptes **vaut approbation** — mais seulement s'il a lieu **dans le
même délai de six mois**. En prenant le raccourci, on ne gagne pas un mois : **on perd le mois
supplémentaire** du dépôt.

**Article L223-31, alinéa 3 (version en vigueur au 06/08/2008)** :

> « Lorsque l'associé unique est seul gérant de la société, le dépôt au registre du commerce et des
> sociétés, **dans le même délai**, de l'inventaire et des comptes annuels, dûment signés, vaut
> approbation des comptes sans que l'associé unique ait à porter au registre prévu à l'alinéa suivant
> le récépissé délivré par le greffe du tribunal de commerce. »

★ **Nuance à ne pas rater entre les deux formes** : en SASU, l'article `L227-9` réserve le même
raccourci à l'associé unique **personne physique** qui « assume personnellement la présidence ». En
EURL, `L223-31` dit seulement « seul gérant ». Une holding associée unique de SASU **n'a pas** le
raccourci.

## ★★ Le registre des décisions : la formalité la plus petite et la plus sanctionnée

En société unipersonnelle, il n'y a pas d'assemblée — il y a **un registre**. Et son absence n'est pas
un simple manquement formel : elle ouvre une **action en annulation**.

**Article L223-31, alinéas 4 et 5** :

> « L'associé unique ne peut déléguer ses pouvoirs. Ses décisions, prises au lieu et place de
> l'assemblée, sont répertoriées dans un registre.
>
> Les décisions prises en violation des dispositions du présent article peuvent être annulées à la
> demande de tout intéressé. »

★★ **« À la demande de tout intéressé »**, pas seulement de l'associé. Un créancier, un acheteur en
audit d'acquisition, un liquidateur peuvent s'en servir. Pour une SASU ou une EURL de développeur
solo, **le registre est l'unique preuve que les décisions ont existé** — et il ne coûte rien à tenir.

⛔ **« L'associé unique ne peut déléguer ses pouvoirs »** : on ne fait pas signer les décisions
d'associé par un comptable, un conjoint ou un mandataire.

⚠️ **Durée de conservation du registre** : non vérifiée ici. Une page service-public annonce six ans,
mais je n'ai pas trouvé le texte qui le fixe → dans `parametres.json`, la valeur est **`null` avec
`a_verifier: true`**. En pratique, gardez-le sans limite : il ne pèse rien.

## Dépôt des comptes : l'amende n'est pas le vrai risque

**Article R247-3 du code de commerce** : le défaut de dépôt

> « est puni de l'amende prévue par le 5e de l'article 131-13 du code pénal pour les contraventions de
> la cinquième classe. En cas de récidive, la peine applicable est celle prévue par le 5e de l'article
> 131-13 du code pénal pour les contraventions de la cinquième classe commises en récidive. »

**Article 131-13, 5° du code pénal** : « 1 500 euros au plus pour les contraventions de la 5e classe,
montant qui peut être porté à 3 000 euros en cas de récidive ».

★★ **Le vrai risque n'est pas l'amende, c'est d'entrer dans le radar du tribunal.** L'injonction de
déposer sous astreinte figure au **II de l'article L611-2**, dont le **I** est le mécanisme de
**détection des entreprises en difficulté** — convocation du dirigeant par le président du tribunal de
commerce et lever de son secret bancaire et social.

**Article L611-2, II (version en vigueur au 01/10/2021)** :

> « Lorsque les dirigeants d'une société commerciale ne procèdent pas au dépôt des comptes annuels
> dans les délais prévus par les textes applicables, le président du tribunal peut […] leur adresser
> une injonction de le faire à bref délai sous astreinte. »

Et si l'injonction reste sans effet, le président « peut également faire application à leur égard des
dispositions du deuxième alinéa du I » — c'est-à-dire **la collecte d'informations auprès des banques,
de l'URSSAF et des administrations**. ⇒ **Ne pas déposer ses comptes, c'est se signaler comme une
entreprise qui va mal.** C'est ça qui coûte cher, pas les 1 500 €.

⚠️ **Piège de lecture des sources** — l'article `L232-21` **ne concerne pas les SARL** : il visite les
sociétés en nom collectif dont tous les associés indéfiniment responsables sont des SARL ou des
sociétés par actions. Le dépôt des SARL est à **`L232-22`**, celui des sociétés par actions
(SAS, SASU, SA) à **`L232-23`**. Plusieurs synthèses en ligne se trompent sur ce point.

## ★ Les comptes déposés peuvent rester confidentiels

Beaucoup de dirigeants découvrent leurs propres chiffres publiés et croient que c'est inévitable. Ce
n'est pas le cas : `L232-25` ouvre une **déclaration de confidentialité au moment du dépôt**.

| Taille | Ce qui peut être soustrait au public |
|---|---|
| **Micro-entreprise** (`L123-16-1`) | **l'intégralité des comptes annuels** |
| **Petite entreprise** (`L123-16`) | **le compte de résultat** seul |
| **Moyenne entreprise** | présentation simplifiée du bilan et de l'annexe |

**Article L232-25 (version en vigueur au 24/05/2019)** :

> « Lors du dépôt prévu au I des articles L. 232-21 à L. 232-23, les sociétés répondant à la
> définition des micro-entreprises au sens de l'article L. 123-16-1 […] peuvent déclarer que les
> comptes annuels qu'elles déposent ne seront pas rendus publics. »

Seuils relevés sur `entreprendre.service-public.gouv.fr` (page **vérifiée le 11/06/2025**, à
recouper) — il faut ne pas dépasser **deux des trois** critères :

| | Total du bilan | Chiffre d'affaires | Salariés |
|---|---|---|---|
| Micro-entreprise | **450 000 €** | **900 000 €** | **10** |
| Petite entreprise | **7 500 000 €** | **15 000 000 €** | **50** |

⛔ **Confidentialité n'est pas opacité** : `L232-25` réserve l'accès aux comptes complets aux
autorités judiciaires et administratives et à la Banque de France. Et la déclaration doit être
**faite au moment du dépôt** — elle ne se rattrape pas après.

★ Une société **appartenant à un groupe** au sens de `L233-16` ne peut pas user de l'option
« compte de résultat ».

## Commissaire aux comptes : les seuils ont changé, et beaucoup de sources l'ignorent

**Article D221-5 (version en vigueur au 01/03/2024, décret n° 2024-152 du 28/02/2024)** :

> « le total du bilan est fixé à 5 000 000 euros, le montant hors taxe du chiffre d'affaires à
> 10 000 000 euros et le nombre moyen de salariés à cinquante. »

Deux des trois seuils dépassés à la clôture ⇒ CAC obligatoire (`L227-9-1` pour la SAS).

⚠️ **Beaucoup de contenus en ligne citent encore 4 000 000 € et 8 000 000 €** — les seuils du décret
n° 2019-514 du 24 mai 2019, **remplacés depuis**. C'est le type de chiffre qu'il faut relire à sa
source avant de le donner.

★ Deux voies indépendantes des seuils, dans une SAS : un ou plusieurs associés représentant **un
dixième** du capital peuvent **demander la nomination en justice** ; des associés représentant **un
tiers** du capital peuvent l'imposer par demande motivée à la société, pour trois exercices
(`L227-9-1`).

## Pouvoirs et révocation du dirigeant

★★ **Le contraste entre les deux formes est le point de décision le plus important de ce fichier.**

**SAS — article L227-5** : « Les statuts fixent les conditions dans lesquelles la société est
dirigée. » Une phrase, et tout est renvoyé aux statuts. ⇒ **En SAS, la protection du dirigeant, ou son
absence, est entièrement ce que les statuts en font.** Des statuts types récupérés en ligne peuvent
donc contenir une révocation *ad nutum*, sans motif ni indemnité, sans que personne ne l'ait voulu.

**SARL — article L223-25, alinéa 1 (version en vigueur au 27/03/2004)** :

> « Le gérant peut être révoqué par décision des associés dans les conditions de l'article L. 223-29,
> à moins que les statuts prévoient une majorité plus forte. **Si la révocation est décidée sans juste
> motif, elle peut donner lieu à des dommages et intérêts.** »

★★ **Lire la sanction exactement** : la révocation sans juste motif **reste valable**. Elle ouvre des
dommages-intérêts, elle **ne rend pas le dirigeant à ses fonctions**. La croyance inverse est
extrêmement répandue — et elle fait rater le seul moment utile, qui est la négociation des statuts.

★ Et il existe une seconde porte : « le gérant est révocable par les tribunaux pour cause légitime, à
la demande de **tout associé** » (`L223-25` al. 2). Un minoritaire seul peut donc agir.

⚠️ **Publicité du changement de dirigeant** : la nomination et la cessation de fonctions doivent être
déclarées au registre du commerce **dans le mois** (`R123-66`, en vigueur au 01/01/2023) :

> « Toute personne morale immatriculée demande, par l'intermédiaire de l'organisme unique mentionné à
> l'article R. 123-1, une inscription modificative dans le mois de tout fait ou acte rendant
> nécessaire la rectification ou le complément des énonciations prévues aux articles R. 123-53 et
> suivants. »

⇒ Même chose pour le siège, l'objet, le capital, la dénomination. La déclaration passe par le
**guichet unique** (`formalites.entreprises.gouv.fr`).

## ★★ Responsabilité du dirigeant : trois régimes à ne pas confondre

### 1. La faute de gestion envers la société (`L223-22`)

> « Les gérants sont responsables, individuellement ou solidairement, selon le cas, envers la société
> ou envers les tiers, soit des infractions aux dispositions législatives ou réglementaires
> applicables aux sociétés à responsabilité limitée, soit des violations des statuts, soit des fautes
> commises dans leur gestion. »

⛔ **On ne peut pas se blinder par les statuts** : « Est réputée non écrite toute clause des statuts
ayant pour effet de subordonner l'exercice de l'action sociale à l'avis préalable ou à l'autorisation
de l'assemblée, ou qui comporterait par avance renonciation à l'exercice de cette action »
(`L223-22`). Et « aucune décision de l'assemblée ne peut avoir pour effet d'éteindre une action en
responsabilité ». **Un quitus voté en assemblée ne vaut rien.**

**Prescription (`L223-23`) : 3 ans** à compter du fait dommageable ou, s'il a été dissimulé, de sa
révélation ; **10 ans** si le fait est qualifié crime.

### 2. Le comblement de l'insuffisance d'actif (`L651-2`) — et son bouclier

**Article L651-2 (version en vigueur au 15/05/2022)** :

> « Lorsque la liquidation judiciaire d'une personne morale fait apparaître une insuffisance d'actif,
> le tribunal peut, en cas de faute de gestion ayant contribué à cette insuffisance d'actif, décider
> que le montant de cette insuffisance d'actif sera supporté, en tout ou en partie, par tous les
> dirigeants de droit ou de fait […]. **Toutefois, en cas de simple négligence du dirigeant de droit
> ou de fait dans la gestion de la personne morale, sa responsabilité au titre de l'insuffisance
> d'actif ne peut être engagée.** »

★★ **Cette phrase est le bouclier le plus utile du droit des sociétés français, et le moins connu.**
La responsabilité personnelle du dirigeant en cas de liquidation **n'est pas automatique** : la simple
négligence l'exclut par texte. La peur inverse — « si ça coule, je paie tout » — fait renoncer des
gens à entreprendre, et fait accepter des transactions qu'ils n'auraient pas dû accepter.

⚠️ Ce bouclier vise la **simple négligence**, pas la faute caractérisée, et **« dirigeant de fait »**
signifie que se cacher derrière un gérant de paille ne protège de rien. **Prescription : 3 ans** à
compter du jugement de liquidation.

### 3. ★★ La responsabilité fiscale personnelle — celle qui traverse la personne morale

**Article L267 du livre des procédures fiscales (version en vigueur au 01/01/2020)** :

> « Lorsqu'un dirigeant d'une société, d'une personne morale ou de tout autre groupement, est
> responsable des manœuvres frauduleuses ou de l'inobservation grave et répétée des obligations
> fiscales qui ont rendu impossible le recouvrement des impositions et des pénalités dues par la
> société […], ce dirigeant peut […] être déclaré solidairement responsable du paiement de ces
> impositions et pénalités par le président du tribunal judiciaire. […] Cette disposition est
> applicable à toute personne exerçant **en droit ou en fait, directement ou indirectement**, la
> direction effective de la société […]. »

★★ **La responsabilité limitée ne protège pas de l'impôt de la société.** Deux mots portent tout :
« **grave et répétée** ». Un retard isolé n'est pas visé ; une TVA jamais déclarée pendant deux ans,
si. C'est le mécanisme par lequel une dette fiscale de société atterrit sur le patrimoine personnel du
dirigeant, **sans qu'il y ait besoin d'une liquidation ni d'une fraude**.

⚠️ Les voies de recours contre la décision **n'empêchent pas** le comptable public de prendre des
mesures conservatoires.

## Conventions réglementées : minuscule en unipersonnel, et vital

Compte courant d'associé, bail consenti par le dirigeant à sa société, prestation facturée entre deux
de ses sociétés : ce sont des **conventions réglementées**.

En pluripersonnel, il y a un rapport, un vote, et l'intéressé **ne prend pas part au vote** — « ses
parts ne sont pas prises en compte pour le calcul du quorum et de la majorité » (`L223-19` al. 2).
En SAS, la convention est visée dès qu'elle est conclue avec un actionnaire disposant de plus de
**10 %** des droits de vote (`L227-10`).

★ **En unipersonnel, tout se réduit à une ligne dans le registre** :

**Article L223-19, alinéa 4** :

> « Par dérogation aux dispositions du premier alinéa, lorsque la société ne comprend qu'un seul
> associé et que la convention est conclue avec celui-ci, il en est seulement fait mention au registre
> des décisions. »

**Article L227-10, alinéa 4**, en SASU, dit la même chose pour les conventions passées avec « son
dirigeant, son associé unique ».

★ **La formalité coûte une phrase, son oubli fragilise la convention elle-même** — typiquement le
compte courant d'associé, dont on aura besoin de prouver l'existence et le montant devant un
liquidateur, un repreneur ou un vérificateur.

⚠️ **La non-approbation n'annule pas la convention** : « Les conventions non approuvées produisent
néanmoins leurs effets, à charge pour le gérant […] de supporter individuellement ou solidairement,
selon les cas, les conséquences du contrat préjudiciables à la société » (`L223-19` al. 5, et
`L227-10` al. 3 en termes voisins). ⇒ **La sanction ne tombe pas sur l'acte, elle tombe sur le
dirigeant.**

## Cession de parts et d'actions : deux mondes

### SARL / EURL — l'agrément est la règle légale

**Article L223-14, alinéa 1 (version en vigueur au 27/03/2004)** :

> « Les parts sociales ne peuvent être cédées à des tiers étrangers à la société qu'avec le
> consentement de la majorité des associés représentant au moins la moitié des parts sociales, à moins
> que les statuts prévoient une majorité plus forte. »

Le calendrier de la procédure, lui, protège le cédant :

| Étape | Délai | Effet |
|---|---|---|
| Silence de la société après notification | **3 mois** | ★ « le consentement à la cession est **réputé acquis** » |
| Après un refus, obligation d'acquérir ou faire acquérir les parts | **3 mois** | prix fixé selon `1843-4` du code civil, **frais d'expertise à la charge de la société** |
| Prolongation judiciaire de ce délai | **6 mois** maximum | à la demande du gérant |
| Délai de paiement accordé à la société qui rachète | **2 ans** maximum | sur justification, par décision de justice |

★ **Le refus d'agrément n'enferme pas l'associé** : si aucune solution n'intervient dans le délai,
« l'associé peut réaliser la cession initialement prévue » (`L223-14` al. 5). ⚠️ **Sauf s'il détient
ses parts depuis moins de deux ans** (al. 6, hors succession, liquidation de communauté ou donation au
conjoint / ascendant / descendant).

⛔ « Toute clause contraire aux dispositions du présent article est réputée non écrite » (dernier
alinéa) : on ne peut pas contractualiser un blocage plus dur que la loi.

**La forme de la cession** — `L223-17` : « La cession des parts sociales est soumise aux dispositions
de l'article L. 221-14. » Et `L221-14` (version au 03/08/2014) :

> « La cession des parts sociales doit être constatée par écrit. Elle est rendue opposable à la
> société, dans les formes prévues à l'article 1690 du code civil. Toutefois, la signification peut
> être remplacée par le dépôt d'un original de l'acte de cession au siège social contre remise par le
> gérant d'une attestation de ce dépôt. »

⚠️ **Trois niveaux distincts** : la cession est **valable** entre les parties, **opposable à la
société** après signification ou dépôt, et **opposable aux tiers** seulement après publication des
statuts modifiés au registre du commerce. Sauter la troisième étape, c'est détenir des parts que
personne n'est tenu de reconnaître.

### SAS / SASU — rien n'est verrouillé sauf par les statuts

| Clause | Texte | Ce qu'elle permet |
|---|---|---|
| Inaliénabilité | `L227-13` | interdire la cession, **10 ans maximum** |
| Agrément | `L227-14` | soumettre toute cession à l'accord de la société |
| Exclusion | `L227-16` | « prévoir qu'un associé peut être tenu de céder ses actions » |

★ **La sanction est la nullité, pas l'indemnité** — `L227-15` : « Toute cession effectuée en violation
des clauses statutaires est nulle. »

★★ **Et voici le point le plus contre-intuitif du fichier.** On répète qu'une clause d'exclusion
exige l'unanimité en SAS. **Ce n'est plus vrai.**

**Article L227-19 (version en vigueur au 21/07/2019)** :

> « Les clauses statutaires visées aux articles L. 227-13 et L. 227-17 ne peuvent être adoptées ou
> modifiées qu'à l'unanimité des associés.
>
> Les clauses statutaires mentionnées aux articles **L. 227-14 et L. 227-16** ne peuvent être adoptées
> ou modifiées **que par une décision prise collectivement par les associés dans les conditions et
> formes prévues par les statuts**. »

⇒ **L'inaliénabilité exige toujours l'unanimité ; l'agrément et l'exclusion, non.** Une clause
d'exclusion peut donc être **introduite après coup à la majorité statutaire** — c'est-à-dire imposée à
un minoritaire qui ne l'a jamais acceptée. ⚠️ **Pour un fondateur qui descend sous la majorité en
faisant entrer un associé, c'est le risque numéro un**, et il est presque toujours découvert trop
tard. ⇒ La contre-mesure se prend **avant** : verrouiller la majorité de modification des statuts.

★ Si les statuts ne disent rien du prix, il est fixé d'accord entre les parties ou, à défaut, selon
`1843-4` du code civil ; les actions rachetées par la société doivent être cédées ou annulées dans les
**6 mois** (`L227-18`).

⛔ **Le code n'ouvre expressément la clause d'exclusion que pour la SAS.** Aucun équivalent de
`L227-16` n'existe au chapitre des SARL. La validité d'une clause d'exclusion statutaire en SARL est
**discutée** et dépend de la jurisprudence : ⇒ **avocat, pas ce fichier.**

### ★★ Le coût de sortie se décide à la création

Droits d'enregistrement, **article 726 du CGI (version en vigueur au 01/01/2024)** :

| Objet cédé | Taux | Abattement |
|---|---|---|
| **Actions** de sociétés par actions (SAS, SASU, SA) non cotées | **0,1 %** | — |
| **Parts sociales** de sociétés dont le capital n'est pas divisé en actions (SARL, EURL) | **3 %** | **23 000 €** répartis au prorata du nombre de parts |
| Participations dans des personnes morales à prépondérance immobilière | **5 %** | — |

★★ **Un facteur trente entre les deux formes, payé le jour de la revente.** À valorisation égale, la
différence se chiffre en milliers d'euros. Ce paramètre n'apparaît nulle part dans les comparatifs
EURL/SASU centrés sur le régime social — ⇒ il appartient à la décision du rôle `comptable`
(`formes-juridiques.md`), et c'est ce fichier qui doit le lui rappeler.

## ★★ Perte de la moitié du capital : l'obligation que le capital symbolique rend permanente

**Article L223-42, alinéas 1 et 2 (version en vigueur au 11/03/2023)** :

> « Si, du fait de pertes constatées dans les documents comptables, les capitaux propres de la société
> deviennent inférieurs à la moitié du capital social, les associés décident, dans les **quatre mois**
> qui suivent l'approbation des comptes ayant fait apparaître cette perte s'il y a lieu à dissolution
> anticipée de la société.
>
> Si la dissolution n'est pas prononcée […], la société est tenue, au plus tard à la clôture du
> **deuxième exercice** suivant celui au cours duquel la constatation des pertes est intervenue, de
> reconstituer ses capitaux propres […] ou de réduire son capital social […]. »

⚠️ **La sanction est la dissolution judiciaire** : « À défaut par le gérant ou le commissaire aux
comptes de provoquer une décision […], tout intéressé peut demander en justice la dissolution de la
société. » Le tribunal peut accorder **6 mois** pour régulariser, et ne peut plus prononcer la
dissolution si la régularisation a eu lieu au jour où il statue.

★★ **Le raisonnement que personne ne fait** : une SASU ou une EURL créée avec un capital
**symbolique** a des capitaux propres inférieurs à la moitié de son capital **dès la première perte,
même minime**.
L'obligation de consultation dans les quatre mois n'est alors pas une hypothèse lointaine : c'est
l'état normal des premières années. ⇒ **Le capital symbolique n'est pas neutre juridiquement**, et
c'est un argument que les comparatifs de forme n'avancent jamais. *(Déduction du texte, pas citation :
à faire confirmer avant d'en tirer un acte.)*

★ La règle **ne s'applique pas** aux sociétés en sauvegarde ou redressement judiciaire, ni à celles
qui bénéficient d'un plan (`L223-42` dernier alinéa).

## Dissolution : le piège de l'associé unique personne physique

**Article 1844-5 du code civil (version en vigueur au 16/05/2001)** :

- **al. 1** : « La réunion de toutes les parts sociales en une seule main n'entraîne pas la
  dissolution de plein droit de la société. Tout intéressé peut demander cette dissolution si la
  situation n'a pas été régularisée dans le délai d'**un an**. » Le tribunal peut accorder **6 mois**
  de plus, et ne peut prononcer la dissolution si la régularisation a eu lieu.
- **al. 3** : « En cas de dissolution, celle-ci entraîne la **transmission universelle du patrimoine**
  de la société à l'associé unique, **sans qu'il y ait lieu à liquidation**. Les créanciers peuvent
  faire opposition à la dissolution dans le délai de **trente jours** à compter de la publication de
  celle-ci. »
- **al. 4** : « Les dispositions du troisième alinéa **ne sont pas applicables aux sociétés dont
  l'associé unique est une personne physique**. »

★★ **C'est l'alinéa 4 qu'il faut retenir.** La fermeture simplifiée sans liquidation — la « TUP » —
est réservée au cas où l'associé unique est une **personne morale**. Le développeur, consultant ou
artisan seul associé de sa SASU **doit passer par une liquidation complète** : nomination d'un
liquidateur, comptes de liquidation, clôture, radiation. C'est exactement l'inverse de l'intuition
(« je suis seul, ce sera simple »), et cela change le coût et le calendrier d'une fermeture.

## Ce qui reste à écrire

- **L'objet social** : le rédiger ni trop étroit ni fourre-tout, et l'articulation avec les
  `activites-reglementees.md` — c'est le point d'entrée annoncé par le `SKILL.md` et il manque encore.
- **L'augmentation de capital** : souscription en numéraire et libération des parts en SARL
  (`L223-32`, `L223-33`), droit préférentiel de souscription et son renoncement en SAS, apports en
  nature et commissaire aux apports, dilution. Seul point déjà sourcé : `L227-9` al. 2 impose que
  l'augmentation de capital en SAS soit **décidée collectivement par les associés**.
- **La liquidation ordinaire** : nomination et pouvoirs du liquidateur, comptes de liquidation,
  clôture, radiation, sort du boni — indispensable pour compléter la section ci-dessus.
- **Les majorités d'assemblée en détail** : `L223-29` (décisions ordinaires) et `L223-30`
  (modification des statuts, changement de nationalité à l'unanimité) n'ont pas été relevés verbatim
  ici ; il faut les citer avant d'en tirer un calcul de majorité.
- **Le pacte d'associés** : ce qu'il peut faire que les statuts ne peuvent pas, et l'inverse ;
  articulation avec `L227-19` et sanction de sa violation (dommages-intérêts, et non nullité).
- **Le droit de retrait et la valorisation** : `1843-4` du code civil, portée du recours à l'expert.
- **L'abus de biens sociaux** (`L241-3` en SARL, `L242-6` en SA/SAS) : non vérifié, à rédiger avec les
  peines exactes.
- **La durée de conservation du registre des décisions** : valeur non trouvée, marquée `a_verifier`.
- **Le statut du conjoint** et **les sociétés civiles** : hors périmètre pour l'instant.

## Sources

Toutes les pages ci-dessous ont été réellement consultées le **2026-08-17**.

**Code de commerce (Légifrance)**

- `L221-14` cession de parts, forme et opposabilité — <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000029329292>
- `L223-14` agrément et procédure de rachat — <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006223059/>
- `L223-17` renvoi à `L221-14` — <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006223103>
- `L223-19` conventions réglementées en SARL — <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006223120>
- `L223-22` responsabilité des gérants — <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006223141>
- `L223-25` révocation du gérant — <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006223152>
- `L223-26` approbation des comptes — <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048535091>
- `L223-31` associé unique et registre des décisions — <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000019291719>
- `L223-42` perte de la moitié du capital — <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000047292166>
- `L227-9` décisions collectives et associé unique en SAS — <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000019291762/>
- `L227-9-1` commissaire aux comptes en SAS — <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000038799598>
- `L227-10` conventions réglementées en SAS — <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000034584108>
- `L227-16` clause d'exclusion — <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006227180>
- `L227-19` majorités d'adoption des clauses — <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000038799606>
- chapitre VII, SAS (`L227-1`, `L227-5`, `L227-13`, `L227-14`, `L227-15`, `L227-18`) — <https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000005634379/LEGISCTA000006146048/>
- `L232-21` (SNC — **ne concerne pas les SARL**) — <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048535225>
- `L232-22` dépôt des comptes des SARL — <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048535223>
- section « De la publicité des comptes » (`L232-23`, `L232-25`, `L232-26`) — <https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000005634379/LEGISCTA000006161292/>
- `L232-25` confidentialité — <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000038611013>
- `L611-2` injonction sous astreinte et détection des difficultés — <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044052535>
- `L651-2` insuffisance d'actif et simple négligence — <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000045178209>
- `R123-66` inscription modificative dans le mois — <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006256603/>
- `R247-3` sanction du défaut de dépôt — <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006265627>
- `D221-5` seuils du commissaire aux comptes — <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000049216674>
- chapitre III, SARL (`R223-20`, majorités) — <https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000005634379/LEGISCTA000006146044/>
- décret n° 2019-514 du 24 mai 2019, **seuils remplacés depuis** — <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000038505937>

**Autres codes**

- Code civil, `1844-5` réunion des parts et transmission universelle — <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006444165>
- Code pénal, `131-13` montant des amendes contraventionnelles — <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006417259/>
- CGI, `726` droits d'enregistrement sur cessions de droits sociaux — <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044978804>
- Livre des procédures fiscales, `L267` responsabilité solidaire du dirigeant — <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000022175305>

**Administration**

- Dépôt des comptes annuels, seuils de confidentialité et sanctions, page **vérifiée le 11/06/2025** — <https://entreprendre.service-public.gouv.fr/vosdroits/F31214>
- SASU, registre des décisions et cession d'actions, page **du 06/02/2026** — <https://entreprendre.service-public.gouv.fr/vosdroits/F37383>
- Guichet des formalités des entreprises — <https://formalites.entreprises.gouv.fr/>

## Rappel de cadrage

Ce fichier alimente le skill `juriste`, un outil d'**aide à la décision**. Il ne remplace ni un
expert-comptable inscrit à l'Ordre, ni un avocat inscrit à un barreau.

**Trois moments où il faut s'arrêter et faire relire par un avocat**, sans exception :

1. **Avant de signer des statuts ou un pacte** — parce que `L227-5` et `L227-19` font des statuts la
   loi de la société, et qu'une clause de révocation ou d'exclusion ne se renégocie pas après.
2. **Avant une cession de parts ou d'actions** — un défaut de forme ou d'agrément se sanctionne par la
   nullité (`L227-15`), pas par un rattrapage.
3. **Dès qu'une procédure collective, une injonction du tribunal ou une mise en cause fiscale
   apparaît** — `L651-2` et `L267` du LPF engagent le patrimoine personnel, et les délais courent
   déjà.

⚠️ **Sur ce sujet, la première utilité n'est pas d'expliquer le droit : c'est de faire tenir un
calendrier et un registre.** Approbation à six mois, dépôt dans le mois, registre des décisions à
jour, inscription modificative dans le mois. Quatre obligations, aucune difficile, et ce sont elles
qui coûtent cher aux petites structures — pas les sujets nobles.
