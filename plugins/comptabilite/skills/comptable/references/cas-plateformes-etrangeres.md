# Cas : être payé par une plateforme étrangère

> **État : `PARTIEL`**. **`RÉDIGÉ`** pour la déclaration des comptes détenus à l'étranger et son
> régime de sanction, le délai de reprise, ce que la plateforme déclare de vous, le taux de change,
> la conservation et la traduction des justificatifs, et la facturation par mandat. **`À ÉCRIRE`**
> pour la qualification exacte du revenu (prestation ou redevance), pour l'identité du vendeur dans
> une marketplace, et pour les ventes à des particuliers **hors** UE — trois points que je n'ai pas
> pu trancher sur une page officielle, et qui sont donc laissés ouverts plutôt que devinés.
> Vérifié le **2026-08-17**. Pages sources : `impots.gouv.fr` des **10/03/2026**, **16/06/2026**,
> **09/03/2026**, **22/08/2025**, **22/03/2024** et **14/02/2025** · fiche
> `entreprendre.service-public.gouv.fr` vérifiée le **07/08/2026** · CGI et LPF sur Légifrance,
> versions en vigueur au **01/07/2026**. ⚠️ Deux pages sont anciennes et à recouper : la page sur les
> numéros d'identification (**27/07/2016**) et celle sur l'imposition des revenus de source étrangère
> (**12/03/2021**). Le BOFiP cité sur la notion de compte « utilisé » est du **26/05/2021**.

## ⏱️ D'abord : le risque n'est pas celui qu'on croit

Quelqu'un qui vend sur une app store ou une marketplace arrive presque toujours avec la même
question — *« comment je déclare ça ? »* — alors que le vrai danger est ailleurs.

| Ce qui inquiète | Ce qui coûte réellement |
|---|---|
| « Je me trompe de case » | une case fausse se corrige |
| « La plateforme est à l'étranger, l'administration ne voit rien » | ⛔ **faux** : elle reçoit le chiffre par échange automatique |
| — | ★★ **le compte de paiement de la plateforme non déclaré** : amende par compte, présomption de revenus, et délai de contrôle porté à **10 ans** |

★★ **Le point à traiter en premier, avant toute question de TVA ou de catégorie, c'est l'existence
d'un compte détenu à l'étranger.** C'est le seul endroit du sujet où l'oubli se paie en milliers
d'euros et rouvre des années entières au contrôle. Tout le reste se rattrape.

## 1. Qualifier le revenu — et pourquoi ça n'est pas cosmétique

Selon le contrat, ce que verse une plateforme peut être :

- le **prix d'une prestation de services** rendue à la plateforme ou au client final ;
- une **redevance** — la contrepartie d'une concession de droit d'usage sur un logiciel, un contenu,
  une marque ;
- un **revenu publicitaire** — une part de recettes de diffusion ;
- le **produit de ventes au client final**, la plateforme n'étant qu'un encaisseur.

★ **La distinction prestation / redevance change deux choses à la fois, et c'est pour ça qu'elle
compte :**

1. **Elle change l'article de la convention fiscale qui s'applique** — donc le droit du pays de la
   plateforme de prélever une retenue à la source, et le taux plafond de cette retenue. Une même
   somme peut sortir nette ou amputée selon la ligne du contrat qui la nomme. Aucun taux ne peut
   être donné ici : voir la section 3.
2. **Elle change la catégorie fiscale interne** — donc, en micro, l'abattement forfaitaire
   appliqué. → `micro-entreprise.md`

⚠️ **Je n'ai pas trouvé de page officielle tranchant si la rémunération versée par une marketplace
logicielle est une prestation de services ou une redevance de propriété intellectuelle.** Ce dépôt
n'admet pas les sources secondaires : la valeur reste donc `a_verifier`. ⇒ **Posez la question au
service des impôts des entreprises, contrat de la plateforme en main**, avant la première
déclaration — pas après, parce que la catégorie commande l'abattement de toute l'année.

### ⚠️ La question préalable que personne ne pose : qui est le vendeur ?

Deux montages produisent des obligations radicalement différentes :

- **la plateforme vend en son nom propre** au client final, et vous verse une rémunération : vous
  avez **un seul client**, professionnel, établi à l'étranger ;
- **la plateforme n'est qu'un intermédiaire** : vous avez **des milliers de clients**, souvent des
  particuliers, répartis dans autant de pays — et la TVA suit *leur* lieu, pas le vôtre.

★★ **Ce seul point décide si le guichet unique de TVA vous concerne ou pas.** Il ne se lit pas dans
la loi fiscale mais **dans les conditions générales de la plateforme**. Je n'ai pas pu vérifier sur
une source admise le régime applicable aux interfaces électroniques pour les services fournis par
voie électronique — la base européenne n'était pas exploitable à la date de vérification. ⇒
**à faire confirmer, et à ne jamais présumer.**

## 2. La TVA

### Ce que vous facturez à la plateforme

Si votre client est la plateforme et qu'elle est assujettie hors de France, la prestation **n'est pas
soumise à la TVA française** et la facture porte une mention selon que la plateforme est dans l'UE ou
non. Les mentions exactes, les seuils de la franchise en base et la **déclaration européenne de
services (DES)** — à transmettre dans les **10 jours** du mois suivant l'exigibilité — sont traités
dans **`tva.md`** : ne les dupliquez pas de mémoire, allez les lire là.

### ★★ Ce que vous ACHETEZ à l'étranger, et que tout le monde oublie

Une commission de marketplace, un abonnement d'hébergement, de la publicité en ligne : ce sont des
**prestations reçues d'un prestataire établi hors de France**. Or, sur ces opérations, la page
`impots.gouv.fr` est explicite :

> « Le redevable de la TVA est le preneur de la prestation (le client). »

> « Lorsqu'une prestation relevant de ces règles particulières est effectuée par un assujetti établi
> hors de France, la taxe est acquittée par le client assujetti ayant un numéro intracommunautaire
> français. »

Et la même page ajoute la phrase qui rend le sujet piégeux :

> « Un micro-entrepreneur bénéficiant de la franchise en base en matière de TVA est assujetti à la
> TVA mais n'est pas redevable de la TVA. »

★ **« Assujetti » et « redevable » ne sont pas synonymes** — c'est la distinction la plus mal comprise
de toute la TVA. Être dispensé de *collecter* la TVA sur ses ventes ne dit rien de ce qu'on doit
faire quand on *reçoit* une prestation de l'étranger.

⚠️ **Je n'ai trouvé aucune page officielle traitant explicitement le cas du preneur en franchise en
base qui achète une prestation hors de France.** La lecture combinée des deux passages ci-dessus
pousse fortement vers l'autoliquidation, donc vers l'obtention d'un numéro de TVA
intracommunautaire et le dépôt d'une déclaration. **Je ne l'écris pas comme un fait.** ⇒ **Question
à poser au SIE avant le premier achat** : une autoliquidation oubliée se rattrape, mais elle se
rattrape avec des pénalités, et sur toutes les factures de l'exercice.

### Le numéro de TVA intracommunautaire

- Il **s'ajoute** au SIREN, il ne le remplace pas : « Il comporte 2 lettres (FR en France) et
  11 chiffres (clé informatique de 2 chiffres + le numéro SIREN) » *(page du 27/07/2016, à
  recouper)*. Une facture porte les deux.
- Il « doit obligatoirement figurer sur les factures, les déclarations d'échanges de biens (DEB),
  les déclarations européennes de services (DES) et les déclarations de TVA de l'entreprise ».
- ★ **Il est gratuit.** L'attribution « relève de la compétence de votre service des impôts des
  entreprises (SIE) et [...] elle est entièrement gratuite » *(page du 16/06/2026)*, sur demande
  depuis l'espace professionnel, après obtention du SIRET. **Des intermédiaires payants font croire
  le contraire.**
- ⚠️ **En demander un ne fait pas sortir de la franchise en base** — c'est un point déjà établi dans
  `tva.md`, et la distinction assujetti / redevable ci-dessus en donne le mécanisme. Je n'ai
  toutefois pas trouvé de page officielle l'énonçant en propre : à faire confirmer si la décision en
  dépend.

### Vos ventes à des particuliers hors de France

Si vous vendez directement à des particuliers d'autres États membres (biens à distance ou services),
la règle est celle du **guichet unique de TVA (OSS)**, dispositif **optionnel** :

> « un seuil de **10 000 €** a été instauré, en deçà duquel la TVA sur les prestations de services et
> les ventes à distance intracommunautaire de biens, reste due dans l'État membre d'établissement du
> prestataire » *(page du 22/03/2024)*.

Au-delà, la TVA est due **dans l'État du consommateur** — et le guichet unique évite de s'immatriculer
dans chaque pays.

⚠️ Ce seuil ne vise que les clients **non assujettis établis dans l'UE**. **Le cas des particuliers
établis hors de l'UE n'est pas couvert ici** : je n'ai pas trouvé de page officielle le traitant.
`À ÉCRIRE`.

## 3. La retenue à la source pratiquée par la plateforme

Certaines plateformes retiennent un pourcentage avant de vous verser quoi que ce soit, au titre de
l'impôt de *leur* pays. Trois réflexes, dans cet ordre :

**1. Ouvrir la convention fiscale du pays concerné.** Les textes sont publiés pays par pays sur
`impots.gouv.fr`, rubrique « Conventions par pays ». ⛔ **Aucun taux générique n'existe** : il dépend
de la convention **et** de la qualification du revenu (section 1). Une réponse qui annonce un taux
sans avoir ouvert la convention est une réponse inventée.

**2. Fournir à la plateforme la preuve de votre résidence fiscale française.** C'est ce qui déclenche
le taux conventionnel — souvent réduit, parfois nul — au lieu du taux interne plein. Le document est
le **formulaire n° 730-SD, « Attestation de résidence fiscale en France »** (millésime 2026, versions
franco-anglaise et franco-espagnole).

⛔ **Ne confondez pas avec le formulaire n° 5000-SD.** Celui-là sert au cas **inverse** : un
non-résident qui perçoit des revenus **de source française**. Le confondre, c'est envoyer à la
plateforme un document qui ne prouve rien.

★ **Le formulaire se fournit AVANT le paiement.** Une retenue déjà prélevée ne se corrige plus par
l'administration française : elle se réclame à l'État étranger, dans ses formes et ses délais.

**3. Neutraliser la double imposition en France.** Deux mécanismes, selon la convention *(page du
12/03/2021, à recouper)* :

| Mécanisme | Effet |
|---|---|
| **Crédit d'impôt** | « neutralisation par application d'un crédit d'impôt égal à l'impôt payé à l'étranger » |
| **Exonération avec taux effectif** | les revenus exonérés « seront simplement pris en compte afin de déterminer le montant d'impôt » |

Le véhicule déclaratif est la **déclaration n° 2047**. → `impot-revenu.md`

⚠️ **Réserve importante** : ces deux mécanismes sont décrits pour l'impôt sur le revenu. **L'effet
d'une retenue étrangère sur un chiffre d'affaires de micro-entreprise n'est pas traité ici** — en
micro, on est imposé sur le chiffre d'affaires après abattement, et l'articulation avec un crédit
d'impôt conventionnel n'a pas pu être vérifiée. `À ÉCRIRE`, et **à faire trancher par un
professionnel si des sommes significatives sont retenues.**

## 4. ★★ Les comptes détenus à l'étranger — le risque le plus sous-estimé

### L'obligation

**CGI, article 1649 A, deuxième alinéa** *(version en vigueur au 07/05/2022)* :

> « Les personnes physiques, les associations, les sociétés n'ayant pas la forme commerciale,
> domiciliées ou établies en France, sont tenues de déclarer, en même temps que leur déclaration de
> revenus ou de résultats, les références des comptes **ouverts, détenus, utilisés ou clos** à
> l'étranger. »

Quatre verbes, et chacun élargit le piège :

- **ouvert** — même si vous n'y avez jamais rien reçu ;
- **détenu** — même inactif. Depuis le 01/01/2019, tous les comptes à l'étranger doivent être
  déclarés, y compris non utilisés *(BOFiP du 26/05/2021, à recouper)* ;
- **utilisé** — un compte est réputé utilisé « dès lors que [la personne] a effectué au moins une
  opération de crédit ou de débit pendant la période visée par la déclaration ». **Une seule
  opération suffit** ; les inscriptions d'intérêts et les frais de gestion ne comptent pas
  *(même source)* ;
- **clos** — **le compte fermé dans l'année doit encore être déclaré.** C'est l'oubli type : on ferme
  le compte de la plateforme, on croit la page tournée.

Le formulaire est le **n° 3916 / 3916 bis** (comptes bancaires, comptes d'actifs numériques,
contrats d'assurance-vie), à déposer **avec la déclaration de revenus**.

⚠️ **Ce qu'aucune page ne dit clairement, et qui est la vraie difficulté pratique : un « compte de
paiement » de plateforme est-il un compte au sens de ce texte ?** Le BOFiP vise les comptes ouverts
auprès de « toute personne de droit privé ou public qui reçoit habituellement en dépôt des valeurs
mobilières, titres ou fonds ». **Je n'ai pas trouvé de page officielle nommant explicitement les
portefeuilles de marketplaces ou les prestataires de services de paiement.**

⇒ **Le réflexe raisonnable, vu l'ampleur de la sanction : si le compte a un solde que vous pouvez
conserver et déplacer, traitez-le comme un compte et posez la question au SIE.** Le coût d'une
déclaration inutile est nul. Le coût de l'omission est ci-dessous.

### Les sanctions

| Manquement | Sanction |
|---|---|
| Compte non déclaré | **1 500 €** par compte |
| Compte dans un État sans convention d'assistance administrative | **10 000 €** par compte |
| Omission ou inexactitude | amende de l'article 1729 B du CGI |
| Sommes transitées par un compte non déclaré | **taxation d'office + majoration de 40 %** |

**CGI, article 1736 IV** *(version en vigueur au 01/07/2026)* :

> « Les infractions aux dispositions du deuxième alinéa de l'article 1649 A et de l'article 1649 A
> bis sont passibles d'une amende de **1 500 €** par compte ou avance non déclaré. »

Montant porté à :

> « **10 000 €** par compte non déclaré lorsque l'obligation déclarative concerne un État ou un
> territoire qui n'a pas conclu avec la France une convention d'assistance administrative en vue de
> lutter contre la fraude et l'évasion fiscales permettant l'accès aux renseignements bancaires. »

★★ **Et surtout, la présomption — c'est elle qui fait mal.** Article 1649 A du CGI :

> « Les sommes, titres ou valeurs transférés à l'étranger ou en provenance de l'étranger par
> l'intermédiaire de comptes non déclarés dans les conditions prévues au deuxième alinéa constituent,
> **sauf preuve contraire**, des revenus imposables. »

Ce que `impots.gouv.fr` traduit ainsi *(page du 10/03/2026)* :

> « Taxation des revenus présumés en vertu de l'article 1649 A du CGI, assortie d'une majoration de
> **40 %**. »

★★ **Autrement dit : l'argent reçu sur un compte de plateforme non déclaré est présumé être un revenu
imposable — même si vous avez déjà déclaré ce même chiffre d'affaires par ailleurs.** C'est à vous
d'apporter la preuve contraire. **La charge de la preuve est retournée**, et c'est exactement pour ça
que les relevés de la plateforme doivent être conservés (section 5).

### Les portefeuilles de crypto-actifs : un régime à part

**CGI, article 1736 X** *(version en vigueur au 01/07/2026)* :

> « Les infractions à l'article 1649 bis C sont passibles d'une amende de **750 €** par portefeuille
> ou par crypto-actif unique et non fongible non déclarés ou de **125 €** par omission ou
> inexactitude, dans la limite de **10 000 €** par déclaration. »

Montants « respectivement portés à **1 500 €** et **250 €** » lorsque la valeur vénale des
crypto-actifs uniques et non fongibles ou celle des portefeuilles ouverts, détenus, utilisés ou clos
à l'étranger « est supérieure à **50 000 €** ».

★ **Deux différences décisives avec les comptes bancaires** : l'amende unitaire est plus faible,
**mais surtout elle est plafonnée par déclaration** — plafond qui **n'existe pas** pour les comptes de
l'article 1649 A, où l'amende est purement multiplicative. ⇒ **Un portefeuille crypto oublié coûte
moins cher qu'un compte de paiement oublié.** Contre-intuitif, et bon à savoir pour hiérarchiser
l'urgence. Sur l'imposition des cessions elles-mêmes → `revenus-financiers.md`.

### ★★ Le délai de reprise : l'effet le plus grave, et le plus discret

**LPF, article L169** *(version en vigueur au 01/07/2026)* :

| Situation | Le contrôle est possible jusqu'à |
|---|---|
| Droit commun | « la fin de la **3**ᵉ année qui suit celle au titre de laquelle l'imposition est due » |
| Obligations des articles 123 bis, 209 B, 1649 A, 1649 AA, 1649 AB, 1649 bis C non respectées | « la fin de la **10**ᵉ année » |

★ **L'échappatoire, et elle est chiffrée** : l'extension

> « ne s'applique pas lorsque le contribuable apporte la preuve que le total des soldes créditeurs de
> ses comptes à l'étranger n'a pas excédé **50 000 €** à un moment quelconque de l'année au titre de
> laquelle la déclaration devait être faite. »

★★ **« À un moment quelconque de l'année »** : ce n'est pas le solde au 31 décembre, c'est le **pic**.
Un compte vidé chaque mois peut avoir dépassé le seuil sans jamais l'afficher en fin d'année. **Et
c'est au contribuable d'apporter la preuve** — donc **sans les relevés mensuels, on ne peut pas
refermer le délai de 10 ans**, même quand on est de bonne foi. C'est la raison la plus concrète de
tout archiver.

## 5. Le taux de change et les justificatifs

**Le cours à retenir** *(page `impots.gouv.fr` du 09/03/2026)* :

> « En principe, il faut utiliser le cours du change à Paris au jour de l'encaissement »

⚠️ **Cette page est rédigée pour les revenus suisses** et prévoit un taux moyen annuel calculé par
l'administration **réservé aux travailleurs frontaliers franco-suisses**. Elle précise que ce taux
moyen ne s'applique pas aux gains exceptionnels. ⇒ **Ne transposez pas un taux moyen annuel à des
recettes de plateforme** : le principe reste le cours du jour de l'encaissement, opération par
opération.

★ **Conséquence opérationnelle** : la conversion se fait **au fil de l'eau**, pas une fois par an sur
le total. Un tableur où chaque versement porte sa date, son montant en devise et son cours vaut mieux
que n'importe quelle reconstitution de janvier suivant.

**Les justificatifs en anglais** — deux règles, et la seconde surprend *(fiche vérifiée le
07/08/2026)* :

> « Lorsque la facture est rédigée en langue étrangère, il peut être exigé une traduction
> certifiée. »

> « Les factures émises ou reçues par une entreprise doivent être conservées pendant **10 ans**. »

⚠️ **La conservation pendant 10 ans et le délai de reprise de 10 ans sont deux horloges distinctes.**
Elles coïncident ici par hasard, pas par construction : ne raisonnez pas sur l'une pour conclure sur
l'autre.

## 6. Ce que la plateforme déclare de vous

★★ **La plateforme vous déclare, et l'information traverse les frontières.** C'est le dispositif DAC7.

| Étape | Échéance |
|---|---|
| L'opérateur de plateforme déclare à son administration fiscale | « au plus tard le 31 janvier de l'année suivant celle au cours de laquelle les opérations ont été réalisées » *(CGI, art. 1649 ter A)* |
| L'opérateur vous adresse un récapitulatif | « en janvier », « un récapitulatif des opérations réalisées au cours de l'année précédente » *(page du 22/08/2025)* |
| Les administrations s'échangent l'information | « au plus tard le dernier jour du mois de février de l'année qui suit » |

Et côté déclaration de revenus :

> « La transmission des informations par votre opérateur de plateforme auprès de l'administration
> fiscale va permettre d'afficher les éléments qui vous concernent et ainsi de vous accompagner lors
> de votre déclaration de revenus en ligne. »

★★ **Ce que la plateforme déclare est donc comparé à ce que vous déclarez.** Deux conséquences
pratiques, et ce sont les seules qui comptent :

1. ⛔ **« C'est à l'étranger, ils ne verront pas » est faux.** L'échange est automatique et daté.
2. ★ **Le récapitulatif de janvier est une pièce à rapprocher de votre comptabilité AVANT de
   déclarer**, pas un courrier à archiver sans le lire. ⚠️ **Il porte en général le montant BRUT des
   opérations**, avant commission de la plateforme et avant retenue à la source : un écart avec ce
   que vous avez encaissé est **normal**, mais il doit être **expliqué et documenté**. C'est
   exactement l'écart que l'administration voit.

## 7. La facturation

Les mentions obligatoires générales et le cas du client étranger sont traités dans **`facturation.md`**
et **`tva.md`** : mention « Autoliquidation » pour un assujetti de l'UE, mention d'exonération pour un
assujetti hors UE, et les deux numéros de TVA intracommunautaire.

**Quand la plateforme émet le document à votre place**, le cadre est le **mandat de facturation**
*(fiche vérifiée le 07/08/2026)* :

> « Le vendeur ou le prestataire autorise son client (auto-facturation) ou un tiers (sous-traitance de
> la facturation) à facturer pour son compte par un mandat de facturation. »

★ **C'est le régime réel de la plupart des marketplaces** : le « rapport de ventes » ou le
« statement » qu'elles produisent tient lieu de facture parce que vous les y avez autorisées en
acceptant leurs conditions générales — souvent sans le savoir.

⚠️ **La fiche ne dit pas qui reste responsable des obligations de facturation en cas de mandat.** Je
ne l'affirme donc pas. ⇒ **Ne partez pas du principe que le mandat transfère la responsabilité** :
vérifiez que le document de la plateforme porte bien les mentions exigées, et conservez-le comme
votre propre facture.

## Ce qui reste à écrire

Par ordre d'utilité réelle :

1. ★★ **Qui est le vendeur dans une marketplace de services numériques** — régime des interfaces
   électroniques. C'est le point qui décide si le guichet unique OSS vous concerne ; il commande
   toute la section TVA et il est aujourd'hui ouvert.
2. ★★ **L'autoliquidation par un preneur en franchise en base** qui achète commissions, publicité ou
   hébergement à l'étranger. Situation extrêmement courante, aucune page officielle trouvée.
3. ★ **La qualification prestation / redevance** d'une licence de logiciel vendue sur une
   marketplace, et sa catégorie (BIC ou BNC) — elle commande l'abattement micro.
4. ★ **L'articulation d'une retenue à la source étrangère avec le régime micro** : crédit d'impôt
   imputable ou perte sèche ?
5. Les **ventes à des particuliers établis hors de l'UE** (services fournis par voie électronique).
6. Le **cas des prestataires de paiement hors UE et des paiements en crypto** : qualification du
   portefeuille, et articulation avec `revenus-financiers.md`.
7. La **facturation électronique** et son application aux documents émis par une plateforme
   étrangère → `facturation.md`.
8. Le **traitement d'un oubli déjà commis** : régularisation spontanée, et ce qu'elle change sur les
   amendes de la section 4. Sujet sensible — **relève d'un professionnel, pas d'un fichier de
   référence.**

## Sources

- CGI, article 1649 A (déclaration des comptes à l'étranger, présomption de revenus) —
  <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000045764822>
- CGI, article 1736 (amendes, IV pour les comptes et X pour les crypto-actifs) —
  <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051215709>
- LPF, article L169 (délais de reprise) —
  <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051759330>
- CGI, article 1649 ter A (déclaration par les opérateurs de plateforme) —
  <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044936377>
- BOFiP, déclaration des comptes ouverts, détenus, utilisés ou clos hors de France —
  <https://bofip.impots.gouv.fr/bofip/580-PGP.html/identifiant=BOI-CF-CPF-30-20-20210526>
- Déclarer ses comptes et contrats détenus à l'étranger (sanctions) —
  <https://www.impots.gouv.fr/international-particulier/questions/je-viens-ou-je-reviens-en-france-et-je-ne-conserve-pas-dinterets>
- Prestations entre assujettis (redevable, DES, franchise en base) —
  <https://www.impots.gouv.fr/professionnel/prestations-entre-assujettis>
- Les numéros d'identification —
  <https://www.impots.gouv.fr/professionnel/les-numeros-didentification>
- L'attribution d'un numéro de TVA intracommunautaire est-elle payante ? —
  <https://www.impots.gouv.fr/professionnel/questions/lattribution-dun-numero-de-tva-intracommunautaire-est-elle-payante>
- Guichet unique de TVA — suis-je concerné ? —
  <https://www.impots.gouv.fr/professionnel/suis-je-concerne-0>
- J'utilise le guichet unique TVA (IOSS-OSS) —
  <https://www.impots.gouv.fr/professionnel/jutilise-le-guichet-unique-tva-ioss-oss>
- Formulaire n° 730-SD, attestation de résidence fiscale en France —
  <https://www.impots.gouv.fr/formulaire/730-sd/attestation-de-residence-fiscale-en-france>
- Les conventions internationales (conventions par pays) —
  <https://www.impots.gouv.fr/les-conventions-internationales>
- Imposition des revenus de source étrangère —
  <https://www.impots.gouv.fr/international-particulier/imposition-des-revenus-de-source-etrangere>
- Quel taux de change utiliser pour la déclaration —
  <https://www.impots.gouv.fr/international-particulier/questions/quel-taux-de-change-dois-je-utiliser-pour-la-declaration>
- Comment déclarer mes revenus issus de l'économie collaborative —
  <https://www.impots.gouv.fr/particulier/questions/comment-declarer-mes-revenus-issus-de-leconomie-collaborative>
- Transfert d'informations DPI-DAC7 —
  <https://www.impots.gouv.fr/transfert-dinformations-en-application-des-dispositifs-dpi-dac7-plateformes-deconomie-collaborative>
- Tout savoir sur la facturation (mandat de facturation, traduction, conservation) —
  <https://entreprendre.service-public.gouv.fr/vosdroits/F23208>
- Formulaire n° 3916 —
  <https://www.impots.gouv.fr/formulaire/3916/declaration-par-un-resident-dun-compte-letranger-ou-dun-contrat-de-capitalisation-o>

## Rappel de cadrage

Ce fichier alimente le skill `comptable`, un outil d'**aide à la décision**. Il ne remplace ni un
expert-comptable inscrit à l'Ordre, ni un avocat inscrit à un barreau, ni le service des impôts des
entreprises.

⚠️ **Sur ce sujet, la première utilité n'est pas fiscale, elle est chronologique** : faire déclarer le
compte détenu à l'étranger, faire fournir l'attestation de résidence **avant** le premier versement,
et faire archiver les relevés mois par mois. Ces trois gestes coûtent une heure et referment
l'essentiel du risque. Le débat sur la bonne catégorie de revenu vient après — et il se tranche avec
un professionnel, contrat de la plateforme en main.
