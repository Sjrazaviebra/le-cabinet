# Cas : revenus versés par une prop firm de trading

> **État : `PARTIEL`**. **Solidement établi et sourcé** : les obligations déclaratives liées aux
> comptes à l'étranger, leurs sanctions, la catégorie fiscale « balai » des BNC, l'articulation avec
> le régime des contrats financiers, et la grille de questions de qualification.
> **Non établi, et signalé comme tel dans le texte** : la qualification retenue par l'administration
> (aucune doctrine ne la donne), le taux de change à retenir, la durée de report des déficits non
> professionnels, le numéro exact de l'annexe « comptes à l'étranger ».
> Vérifié le **2026-08-17** — Légifrance (versions en vigueur affichées jusqu'au 17/08/2026),
> service-public du **09/07/2026** et du **01/01/2026**, entreprendre.service-public du **21/02/2026**.

## ⚠️⚠️ À lire avant tout : il n'existe aucune doctrine fiscale nommant les « prop firms »

Le BOFiP ne contient pas de commentaire consacré aux sommes versées par une société de *proprietary
trading* à un particulier. Aucun texte, aucune instruction, aucune fiche officielle ne dit « les
revenus de prop firm relèvent de tel régime ».

**Conséquence directe, et elle est structurante :**

- ⛔ **Toute page — y compris celle-ci — qui annoncerait « le régime applicable est X » vous
  raconterait une histoire.** Ce qui existe, ce sont des textes généraux et une qualification à
  construire sur les faits de *votre* contrat.
- ★★ **Le seul moyen d'obtenir une réponse opposable à l'administration est un rescrit fiscal** —
  une prise de position formelle demandée par écrit sur une situation décrite précisément. C'est la
  démarche que personne ne mentionne, et c'est la seule qui transforme une opinion en protection.
  ⚠️ Les modalités et délais exacts du rescrit ne sont pas vérifiés ici : demandez-les au service des
  impôts.
- ⇒ Ce fichier fait donc autre chose : il **pose les questions qui déterminent le régime**, il
  **renvoie aux textes généraux**, et il **isole ce qui est dû quelle que soit la qualification**.
  Cette dernière partie est la plus utile, parce qu'elle est la seule certaine.

## ★★ « Pas de doctrine » ne veut pas dire « pas d'impôt »

C'est l'erreur de raisonnement la plus coûteuse du sujet. Le code général des impôts s'est fermé
lui-même cette porte, à l'article 92, 1 :

> « Sont considérés comme provenant de l'exercice d'une profession non commerciale ou comme revenus
> assimilés aux bénéfices non commerciaux, les bénéfices des professions libérales, des charges et
> offices dont les titulaires n'ont pas la qualité de commerçants et de **toutes occupations,
> exploitations lucratives et sources de profits ne se rattachant pas à une autre catégorie de
> bénéfices ou de revenus**. »

*(Version en vigueur depuis le 27 juin 2026.)*

★★ **Les BNC sont une catégorie balai.** Un profit qui ne rentre nulle part ailleurs y tombe **par
construction**. Il n'existe donc pas de revenu « hors catégorie » : l'absence de doctrine spécifique
rend la qualification incertaine, elle ne la rend pas inexistante.

## Séparer les faits avant de parler régime

Dans la plupart des modèles commercialisés, ce qui se passe réellement est le suivant :

| Ce qu'on croit | Ce qui se passe le plus souvent |
|---|---|
| « Je trade un capital confié » | le compte est **simulé** ; le solde affiché est un paramètre du logiciel |
| « J'ai gagné sur les marchés » | aucune position n'a été ouverte **en votre nom** ni **à votre risque** |
| « C'est une plus-value » | il n'y a **aucun bien cédé** par vous : sans cession, pas de plus-value |
| « La firme me reverse mes gains » | elle vous verse **une part de performance, en exécution d'un contrat** |

⇒ **Analyse** — et c'en est une, pas une certitude : lorsque le compte est simulé et que la perte
maximale du trader est plafonnée au prix payé, la somme reçue ressemble à la **rémunération d'une
activité** et non au produit d'un patrimoine. Cette lecture oriente vers un **revenu d'activité**, et
elle écarte le régime des plus-values de cession de valeurs mobilières. **Elle n'a pas été validée
par l'administration.**

★ **Le bon test n'est pas « est-ce une prop firm ? » mais « qui porte la perte au-delà du prix
payé ? »** Si votre perte maximale est le droit d'entrée, vous rendez un service. Si vous pouvez
perdre davantage, du capital propre est engagé — et l'analyse change complètement.

## Les questions qui déterminent le régime

Aucune réponse n'est utilisable avant d'avoir ces éléments. Ils sont dans le contrat, pas sur le site
commercial.

| Question | Pourquoi elle change la réponse |
|---|---|
| **Du capital propre est-il engagé ?** | non → revenu d'activité ; oui → le régime des profits sur contrats financiers entre dans le jeu |
| **Le contrat est-il un contrat de prestation ?** | il détermine si vous êtes prestataire indépendant, mandataire, ou autre chose |
| **Qui verse, et depuis quel pays ?** | revenu de source étrangère, convention applicable, et pays du compte |
| **L'activité est-elle habituelle ?** | l'habitude fait basculer vers une activité professionnelle, avec immatriculation et cotisations |
| **Y a-t-il une clause d'indépendance ?** | elle est le premier rempart contre une requalification, mais elle ne suffit pas : ce sont les faits qui comptent |

⚠️ **Le vocabulaire du contrat ne lie pas l'administration.** « Profit split », « funded account »,
« trader agreement » sont des mots de marketing anglo-saxon ; la qualification se fait sur la réalité
de la relation, pas sur son étiquette.

## Les régimes candidats, et ce que chacun impliquerait

| Régime | Quand il serait retenu | Ce qu'il impliquerait |
|---|---|---|
| **BNC professionnels** | activité exercée à titre habituel et dans un but lucratif | immatriculation, cotisations, régime micro ou déclaration contrôlée → `micro-entreprise.md`, `formes-juridiques.md` |
| **BNC non professionnels** | profits réels mais activité non exercée à titre professionnel | imposition maintenue, mais **déficits non imputables sur le revenu global** |
| **BIC** | si l'activité prenait un caractère commercial, ou sur option pour les opérations sur contrats financiers | comptabilité commerciale, autres abattements |
| **Traitements et salaires** | uniquement si la relation était requalifiée en salariat | suppose un **lien de subordination juridique permanente** |
| **Plus-values / profits sur contrats financiers** | **seulement si du capital propre est engagé** | ne concerne pas un compte simulé → `revenus-financiers.md` |

### Le point que l'on manque presque toujours : le PFU n'est pas un refuge

L'article 150 ter du code général des impôts, qui soumet les profits nets sur contrats financiers
réalisés par les personnes physiques au régime de l'article 200 A, s'ouvre par une réserve :

> « **Sous réserve des dispositions propres aux bénéfices industriels et commerciaux, aux bénéfices
> non commerciaux et aux bénéfices agricoles**, les profits nets réalisés, directement, par personne
> interposée ou par l'intermédiaire d'une fiducie, lors du dénouement ou de la cession à titre
> onéreux de contrats financiers […] »

★★ **Le régime des BNC prime sur celui-là, il ne lui est pas subordonné.** Déclarer « au forfait
financier » n'est donc pas une position neutre ou prudente : c'est déjà un choix de qualification, et
c'est celui que la réserve de l'article 150 ter peut faire tomber.

Et l'article 92, 2 range expressément dans les BNC :

> « 1° Les produits des opérations de bourse effectuées dans des conditions analogues à celles qui
> caractérisent une activité exercée par une personne se livrant à titre professionnel à ce type
> d'opérations ; »

> « 5° Les produits des opérations réalisées **à titre habituel** […] sur des contrats financiers,
> également dénommés "instruments financiers à terme" […] lorsque l'option prévue au 8° du I de
> l'article 35 n'était pas ouverte au contribuable ou lorsqu'il ne l'a pas exercée ; »

★ **Même sur capital propre, l'habitude fait sortir du régime financier.** Quelqu'un qui trade des
CFD ou des contrats à terme de façon soutenue peut relever des BNC sans jamais avoir approché une
prop firm. Le sujet « prop firm » n'est donc pas isolé : il se pose à côté d'une question de trading
personnel qu'il faut instruire séparément.

### Sur la requalification en salariat

L'article L8221-6 du code du travail pose une présomption de non-salariat pour les personnes
immatriculées, et il en donne la limite :

> « L'existence d'un contrat de travail peut toutefois être établie lorsque les personnes mentionnées
> au I fournissent directement ou par une personne interposée des prestations à un donneur d'ordre
> dans des conditions qui les placent dans un **lien de subordination juridique permanente** à
> l'égard de celui-ci. »

★ **La présomption ne protège que les personnes immatriculées.** Ne pas s'immatriculer ne met donc
personne à l'abri : cela retire une protection sans retirer une obligation.

⚠️ **Analyse, à faire trancher** : les règles d'une prop firm (limite de perte journalière,
plafond de perte totale, contrainte de régularité) ressemblent à des **limites de risque** plutôt
qu'à des directives sur l'exécution du travail. Le trader choisit ses horaires, ses instruments et
sa méthode. La subordination juridique permanente paraît donc difficile à établir — mais c'est une
appréciation de fait, elle n'est pas acquise, et personne ne l'a jugée pour ce modèle.

## Droits d'entrée, resets, échecs : c'est le choix de régime qui décide

| Situation | Sous **micro-BNC** | Sous **déclaration contrôlée** |
|---|---|---|
| Droits d'entrée, resets, add-ons, abonnements de données | **rien n'est déductible** : l'abattement forfaitaire remplace les frais réels | déductibles s'ils sont engagés pour l'activité |
| Une année de frais sans aucun versement | aucune prise en compte | produit un déficit, dont le sort dépend du caractère professionnel ou non |

★★ **Voilà la vraie conséquence chiffrable du choix de régime pour ce cas précis.** Quelqu'un qui a
payé plusieurs droits d'entrée et resets avant d'obtenir un seul versement peut se retrouver imposé
sur la somme reçue **sans que ses échecs comptent**. C'est le point où la décision se prend, et il se
prend **avant**, au moment du choix du régime — voir `micro-entreprise.md`.

⚠️ **Question à poser, pas à trancher** : le premier versement inclut souvent le **remboursement du
droit d'entrée**. Un remboursement de frais n'est pas nécessairement un revenu. La réponse change
l'assiette, et elle dépend de la rédaction du contrat.

⚠️ **Déficits en BNC non professionnels** : non imputables sur le revenu global, reportables sur les
seuls bénéfices de même nature des années suivantes — **la limite de durée n'a pas été vérifiée dans
cette passe** et est marquée `a_verifier`. À lire au texte : article 156, I, 2° du code général des
impôts.

## ★★ Ce qui est dû quelle que soit la qualification

C'est la partie certaine du fichier, et la plus rentable à lire.

### Déclarer les comptes ouverts, détenus, utilisés ou clos à l'étranger

L'article 1649 A du code général des impôts impose de déclarer, avec la déclaration de revenus,
« les références des comptes ouverts, détenus, utilisés ou clos à l'étranger ». L'article 344 A de
l'annexe III précise le champ, et c'est là que se trouve le piège :

> « comptes ouverts auprès de **toute personne de droit privé ou public qui reçoit habituellement en
> dépôt des valeurs mobilières, titres ou fonds** »

> « Un compte est réputé avoir été **utilisé** […] dès lors que celle-ci a effectué **au moins une
> opération de crédit ou de débit** pendant la période visée par la déclaration »

★★ **Une seule opération suffit.** Un versement reçu sur un portefeuille en ligne étranger, même
vidé et fermé le lendemain, rend ce compte déclarable pour l'année. Sont visés les comptes bancaires,
les **comptes de paiement et portefeuilles électroniques**, et les **comptes d'actifs numériques**
ouverts sur une plateforme étrangère.

★★ **Et la dispense que tout le monde croit avoir ne s'applique pas ici.** Elle suppose **trois**
conditions cumulatives :

> « Il sert à payer des achats en ligne ou encaisser des ventes de biens / Il est lié à un compte que
> vous avez déjà en France / Vous avez encaissé sur ce compte une somme ne dépassant pas **10 000 €**
> dans l'année »

⇒ **Un versement de prop firm n'est pas l'encaissement d'une vente de biens.** La condition tombe, et
avec elle la dispense — indépendamment du montant. C'est exactement le raisonnement faux qui expose
des gens qui pensaient être en règle parce que « les sommes sont petites ».

### Les sanctions, et le fait qu'elles se cumulent

| Type de compte | Amende | Cas aggravé |
|---|---|---|
| Compte bancaire, de paiement, portefeuille électronique | **1 500 €** par compte non déclaré | **10 000 €** par compte si l'État n'a pas conclu de convention d'assistance administrative avec la France |
| Compte d'actifs numériques | **750 €** par compte non déclaré | **1 500 €** par compte si la valeur du compte dépasse **50 000 €** |

**Et dans les deux cas, en plus : « Majoration de 80 % des droits dus ».**

⚠️ **L'amende est par compte et par année**, et elle frappe le seul manquement déclaratif : elle est
due **même si aucun impôt n'était dû** et même si le compte est à zéro. Pour un trader qui a utilisé
successivement un prestataire de paiement, une banque en ligne étrangère et une plateforme
d'échange, l'addition se fait par compte.

★ **Une croyance fausse à démonter au passage** : l'amende proportionnelle de **5 %** du solde
créditeur au-delà de **50 000 €** cumulés, que l'on trouve encore citée en ligne, **a été déclarée
contraire à la Constitution** par la décision n° 2016-554 QPC du 22 juillet 2016, pour disproportion
manifeste, avec effet immédiat y compris sur les amendes non encore définitives. Elle ne figure plus
dans la version en vigueur de l'article 1736, IV. ⚠️ **Ne pas la confondre** avec le seuil de
50 000 € des comptes d'actifs numériques ci-dessus, qui est un dispositif distinct et bien en
vigueur.

### Résidence, conventions, change

- **Le domicile fiscal en France est établi si UN SEUL des quatre critères est rempli** : foyer,
  séjour en France pendant au moins **183 jours** dans l'année, activité principale, ou centre des
  intérêts économiques. ★ Un trader qui voyage beaucoup ne sort donc pas de la résidence fiscale
  française par le seul fait d'être moins de la moitié de l'année en France.
- ⚠️ « Une convention internationale conclue entre la France et un pays étranger peut prévoir des
  règles différentes. » La convention ne s'ajoute pas au droit interne : **elle le corrige**. Il faut
  lire celle du pays payeur, et non raisonner en général.
- ⚠️ **Non vérifié, et cherché** : le principe d'imposition des résidents sur l'ensemble de leurs
  revenus, de source française comme étrangère, à lire à l'article 4 A du code général des impôts.
  La fiche officielle sur le domicile fiscal ne l'énonce pas explicitement — je ne l'affirme donc
  pas ici comme un fait.
- ⚠️ **Non vérifié, et cherché** : **le taux de change à retenir** pour convertir un versement reçu
  en devise. Aucune page officielle ne l'a confirmé dans cette passe ; la valeur est en
  `a_verifier`. ⇒ **Posez la question au service des impôts, et conservez par écrit la source du
  cours retenu, date par date.** Un cours choisi après coup, sans trace, est le genre de détail qui
  décrédibilise un dossier entier.

### Si la qualification retenue est celle des BNC en déclaration contrôlée

Les formulaires sont la déclaration de résultats **2035** avec ses annexes **2035-A** et **2035-B**,
le résultat étant reporté sur la déclaration complémentaire **2042-C-PRO**. ⚠️ Déposer ces
formulaires **ne crée pas** la qualification : cela la présuppose.

## La TVA : l'angle qu'on oublie complètement

Si l'activité est qualifiée de prestation de services rendue à une société assujettie établie hors de
France, la TVA française n'est pas due, mais **des obligations de forme apparaissent**. Le détail des
mentions, du numéro de TVA intracommunautaire et de la déclaration européenne de services est dans
`tva.md` — **lisez-le, le délai de dépôt de cette déclaration est très court.**

Le point propre à ce cas :

- **Firme établie hors UE** (cas le plus fréquent) → facture sans TVA, mention
  « TVA non applicable – art. 259-1 du CGI », **et pas de déclaration européenne de services**.
- **Firme établie dans l'UE** → mention « Autoliquidation » **et** déclaration européenne de
  services. ⚠️ Le siège réel n'est pas toujours celui affiché sur le site : c'est l'entité qui
  **facture et paie** qui compte.

⚠️ **Question préalable, non tranchée** : y a-t-il même une prestation de services au sens de la TVA
lorsque la rémunération est une part de performance sur un compte simulé ? Cela se discute, et cela
se discute avec quelqu'un d'assuré.

## ⛔ Ce que ce fichier ne fait pas, et ne fera pas

⛔ **Aucune stratégie de trading, aucun choix d'instrument, aucun placement.** Recommander un
placement adapté à une situation personnelle est du **conseil en investissement** : une activité
réglementée, soumise à agrément. → le rôle `juriste`, fichier `activites-reglementees.md`.

⛔ **Aucune réponse à « jusqu'où puis-je aller sans déclarer ».** La question utile est « qu'est-ce
que je dois faire », et sa réponse est en partie certaine, ci-dessus.

## ★ Ce qu'il faut demander à un professionnel, et avec quels éléments

Un expert-comptable ou un avocat fiscaliste peut trancher la qualification et, si nécessaire, rédiger
la demande de rescrit. Il ne pourra rien faire d'utile sans ces pièces. **Réunissez-les avant le
rendez-vous** :

**Le contrat et son environnement**

1. Le contrat signé **en entier**, dans la version en vigueur **à la date de chaque versement** —
   pas la version actuelle du site.
2. Les conditions générales et le règlement de risque (limites de perte, contrainte de régularité).
3. Toute clause d'indépendance, de non-salariat, ou de droit applicable et de juridiction.
4. La preuve de ce que le compte est **simulé** ou **réel** : cette pièce commande tout le reste.

**L'entité payeuse**

5. Son nom exact, son pays d'établissement, son numéro d'immatriculation — **tels qu'ils figurent sur
   les justificatifs de paiement**, et non tels qu'affichés en page d'accueil.
6. Le nom du prestataire de paiement utilisé et le pays de l'établissement teneur du compte.

**L'argent**

7. Le relevé de **tous** les versements reçus : date, devise, montant brut, frais retenus, montant
   net.
8. Le cours de change appliqué à chaque versement, **avec la source du cours**.
9. Toutes les dépenses : droits d'entrée, resets, add-ons, abonnements de données, serveur, logiciels
   — avec les factures, y compris celles des tentatives échouées.

**Les comptes**

10. La liste de **tous** les comptes étrangers ouverts, détenus, utilisés ou clos, année par année :
    banque, prestataire de paiement, portefeuille électronique, plateforme d'actifs numériques,
    compte chez un courtier. Avec, pour chacun, dates d'ouverture et de clôture, et l'indication
    qu'au moins une opération y a eu lieu.

**Vous**

11. Votre situation par ailleurs : salarié, allocations, micro-entreprise déjà existante, autre
    activité — beaucoup de règles se calculent sur le foyer.
12. Si vous tradez **aussi** votre capital propre : les relevés du courtier personnel, **présentés
    séparément**. Mélanger les deux est le meilleur moyen de faire basculer l'ensemble.

**Les questions à poser, dans cet ordre** : quelle catégorie ? professionnel ou non ? faut-il
s'immatriculer, et à partir de quand ? quel régime, au vu des frais réels ? y a-t-il matière à
rescrit ? et quels comptes étrangers dois-je régulariser, pour quelles années ?

## Ce qui reste à écrire

- ⭐ **Le plus utile** : la procédure de **rescrit fiscal** — quelle forme, à qui, quels délais, et
  ce que vaut le silence de l'administration. C'est le cœur pratique du sujet et il manque.
- ⭐ **Le second plus utile** : le **taux de change** à retenir pour les revenus encaissés en devise,
  et la doctrine applicable. Rien n'a pu être confirmé ici.
- La **régularisation du passé** : comment déclarer des comptes et des revenus d'années antérieures,
  et ce que la démarche spontanée change aux sanctions.
- Le **numéro exact** de l'annexe « comptes ouverts, utilisés ou clos à l'étranger » et ses règles de
  dépôt, à lire sur `impots.gouv.fr`.
- La **durée de report** des déficits BNC non professionnels (article 156, I, 2°).
- Le **basculement en activité professionnelle** : le moment exact, l'immatriculation, les
  cotisations, et l'articulation avec les allocations → `chomage-et-creation.md`.
- Les **retenues à la source** pratiquées par certaines firmes et leur imputation, ou non, en France.
- Le cas des firmes qui routent des ordres **réels** sur des sous-comptes : c'est le seul modèle où
  la question des plus-values se pose vraiment.

## Sources

- Code général des impôts, article 92 (définition des BNC, catégorie balai) —
  <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044983291>
- Code général des impôts, article 150 ter (profits sur contrats financiers) —
  <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037526716>
- Code général des impôts, article 1649 A (déclaration des comptes à l'étranger) —
  <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000045764822>
- Code général des impôts, article 1736 (amendes) —
  <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051215709>
- Annexe III au code général des impôts, articles 344 A à 344 C (comptes concernés, compte
  « utilisé ») — <https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006162316/>
- Décret n° 2018-1267 du 26 décembre 2018 (comptes détenus à l'étranger) —
  <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000037865357>
- Conseil constitutionnel, décision n° 2016-554 QPC du 22 juillet 2016 (censure de l'amende
  proportionnelle) — <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000032929126>
- Code du travail, article L8221-6 (présomption de non-salariat) —
  <https://code.travail.gouv.fr/code-du-travail/l8221-6>
- Déclaration des comptes ouverts à l'étranger, sanctions et dispense —
  <https://www.service-public.gouv.fr/particuliers/vosdroits/F34342>
- Domicile fiscal et conventions internationales —
  <https://www.service-public.gouv.fr/particuliers/vosdroits/F62>
- Régime réel d'imposition des BNC et formulaires —
  <https://entreprendre.service-public.gouv.fr/vosdroits/F32105>

## Rappel de cadrage

Ce fichier alimente le skill `comptable`, un outil d'**aide à la décision**. Il ne remplace ni un
expert-comptable inscrit à l'Ordre, ni un avocat inscrit à un barreau, ni le service des impôts.

⚠️ **Sur ce sujet plus que sur tout autre** : il n'existe pas de doctrine officielle, et ce fichier
n'en fabrique pas. Ce qu'il affirme, ce sont les **obligations déclaratives**, qui sont vérifiées et
qui ne dépendent d'aucune qualification. Ce qu'il ne fait que **cadrer**, c'est la qualification
elle-même — et là, seule une prise de position écrite de l'administration, ou un professionnel
assuré, engage quelqu'un d'autre que vous.
