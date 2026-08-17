# Les leviers légaux de réduction d'impôt et de charges — la carte

> **État : `PARTIEL`** — **`RÉDIGÉ`** pour la règle de lecture, la carte des leviers côté entreprise et
> côté particulier, les leviers gratuits, les fausses bonnes idées et les deux lignes rouges.
> **`PARTIEL`** sur deux points nommés plus bas : les **crédits d'impôt** d'une petite structure ne sont
> traités par **aucun fichier du dépôt** et ne sont ici que pointés (dont un que j'ai vérifié
> **supprimé**) ; les **exonérations de zone** ne le sont que pour le zonage **ZFRR**.
> Vérifié le **2026-08-17**. Pages que j'ai fetchées moi-même : Légifrance (CGI 1728 et 1727, versions
> en vigueur affichées), fiches `entreprendre.service-public.gouv.fr` du **21/02/2026**, page
> `service-public.gouv.fr` du **15/04/2026** — toutes de moins de six mois.
> ⚠️ **Tout le reste est relayé** : chaque valeur citée par renvoi garde la source et la
> `date_verifiee` **du fichier qui la porte**, pas de celui-ci.

## Ce que ce fichier est, et ce qu'il n'est pas

★★ **C'est une CARTE, pas un montage.** Il liste les leviers **légaux**, leurs conditions et leurs
pièges, et **renvoie au fichier qui traite chacun en détail**. Il ne recalcule rien et ne conclut
jamais « faites ceci ».

**Conséquence directe sur sa forme** : il cite **le moins de chiffres possible**, et c'est volontaire.
Un taux, un seuil ou un plafond recopié d'un fichier à l'autre est un taux qui se périmera **sans que
personne ne s'en aperçoive**, parce que la mise à jour se fera dans le fichier d'origine. **Ici on
nomme le levier et on dit où lire sa valeur.** Quand un chiffre apparaît quand même, c'est qu'il est
le levier lui-même — pas son illustration.

⚠️ **Une carte a un mode d'échec propre, et il faut le dire** : elle peut envoyer vers un levier qui
n'existe plus. C'est arrivé en écrivant ce fichier, voir le crédit d'impôt formation du dirigeant plus
bas. ⇒ **Le renvoi vaut mieux que la mémoire, et la source vaut mieux que le renvoi.**

## ★★ La règle de lecture : DÉCALER n'est pas SUPPRIMER

**C'est l'erreur la plus commune, et ce fichier existe d'abord pour l'empêcher.** Beaucoup de
dispositifs présentés comme des économies d'impôt ne réduisent pas l'impôt : ils **déplacent le moment
où il est dû**. L'argent n'est pas économisé, il est **emprunté à l'État**, et la question devient
*quand* et *à quel taux* on le rembourse.

| Levier | Ce qu'il fait vraiment | Où l'impôt revient | → le détail |
|---|---|---|---|
| **PER**, versements déduits | déduit à l'entrée | **à la sortie**, sur le capital ou la rente | rôle `impots`, `epargne-retraite-per.md` |
| **Amortissement en meublé au réel** | réduit le résultat imposable | **à la revente** : les amortissements déduits **minorent le prix d'acquisition** retenu pour la plus-value | rôle `impots`, `immobilier-fiscal.md` |
| **Amortissement en location nue** (dispositif récent) | déduit des revenus fonciers | **probablement à la revente**, même mécanique — ⚠️ **rapprochement de sources, non acquis** | rôle `impots`, `immobilier-fiscal.md` |
| **Déficit foncier** | imputation **réelle** sur le revenu global | nulle part — **mais l'avantage est repris si la location cesse trop tôt** | rôle `impots`, `immobilier-fiscal.md` |
| **Report du déficit** d'entreprise | efface un bénéfice futur | **sur les exercices suivants**, et le réservoir peut se perdre | rôle `comptable`, `cloture-et-liasse.md` |
| **Étalement d'une dette** fiscale ou sociale | décale la **trésorerie** | intégralement, et **les majorations restent** — leur remise est une demande distincte | `difficultes-et-mediation.md` |

★★ **Le corollaire qui condamne tout un raisonnement** : un décalage n'est un gain que si le taux
auquel on paiera plus tard est **plus bas** que celui qu'on évite aujourd'hui. C'est donc un **pari sur
sa situation future**, pas une économie constatée. Et ce pari ne se tient pas dans les deux sens : pour
quelqu'un dont les revenus vont monter, le décalage peut coûter plus qu'il ne rapporte.

★ **Les trois questions à poser à n'importe quel levier**, avant toute autre :

1. **Est-ce que l'impôt disparaît, ou est-ce qu'il revient ?** Et s'il revient, **quand et sur quelle
   base** — sur le gain, ou sur le capital entier ?
2. **À quoi est-ce que ça m'engage ?** Une durée de détention, un engagement de location, une
   affectation, une immobilisation de trésorerie.
3. **Qu'est-ce que je perds si ma situation change ?** Un déménagement, une revente, une séparation, un
   changement de régime — c'est là que les reprises se déclenchent.

⚠️ **Et une distinction que tout le monde mélange** : une **réduction d'impôt** ne s'impute que sur
l'impôt dû et se perd s'il n'y en a pas ; un **crédit d'impôt** est **restitué** même sans impôt ; une
**charge déductible** ne vaut que le taux marginal de celui qui la déduit. Trois mécaniques, trois
valeurs très différentes pour un même euro dépensé. → rôle `impots`, `impot-revenu.md`.

## Côté entreprise — la carte

| Levier | Ce qu'il faut remplir | ⚠️ Le piège qui le rend inopérant | → le détail |
|---|---|---|---|
| **Choix du régime et de la forme** | le paramètre **contraint** du projet décide (régime social, IR/IS, forfait ou réel, avenir) | ⚠️ **le moins réversible de tous** : on ne « transforme » pas une entreprise individuelle en société, on **crée** la société et on **ferme** l'entreprise individuelle | rôle `comptable`, `formes-juridiques.md` |
| **Abattement forfaitaire du régime micro** | rester sous les seuils de chiffre d'affaires | ⚠️ **c'est un forfait, pas un remboursement** : si les charges réelles le dépassent, on paie de l'impôt sur de l'argent non gagné. ★ Et on cotise sur le **chiffre d'affaires**, pas sur le bénéfice — **un mois à perte coûte des cotisations** | rôle `comptable`, `micro-entreprise.md` |
| **Versement libératoire** de l'impôt | un plafond de revenu fiscal de référence du foyer | ⚠️ **il se paie dès le premier euro**, alors que le barème comporte une **première tranche non imposée** ⇒ un foyer peu imposé **paie plus** avec l'option | rôle `comptable`, `micro-entreprise.md` |
| **Franchise en base de TVA** | rester sous les seuils **propres à la TVA** | ★★ **ce ne sont PAS les seuils de la micro** : on devient redevable **bien avant** le plafond du régime micro. Et le dépassement du **seuil majoré** fait perdre la franchise **dès le jour du franchissement** ⇒ des mois facturés sans TVA qu'il faut sortir de sa marge | rôle `comptable`, `tva.md` |
| **ACRE** — exonération de cotisations | une **demande à l'Urssaf**, dans un délai court après l'ouverture d'activité | ★★ **elle n'est pas automatique et le délai est bref** — passé lui, l'ACRE est perdue, **et l'ARCE avec elle** puisqu'elle en dépend. ⚠️ Le **taux dépend de la date de création** | rôle `comptable`, `chomage-et-creation.md` |
| **Exonération de zone** (ZFRR, ZFRR+, BER, ZFU-TE, BUD) | conditions **de fond**, cumulatives — voir ci-dessous | ⚠️ **l'adresse ne suffit pas** : c'est l'implantation **réelle** qui est exigée | ⛔ aucun fichier du dépôt — fiches officielles en `## Sources` |
| **Crédits d'impôt** (recherche, innovation) | agrément, nature des dépenses, déclaration spéciale | ⛔ **non traités par le dépôt**, et l'un de ceux que le périmètre citait **n'existe plus** (voir ci-dessous) | ⛔ à lire sur les fiches officielles |
| **Choix de la date de clôture** | libre, sauf deux exceptions sèches | ★ **le premier exercice peut être allongé**, et c'est la marge de manœuvre la moins utilisée. ⚠️ Mais le premier résultat imposable porte alors sur une période plus longue | rôle `comptable`, `cloture-et-liasse.md` |
| **Charges déductibles** | quatre conditions **cumulatives** | ★ **c'est la dernière qui fait perdre les dossiers** : *être justifiée par une facture ou une quittance*. Une dépense professionnelle réelle **sans pièce n'est pas une charge**. ⚠️ Et une **immobilisation ne se déduit pas**, elle s'amortit | rôle `comptable`, `comptabilite-generale.md` |
| **Report du déficit** | régime réel | ⚠️ un déficit **reporté sur une seule catégorie de revenu** se perd si cette catégorie disparaît | rôle `comptable`, `cloture-et-liasse.md` |

### Les exonérations de zone : les conditions de fond, et pourquoi l'adresse ne suffit pas

Le zonage rural en vigueur est la **zone France ruralités revitalisation (ZFRR)**, avec un cran
renforcé **ZFRR+**. Coexistent aussi le **BER**, la **ZFU-TE** et le **BUD**. **Une commune se vérifie
sur un outil officiel** — le lien est en `## Sources` : c'est la première chose à faire, avant tout
raisonnement fiscal.

**Conditions de fond, verbatim de la fiche ZFRR du 21/02/2026** :

- **implantation réelle** : « *la direction effective de l'entreprise, l'ensemble de son activité et de
  ses moyens d'exploitation, humains et matériels, doit être implantée dans la ZFRR* » ;
- **nature de l'activité** : « *activité industrielle, commerciale, artisanale ou libérale* » ;
- **effectif** : « *employer moins de 11 salariés* » ;
- **régime d'imposition** : régime réel, ou déclaration contrôlée pour les activités libérales ;
- **exclusion** : « *Activités bénéficiant ou ayant bénéficié, durant une ou plusieurs des [...] années
  précédant l'année de la création ou de la reprise, d'autres dispositifs d'allégements fiscaux* ».

★★ **La condition d'implantation est celle qui tue le montage** : ce n'est pas une adresse de
domiciliation, c'est **la direction effective ET l'ensemble des moyens d'exploitation**. Une boîte aux
lettres en zone avec l'activité ailleurs ne remplit pas le texte. ⚠️ **Un plafond de chiffre d'affaires
réalisé hors de la zone existe également** : je ne le chiffre pas ici, il est sur la fiche.

⚠️ **L'exclusion pour antériorité d'un autre allégement est le piège silencieux** : avoir déjà
bénéficié d'un dispositif d'aide ferme la porte. C'est exactement le cas de quelqu'un qui a eu l'ACRE
ou une exonération de création — **à vérifier avant de compter dessus.**

### ⚠️ Le crédit d'impôt formation du dirigeant n'existe plus

**Verbatim, `entreprendre.service-public.gouv.fr`, page du 21/02/2026** :

> « Non, il n'est plus possible de bénéficier du crédit d'impôt pour la formation des dirigeants
> d'entreprise, pour les formations réalisées après le 31 décembre 2024. »

★★ **C'est la trouvaille la plus utile de cette section, et elle est négative.** Ce crédit est encore
cité partout comme un levier vivant, y compris dans le périmètre de ce fichier. **Une carte qui y
envoie fait perdre du temps et de l'argent à son lecteur.** ⇒ Sur les crédits d'impôt, ce fichier
donne les **fiches officielles** et rien d'autre : ce sont des dispositifs à durée de vie courte, et
c'est précisément la catégorie où il ne faut jamais parler de mémoire.

## Côté particulier — la carte

| Levier | Ce qu'il faut remplir | ⚠️ Le piège qui le rend inopérant | → le détail |
|---|---|---|---|
| **PER** — versements déductibles | un plafond individuel, lisible **sur l'avis d'imposition** | ★★ **le versement en trop est perdu, définitivement** : c'est le **plafond** qui se reporte, jamais le versement. ⚠️ Et le PER **décale** l'impôt (voir la règle de lecture) | rôle `impots`, `epargne-retraite-per.md` |
| **Mutualisation du plafond PER entre conjoints** | **une case à cocher** | ★★ **un droit qui se perd faute d'être connu** : sans la case, le plafond inutilisé du conjoint reste inutilisé | rôle `impots`, `epargne-retraite-per.md` |
| **Déficit foncier** | des travaux, pas un crédit | ★ **les intérêts d'emprunt sont EXCLUS** de l'imputation sur le revenu global. ★★ Et l'imputation **engage à louer** : cesser de louer trop tôt — vendre, reprendre le bien, **ou le passer en meublé** — **fait reprendre la déduction** | rôle `impots`, `immobilier-fiscal.md` |
| **Régime réel en meublé** et amortissement | une comptabilité | ★★ **les amortissements déduits minorent le prix d'acquisition à la revente** ⇒ report, pas exonération. ⚠️ Et le déficit d'un loueur **non professionnel** ne s'impute **pas** sur le revenu global | rôle `impots`, `immobilier-fiscal.md` |
| **Dons**, **emploi à domicile**, **garde d'enfants** | des justificatifs, et **la bonne case** | ★ **le véhicule est l'annexe `2042-RICI`** — sans elle, l'avantage n'est pas demandé. ⛔ Les **conditions** de chacun ne sont **pas encore écrites** dans le dépôt | rôle `impots`, `declaration-annuelle.md` |
| **L'annexe `2042-RICI`** | la remplir | ★★ **c'est l'annexe la plus oubliée, et c'est elle qui fait baisser l'impôt.** À qui demande « comment payer moins », la première question utile n'est pas un montage : c'est *« avez-vous rempli le RICI ? »* | rôle `impots`, `declaration-annuelle.md` |
| **Rattachement d'un enfant majeur** | conditions d'âge et de situation | ⚠️ **ce n'est pas une évidence, c'est un calcul comparatif** : le rattachement s'oppose à la déduction d'une pension, et l'avantage de parts est **plafonné**. ⛔ Le calcul n'est pas encore écrit dans le dépôt | rôle `impots`, `impot-revenu.md` |
| **Arbitrage PFU / barème** | **une case unique**, sur la déclaration | ★★ **l'option est GLOBALE** : tous les revenus mobiliers **et** toutes les plus-values mobilières du **foyer entier**, ensemble. On ne choisit pas placement par placement. ⚠️ Expresse (sans la case, c'est le PFU) et **annuelle** | rôle `impots`, `revenus-financiers.md` |
| **Comprendre son taux avant de refuser un revenu** | rien — juste ne pas se tromper | ★★ **passer une borne ne réimpose jamais ce qui est en dessous.** Le **taux marginal** sert à arbitrer *une* décision, le **taux moyen** à savoir ce qu'on paie | rôle `impots`, `impot-revenu.md` |

⚠️ **Sur les enveloppes d'épargne, ce fichier s'arrête à la mécanique fiscale.** L'exonération d'un
plan, la durée qui la déclenche, le retrait qui la casse : c'est `revenus-financiers.md` du rôle
`impots`. **La pédagogie sur les placements eux-mêmes vit dans le rôle `patrimoine`.**

## ★ Les leviers qui ne coûtent rien et qu'on oublie

**C'est la section la plus utile de ce fichier, et personne ne l'écrit.** Aucun de ces leviers ne
demande d'argent, de montage ni de conseil : ils demandent **de savoir qu'ils existent et de respecter
un calendrier**. Ils s'adressent à quelqu'un qui pense qu'il est déjà trop tard — et c'est presque
toujours faux.

### ★★ Déposer, même très en retard : la fenêtre après la mise en demeure

**CGI article 1728, version en vigueur affichée au 21/02/2026, verbatim** :

> « **10 %** en l'absence de mise en demeure ou en cas de dépôt dans les trente jours suivant la
> réception d'une mise en demeure »
> « **40 %** lorsque la déclaration n'a pas été déposée dans les trente jours suivant la réception
> d'une mise en demeure »

★★ **La majoration quadruple au seul franchissement de la fenêtre de 30 jours.** Déposer, même très en
retard, même imparfait, **dès réception de la mise en demeure**, divise la sanction par quatre. **Et le
réflexe naturel est exactement l'inverse** : on attend d'avoir un dossier propre — c'est-à-dire qu'on
paie quatre fois plus pour un dossier plus soigné.

★ **Le délai court à compter de la RÉCEPTION**, pas de l'envoi ⇒ **l'accusé de réception est une pièce
à conserver.** ⚠️ Et déposer dans la fenêtre **ne supprime pas l'intérêt de retard**, qui se cumule
avec la majoration : ce sont deux choses distinctes. → rôle `comptable`, `cloture-et-liasse.md` ; rôle
`impots`, `reclamation-et-controle.md`.

### ★★ Rectifier de soi-même, avant tout courrier

**CGI article 1727 V, version en vigueur affichée du 16/02/2025 au 01/01/2027, verbatim** :

> « Le montant dû au titre de l'intérêt de retard est **réduit de 50 %** en cas de dépôt spontané par
> le contribuable, avant l'expiration du délai prévu pour l'exercice par l'administration de son droit
> de reprise, d'une déclaration rectificative à condition, d'une part, que la régularisation ne
> concerne pas une infraction exclusive de bonne foi et, d'autre part, que la déclaration soit
> accompagnée du paiement des droits simples [...] »

⚠️ **Les deux conditions sont dans le texte** : bonne foi, **et** le paiement qui accompagne la
déclaration. Une rectification déposée sans payer ne produit pas la réduction.

### Les autres, en une ligne chacun

| Le levier gratuit | Ce qu'il produit | ⚠️ La condition ou le piège | → le détail |
|---|---|---|---|
| **La mention expresse** — signaler son doute **au moment** de déclarer | **annule l'intérêt de retard** sur le point signalé | ⚠️ il faut **remplir la case ET joindre la note** ; se taire ne protège pas | rôle `impots`, `reclamation-et-controle.md` |
| **Corriger en ligne** une déclaration déjà déposée | gratuit, sans courrier, **sans justifier** | ★ le service traite les **chiffres**, **pas l'état civil** : mariage, PACS, décès, adresse **ne passent pas** par lui | rôle `impots`, `declaration-annuelle.md` |
| **Réclamer dans le délai** | fait rejuger l'imposition | ★ **le point de départ n'est pas celui qu'on croit** — un troisième point de départ sauve des dossiers qu'on croyait fermés. ⚠️ Les **impôts locaux** ont un délai **plus court** | rôle `impots`, `reclamation-et-controle.md` |
| **Demander le sursis de paiement** | suspend l'exigibilité | ⛔ **la réclamation seule ne suspend RIEN**, et le sursis se demande **DANS** la réclamation, pas après | rôle `impots`, `reclamation-et-controle.md` |
| **Le recours gracieux** sur les pénalités | remise possible | ★ **les pénalités sont graciables même quand les droits ne le sont pas**. ⛔ Mais il **ne conserve pas** le délai contentieux : le faire **en plus**, pas **à la place** | rôle `impots`, `reclamation-et-controle.md` |
| **Répondre à une proposition de rectification** | c'est **le seul moment** où le dossier se discute utilement | ★★ **la prorogation du délai de réponse est de DROIT** — rien à justifier, un courrier suffit. ⚠️ Mais la demande doit être **reçue** avant l'expiration | rôle `impots`, `reclamation-et-controle.md` |
| **La dispense de première infraction** (amendes documentaires) | annule l'amende | ⚠️ **personne ne la propose au guichet** : elle se **demande** | rôle `comptable`, `cloture-et-liasse.md` |
| **Demander un étalement AVANT l'échéance** — **CCSF** (fiscal **et** social en un dossier), Urssaf, SIE | **gratuit et confidentiel**, aucune publication | ★★ **les conditions se jouent avant** : être à jour du **dépôt** des déclarations et du **paiement de la part salariale** ⇒ **déclarer quand même, et payer la part salariale d'abord.** ⚠️ Le SIE peut exiger des **garanties**, voire une **caution du dirigeant** | `difficultes-et-mediation.md`, puis `garanties-et-caution-dirigeant.md` |
| **Saisir la médiation du crédit** | **gratuite et confidentielle** ; les concours sont **maintenus pendant la médiation** | ⏱️ **un préavis court** : saisir avant la fin du délai, pas après | `difficultes-et-mediation.md`, `credit-et-rupture.md` |
| **Le dégrèvement de la majoration de taxe d'habitation** sur une résidence secondaire en zone tendue | annule la majoration communale | ⛔ **« sur réclamation »** — **jamais automatique**. Le cas du pied-à-terre professionnel est très répandu et presque jamais réclamé : l'avis arrive majoré, on le croit normal, le délai passe | rôle `impots`, `impots-locaux-et-ifi.md` |
| **Ne pas payer un « compte professionnel »** quand un compte **dédié** suffit | **économie directe et récurrente** | ★★ le texte exige un compte **dédié**, pas un compte « pro » facturé — la banque vend le second en laissant croire qu'il est obligatoire | rôle `comptable`, `comptabilite-generale.md`, `micro-entreprise.md` |
| **Vérifier son relevé de carrière** et faire corriger | des trimestres et des droits qui manquent | ⚠️ **un relevé erroné produit une estimation erronée sans le signaler** — le simulateur ne détecte rien | rôle `patrimoine`, `retraite-et-long-terme.md` |
| **Demander l'attestation de vigilance** de son sous-traitant | évite la **solidarité financière** du donneur d'ordre | ★★ **la demander UNE FOIS à la signature ne vaut rien** : le texte impose de la **renouveler périodiquement** jusqu'à la fin du contrat. ⛔ Et **un PDF non authentifié ne protège pas** — l'authenticité se vérifie auprès de l'organisme de recouvrement | rôle `comptable`, `paie-et-embauche.md` |
| **Sécuriser à l'avance** : rescrit fiscal, droit au contrôle | une position **opposable** à l'administration | ⚠️ **le silence ne vaut pas accord** : ne le supposez jamais | rôle `impots`, `reclamation-et-controle.md` |
| **L'annexe `2042-RICI`** | fait exister les réductions et crédits d'impôt | ★ **l'annexe la plus oubliée** | rôle `impots`, `declaration-annuelle.md` |

★★ **Le fil commun de toute cette section** : **demander tôt coûte moins cher que subir tard**, et
**déposer un dossier imparfait à l'heure vaut mieux qu'un dossier parfait en retard**. Les deux
énoncés sont contre-intuitifs, et ce sont les deux plus rentables du fichier.

## ★ Les fausses bonnes idées

### Celles qui font perdre un droit

| L'idée | Ce qu'elle coûte réellement | → le détail |
|---|---|---|
| **Créer d'abord, demander l'ACRE plus tard** | la fenêtre de demande est courte ; hors délai, l'ACRE est perdue — **et l'ARCE avec elle** | rôle `comptable`, `chomage-et-creation.md` |
| **Prendre l'ARCE « parce que c'est un capital »** | on **échange un revenu plancher mensuel** contre une somme qu'on aurait touchée de toute façon. ⚠️ Et l'ARCE supporte la CSG-CRDS | rôle `comptable`, `chomage-et-creation.md` |
| **Ne pas déclarer un mois sans encaissement** pendant l'actualisation | ce n'est pas un oubli, c'est une **fausse déclaration** : récupération des sommes et sanction possible | rôle `comptable`, `chomage-et-creation.md` |
| **Verser au-delà de son plafond PER** | l'excédent **n'est pas reporté, il est perdu** | rôle `impots`, `epargne-retraite-per.md` |
| **Ne pas cocher la mutualisation du plafond du couple** | le plafond inutilisé du conjoint est **perdu** | rôle `impots`, `epargne-retraite-per.md` |
| **Ne pas déclarer une moins-value l'année où elle est subie** | le droit à l'imputation future est **perdu**, alors même qu'aucun impôt n'était dû cette année-là | rôle `impots`, `revenus-financiers.md` |
| **Attendre pour réclamer un dégrèvement ou une remise** | le délai passe, et il ne se rouvre pas | rôle `impots`, `reclamation-et-controle.md` |

### Celles qui bloquent une trésorerie

| L'idée | Ce qu'elle coûte réellement | → le détail |
|---|---|---|
| **Rester en franchise de TVA « pour payer moins »** | on ne **récupère pas** la TVA sur ses achats ; et le seuil de la franchise est **bien plus bas** que celui de la micro ⇒ on franchit sans le voir et on sort la taxe de sa marge | rôle `comptable`, `tva.md` |
| **Garder le régime micro quand les charges réelles dépassent l'abattement** | de l'impôt **et** des cotisations sur de l'argent qu'on n'a pas gagné. ★ C'est le déclencheur de bascule le plus fréquent, et le plus souvent manqué | rôle `comptable`, `micro-entreprise.md` |
| **Embaucher en micro** | un salaire **ne se déduit pas d'un forfait** : le régime n'est pas conçu pour employer | rôle `comptable`, `formes-juridiques.md` |
| **Clôturer au 31 décembre par défaut** | c'est le moment le plus chargé, et la date entraîne toute une chaîne d'échéances derrière elle | rôle `comptable`, `cloture-et-liasse.md` |
| **Accepter un étalement fiscal sans lire les garanties** | ⚠️ un étalement peut coûter un **engagement personnel qui survivra à l'entreprise** | `difficultes-et-mediation.md`, `garanties-et-caution-dirigeant.md` |
| **Refuser une augmentation, des heures ou une mission « à cause de la tranche »** | on renonce à un revenu net réel sur la base d'un calcul faux | rôle `impots`, `impot-revenu.md` |

### Celles qui déclenchent une sanction ou un contrôle

| L'idée | Ce qu'elle coûte réellement | → le détail |
|---|---|---|
| **Ne pas déclarer pour gagner du temps** | ⛔ **le pire réflexe du fichier** : la majoration passe au taux le plus élevé, **et** on ferme l'accès à la CCSF et aux délais Urssaf — exactement les deux recours dont on aura besoin | `difficultes-et-mediation.md`, rôle `comptable`, `cloture-et-liasse.md` |
| **Invoquer le droit à l'erreur sur un défaut de déclaration** | ⛔ le dispositif **exclut précisément** l'absence ou le retard de déclaration : il protège celui qui s'est trompé, pas celui qui n'a rien déposé | rôle `impots`, `reclamation-et-controle.md` |
| **Découper un contrat pour passer sous le seuil de l'attestation de vigilance** | le seuil porte sur **l'opération**, pas sur une facture — et un découpage visiblement artificiel **se retourne contre vous** | rôle `comptable`, `paie-et-embauche.md` |
| **Oublier un compte d'actifs numériques détenu à l'étranger** | ⛔ **l'amende est PAR COMPTE** : cinq plateformes oubliées, cinq amendes | rôle `impots`, `revenus-financiers.md` |
| **Déposer sur papier au lieu de télétransmettre** | une **majoration qui punit le canal**, même quand la déclaration est à l'heure | rôle `comptable`, `cloture-et-liasse.md` |
| **Laisser expirer le délai de réponse à une rectification** | on quitte la procédure contradictoire — là où le dossier se discute — pour un terrain beaucoup moins favorable | rôle `impots`, `reclamation-et-controle.md` |
| **Une domiciliation en zone d'exonération sans y exercer** | l'implantation exigée est **réelle** : c'est un redressement en attente, pas un levier | fiche ZFRR en `## Sources` |

## ⛔ Les deux lignes que ce fichier ne franchit pas

**1. Aucune recommandation personnalisée portant sur un instrument financier.** C'est le **conseil en
investissement**, activité réglementée par les articles **L321-1** et **L541-1** du code monétaire et
financier, dont l'exercice illégal est puni par **L573-1**.

⚠️ **La frontière porte sur l'ACTE, pas sur le sujet** : expliquer une mécanique fiscale est licite ;
dire à quelqu'un ce qu'il devrait souscrire ne l'est pas. Concrètement, ce fichier explique **comment
un PER est imposé** ; il ne dit **jamais** s'il faut en ouvrir un, ni combien y verser. Voir
`docs/taxonomie-comptabilite.md` et `activites-reglementees.md` du rôle `juriste`. **La pédagogie sur
les placements vit dans le rôle `patrimoine`.**

**2. Aucune optimisation « à la limite ».** Ce fichier dit **où la frontière commence**, il ne s'en
approche pas.

★ **Le repère utile, et il est simple** : le droit sanctionne l'**abus de droit** par la majoration la
plus lourde de tout le barème des majorations — plus lourde que le manquement délibéré. ⇒ **Dès qu'un
montage n'a d'autre justification que fiscale, il n'est plus dans le périmètre de ce fichier** : il se
traite avec un avocat fiscaliste, avant, et éventuellement par un **rescrit**. → rôle `impots`,
`reclamation-et-controle.md`.

⚠️ **Et un rappel qui vaut pour tout le fichier** : un levier légal mal documenté se comporte comme un
levier illégal le jour du contrôle. **La pièce justificative fait partie du levier.**

## Ce qui reste à écrire

Par ordre d'utilité réelle.

- ★★ **Les crédits d'impôt d'une petite structure** — recherche, innovation, recherche collaborative,
  et **l'apprentissage** dont **je n'ai pas pu établir s'il existe encore un crédit d'impôt** (la
  recherche officielle ne renvoie que la **taxe** d'apprentissage et le contrat d'apprentissage).
  ⛔ **Aucun fichier du dépôt ne traite ce sujet** : c'est le plus gros trou de cette carte, et la
  catégorie où les dispositifs meurent le plus vite. **Un fichier dédié du rôle `comptable` serait plus
  juste qu'une ligne ici.**
- ★★ **Les conditions de fond des zonages autres que ZFRR** — BER, ZFU-TE, BUD : seules les fiches sont
  pointées, les conditions ne sont pas vérifiées. Et pour ZFRR, **le plafond de chiffre d'affaires hors
  zone** reste à sourcer verbatim.
- ★ **Les conditions réelles des dons, de l'emploi à domicile et de la garde d'enfants** : la carte sait
  dire *où* les déclarer, pas *si* on y a droit. À écrire dans `impot-revenu.md` du rôle `impots`.
- ★ **Le calcul comparatif du rattachement d'un enfant majeur** — rattachement contre déduction d'une
  pension. C'est un arbitrage chiffré, il n'a pas sa place ici mais dans `impot-revenu.md`.
- **Le prélèvement à la source comme levier de trésorerie** : la modulation en cours d'année est un
  levier gratuit, et il manque à la section correspondante. À écrire d'abord dans `impot-revenu.md`.
- **La CFE** et les exonérations locales sur délibération, côté charges d'une petite structure.
- **Les aides à l'embauche** (par opposition aux crédits d'impôt) : autre mécanique, autre guichet.
- ⚠️ **Une relecture croisée annuelle de cette carte** : par construction, elle vieillit quand les
  fichiers cibles bougent. **Les liens et les noms de fichiers sont à revérifier à chaque campagne
  déclarative.**

## Sources

Pages que j'ai **réellement fetchées** le **2026-08-17** :

- CGI, article 1728 (majorations pour défaut ou retard de déclaration), version en vigueur affichée au
  21/02/2026 — <https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006179995/>
- CGI, article 1727 (intérêt de retard, et réduction en cas de dépôt spontané), version en vigueur
  affichée du 16/02/2025 au 01/01/2027 —
  <https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006133936/>
- Crédit d'impôt pour la formation des dirigeants — **supprimé** (page du 21/02/2026) —
  <https://entreprendre.service-public.gouv.fr/vosdroits/F23460>
- Exonérations fiscales en ZFRR et ZFRR+ (page du 21/02/2026) —
  <https://entreprendre.service-public.gouv.fr/vosdroits/F31139>
- Déclaration papier 2026 des revenus 2025, liste des annexes dont le **2042-RICI** (page du
  15/04/2026) — <https://www.service-public.gouv.fr/particuliers/vosdroits/R1281>
- Recherche « crédit d'impôt » sur le portail entreprises —
  <https://entreprendre.service-public.gouv.fr/recherche?keyword=cr%C3%A9dit+d%27imp%C3%B4t>

**Fiches officielles pointées par cette carte, non vérifiées ligne à ligne ici** — ce sont les points
d'entrée à lire avant de s'appuyer sur un crédit d'impôt ou une exonération de zone :

- Crédit d'impôt recherche (CIR) — <https://entreprendre.service-public.gouv.fr/vosdroits/F23533>
- Crédit d'impôt innovation (CII) — <https://entreprendre.service-public.gouv.fr/vosdroits/F35494>
- Crédit d'impôt recherche collaborative (CICo) —
  <https://entreprendre.service-public.gouv.fr/vosdroits/F36528>
- Exonérations en bassin d'emploi à redynamiser (BER) —
  <https://entreprendre.service-public.gouv.fr/vosdroits/F31154>
- Exonérations sur les bénéfices en zone franche urbaine (ZFU-TE) —
  <https://entreprendre.service-public.gouv.fr/vosdroits/F31149>
- Exonérations en bassin urbain à dynamiser (BUD) —
  <https://entreprendre.service-public.gouv.fr/vosdroits/F34799>
- **Vérifier si une commune est en ZFRR ou ZFRR+** —
  <https://entreprendre.service-public.gouv.fr/vosdroits/R69377>

⛔ **Non vérifié ici** : l'existence d'un crédit d'impôt apprentissage aujourd'hui. La recherche
officielle ne renvoie que la **taxe d'apprentissage** et le **contrat d'apprentissage** — **ce n'est
pas une réponse**, et je ne conclus donc ni dans un sens ni dans l'autre.

## Rappel de cadrage

Ce fichier alimente le skill `financement`, un outil d'**aide à la décision**. Il montre **où sont les
leviers et à quelles conditions** — il ne construit aucun montage, ne chiffre aucun gain, et ne
remplace ni un expert-comptable inscrit à l'Ordre, ni un avocat fiscaliste, ni l'administration
compétente.

⚠️ **La réserve propre à ce fichier** : c'est une **carte relayée**. Sa valeur tient à l'exactitude des
fichiers vers lesquels il pointe, et il vieillit **sans le signaler** quand ceux-ci évoluent. ⇒ **Sur
toute valeur, ouvrez le fichier cité ; sur toute décision, ouvrez la source du fichier cité.**
