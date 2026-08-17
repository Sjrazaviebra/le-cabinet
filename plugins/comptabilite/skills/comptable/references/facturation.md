# Factures : mentions obligatoires, conservation, facturation électronique

> **État : `PARTIEL`.** **`RÉDIGÉ`** pour les mentions obligatoires, les sanctions, le calendrier de
> la facturation électronique, la numérotation, la date d'émission, la conservation (durées), l'avoir
> et la facture rectificative, l'autofacturation et le devis.
> **`À ÉCRIRE`** pour la **piste d'audit fiable** et pour la **forme admise de l'archivage
> numérique** : aucune page officielle admise n'a pu être atteinte le 2026-08-17 sur ces deux
> points — ils sont marqués `a_verifier` et **ne doivent pas être présentés comme une réponse**.
> Vérifié le **2026-08-17**. Pages sources : `entreprendre.service-public.gouv.fr` du **11/08/2026**
> (mentions), du **07/08/2026** (facturation, calendrier), du **08/12/2025** (documents commerciaux) ;
> `impots.gouv.fr` du **16/01/2026** et du **26/05/2026** ; Légifrance art. 1737 CGI **version du
> 21/02/2026** ; art. 242 nonies A annexe II CGI **version du 01/01/2025**.
> ⚠️ Pages plus anciennes, **à recouper** : conservation (**01/07/2024**), devis (**09/09/2022**),
> exigibilité TVA sur acompte (**01/01/2023**), BOFiP sanctions (**12/09/2012**).

## ⏱️ D'abord : la date du 1er septembre 2026, et pourquoi il faut la revérifier

**Ne donnez jamais ce calendrier de mémoire.** Il a déjà été décalé, et **la loi elle-même prévoit
qu'il peut l'être encore**. C'est la première chose à dire.

★★ **Nota de l'article 1737 du CGI, cité verbatim par Légifrance :**

> « Conformément au premier alinéa du III de l'article 91 de la loi n° 2023-1322 du 29 décembre 2023,
> ces dispositions s'appliquent aux factures émises à compter du 1er septembre 2026. **Un décret peut
> fixer une date ultérieure, qui ne peut être postérieure au 1er décembre 2026.** »

⇒ **Le report est écrit dans le texte, pas seulement dans la rumeur.** Avant d'annoncer une date à
qui que ce soit, allez lire <https://www.impots.gouv.fr/professionnel/je-decouvre-la-facturation-electronique>
et vérifiez qu'aucun décret n'est paru. **La date ci-dessous est celle du 2026-08-17.**

| Date | Qui | Ce qui devient obligatoire |
|---|---|---|
| **1er septembre 2026** | **toutes les entreprises** | **recevoir** ses factures sous forme électronique si le fournisseur les émet ainsi |
| **1er septembre 2026** | grandes entreprises et **ETI** | **émettre** en électronique **+ e-reporting** (données de transaction et de paiement) |
| **1er septembre 2027** | **PME et micro-entreprises** | **émettre** en électronique **+ e-reporting** |

★★ **La réception concerne TOUT LE MONDE dès 2026, y compris le micro-entrepreneur.** C'est l'erreur
de lecture la plus répandue : on retient « moi c'est 2027 » et on comprend qu'il n'y a rien à faire
avant. Faux — il faut être **raccordé pour recevoir** un an plus tôt. Un fournisseur qui bascule au
1er septembre 2026 enverra ses factures par plateforme, et **une facture qu'on ne peut pas recevoir
est une TVA qu'on ne peut pas déduire**.

⚠️ **« Micro-entreprise » ici n'est PAS le régime fiscal micro.** C'est la catégorie de taille :
moins de 10 salariés et chiffre d'affaires annuel ou total de bilan inférieur à 2 millions d'euros.
Une SARL avec quelques salariés est une « micro-entreprise » pour ce calendrier. PME : moins de
250 salariés, chiffre d'affaires inférieur à 50 millions d'euros ou bilan inférieur à
43 millions d'euros. Au-delà : ETI ou grande entreprise, donc **échéance 2026**. Le régime fiscal,
lui, est traité dans `micro-entreprise.md`.

### Les plateformes agréées

L'entreprise doit passer par une **plateforme agréée** — une société privée **immatriculée par
l'État**, qui transmet les factures et remonte les données à l'administration. Fournisseur et client
peuvent choisir des plateformes différentes. La liste officielle est publiée et mise à jour sur
<https://www.impots.gouv.fr/je-consulte-la-liste-des-plateformes-agreees>.

★ **Un PDF envoyé par mail n'est plus une facture électronique.** La page impots.gouv.fr du
26/05/2026 est explicite : les factures papier numérisées, les PDF ordinaires et les documents
envoyés par courriel **ne sont plus conformes**. Les formats attendus sont structurés (UBL, CII, ou
un format mixte associant données structurées et fichier image). **C'est la croyance fausse à
démonter en premier** : beaucoup de petites structures pensent être déjà en règle parce qu'elles
« envoient déjà des PDF ».

★ **L'e-reporting est une obligation distincte de la facture.** Il couvre les opérations qui
n'entrent pas dans le circuit de facture électronique B2B : ventes aux **particuliers** et aux
**opérateurs étrangers** (e-reporting de transaction), et les **encaissements** quand la TVA est due
à l'encaissement (e-reporting de paiement). ⇒ Un commerce qui ne facture qu'à des particuliers croit
n'être pas concerné : **il l'est par l'e-reporting.**

## Les mentions obligatoires

### Sur toute facture

| Mention |
|---|
| **Date d'émission** de la facture |
| **Numéro unique**, « basé sur une séquence chronologique et continue » |
| **Date de la vente ou de la prestation** (livraison ou exécution réelle) |
| **Identité du vendeur** : pour un entrepreneur individuel, nom + « Entrepreneur individuel (EI) » + adresse + **SIREN** ; pour une société, dénomination + SIREN + siège + forme juridique + montant du capital |
| **Identité de l'acheteur** : dénomination ou nom et prénom, + adresse |
| **Désignation** des produits ou services, **quantités**, **prix unitaires HT** |
| **Taux de TVA** applicables |
| **Totaux HT et TTC** |
| **Date ou délai de paiement** |
| **Conditions d'escompte** pour paiement anticipé — ou la mention « Escompte pour paiement anticipé : néant » |
| **Numéro individuel d'identification à la TVA** du vendeur, et celui du client professionnel s'il est redevable |
| **Taux des pénalités de retard** et mention de l'**indemnité forfaitaire pour frais de recouvrement** (acheteur professionnel) |

⚠️ **Le taux des pénalités et le montant de l'indemnité forfaitaire doivent FIGURER sur la facture,
même si personne ne les applique jamais.** Leur absence est une mention manquante, donc une amende.
Les taux, les délais de paiement légaux et le montant de l'indemnité sont traités par le rôle
`juriste`, fichier `contrats-commerciaux.md` — **ne les recopiez pas ici, allez-y**.

★ **Dispense limitée en dessous de 150 € HT.** Article 242 nonies A de l'annexe II au CGI, version en
vigueur au 01/01/2025 : une facture d'un montant total **inférieur ou égal à 150 € HT** peut ne pas
comporter le **numéro d'identification à la TVA** ni la **référence à la disposition d'exonération**.
⛔ **Ce n'est pas une dispense générale** : tout le reste reste dû, et la dispense tombe pour les
opérations transfrontalières et les régimes particuliers.

### Quand le client est un particulier

**La facture n'est pas toujours obligatoire, mais un document l'est souvent.**

- Pour une **prestation de services** à un particulier, **une note est obligatoire dès que le montant
  dépasse 25 € TTC**.
- Pour une **vente de biens** à un particulier : facture obligatoire **sur sa demande**, en **vente à
  distance**, et dans certains cas d'exonération de TVA.
- ★ **Mention propre au B2C** : « Lorsque la facture est adressée à un particulier, elle doit
  mentionner l'existence et la durée de la garantie légale de conformité d'au moins 2 ans »
  (électroménager, électronique, articles de sport, meubles…). **Cette mention est absente de tous
  les modèles de facture B2B** — c'est un oubli classique chez qui vend aux deux publics.

### Les mentions spécifiques, selon le cas

| Situation | Mention à porter |
|---|---|
| **Franchise en base de TVA** | mention renvoyant à l'**article 293 B du CGI** → **libellé exact, seuils et personnes concernées dans `tva.md`** |
| **Exonération de TVA** | « la référence à la disposition pertinente du code général des impôts ou à la disposition correspondante de la directive 2006/112/CE » |
| **TVA due par le client** (autoliquidation) | « **Autoliquidation** » |
| **Facture émise par le client** au nom et pour le compte du fournisseur | « **Autofacturation** » |
| **Option pour la TVA d'après les débits** | « **Option pour le paiement de la taxe d'après les débits** » |
| **Régime de la marge** | « Régime particulier-Biens d'occasion », « Régime particulier-Objets d'art », « Régime particulier-Objets de collection et d'antiquité » |

⚠️ **« TVA sur les encaissements » n'est pas une mention.** C'est le régime de droit commun des
prestations de services : rien à écrire. **La mention n'apparaît que si l'on a OPTÉ pour les
débits** — c'est-à-dire dans le cas inverse de celui qu'on croit devoir signaler.

### Les quatre nouvelles mentions liées à la facturation électronique

Fiche du 11/08/2026 : quatre mentions s'**ajoutent** (elles ne remplacent rien) — au
**1er septembre 2026** pour les grandes entreprises et ETI, au **1er septembre 2027** pour les PME et
micro-entreprises :

1. **numéro SIREN du client**, lorsqu'il s'agit d'une entreprise ;
2. **adresse de livraison** des biens, si elle diffère de l'adresse du client ;
3. **nature des opérations** facturées — livraisons de biens, prestations de services, ou les deux ;
4. mention « **Option pour le paiement de la taxe d'après les débits** » le cas échéant.

## ★★ Les sanctions : l'amende se compte PAR MENTION **ET** PAR FACTURE

C'est le point qui rend le sujet sérieux, et il est presque toujours mal compris.

**Article 1737 II du CGI**, version en vigueur du 21/02/2026 :

> « Toute omission ou inexactitude constatée dans les factures ou documents en tenant lieu mentionnés
> aux articles 289 et 290 quinquies donne lieu à l'application d'une **amende de 15 €**. Toutefois, le
> montant total des amendes dues au titre de **chaque facture** ou document ne peut excéder **le quart
> du montant** qui y est ou aurait dû y être mentionné. »

Le BOFiP (BOI-CF-INF-10-40-40, document du **12/09/2012**, à recouper) confirme la lecture :
**chaque** omission ou inexactitude est sanctionnée, et le plafond de **25 %** s'apprécie **facture
par facture**.

★★ **Conséquence concrète, et c'est là que ça se joue** : l'amende ne sanctionne pas « une erreur »,
elle sanctionne **une erreur × un nombre de mentions × un nombre de factures**. Un modèle de facture
mal fait — SIREN absent, escompte non mentionné, pénalités de retard oubliées — **fabrique
mécaniquement une amende sur chaque facture émise depuis qu'il est utilisé**. Et **le plafond est par
facture : il n'existe aucun plafond global sur un lot.** Le plafond protège la petite facture
unitaire, jamais le volume.

| Manquement | Sanction | Texte |
|---|---|---|
| Omission ou inexactitude d'une mention | **15 €** par mention et par facture, plafond **25 %** du montant de la facture | art. 1737 II CGI |
| **Ne pas délivrer** de facture ou de note **et** ne pas comptabiliser l'opération | **50 %** du montant de la transaction, plafond **375 000 €** par exercice — ramené à **5 %** (plafond **37 500 €**) si la comptabilisation régulière est prouvée | art. 1737 I-3 CGI |
| Ne pas émettre sous forme électronique quand c'est obligatoire | **50 €** par facture, plafond **15 000 €** par année civile | art. 1737 III CGI |
| Manquement de la **plateforme agréée** à la transmission des données | **50 €** par facture, plafond **45 000 €** par année civile — **à la charge de la plateforme** | art. 1737 IV CGI |
| Ne pas se doter d'une plateforme permettant de **recevoir** | mise en demeure, puis amendes progressives (**500 €** puis **1 000 €**, par période de **3** mois) ⚠️ lu en résumé, à recouper verbatim | art. 1737 IV bis CGI |

★★ **Le droit qu'on perd faute de le connaître — article 1737 V du CGI, verbatim :**

> « Les amendes mentionnées au 3 du I et aux II, III et IV du présent article **ne sont pas
> applicables en cas de première infraction commise au cours de l'année civile en cours et des trois
> années précédentes** lorsque l'infraction a été **réparée spontanément** ou **dans les trente jours
> suivant une première demande de l'administration**. »

⇒ **Celui qui découvre son erreur a un intérêt chiffré à la réparer tout de suite** — spontanément,
ou au plus tard dans les 30 jours de la première demande. Attendre, négocier, laisser courir : c'est
exactement ce qui fait tomber la tolérance. **C'est l'information la plus utile de ce fichier.**

★ **Il y a une SECONDE amende, et une seconde administration.** L'article **L441-9 du code de
commerce** sanctionne les mêmes manquements de facturation par une **amende administrative** — jusqu'à
**75 000 €** pour une personne physique et **375 000 €** pour une personne morale, **doublée**
(**150 000 €** / **750 000 €**) en cas de réitération dans un délai de **2** ans à compter du jour où
une précédente sanction est devenue définitive. Elle est prononcée par la **DGCCRF**, pas par le fisc,
et **elle se cumule avec l'amende de l'article 1737 CGI**. ⇒ Une même facture incomplète expose sur
deux fronts. Personne ne le dit au guichet.

## Numérotation et date d'émission

**Le numéro doit être « unique à chaque facture, basé sur une séquence chronologique et continue ».**

⚠️ **Un trou dans la numérotation est une anomalie visible immédiatement en contrôle** — et une
facture supprimée ne se rattrape pas : voir l'avoir ci-dessous. Les deux causes classiques de rupture
sont le **changement d'outil de facturation en cours d'année** (le nouveau logiciel repart de 1) et
la **facture annulée puis effacée**. ⛔ Ne jamais réutiliser un numéro, ne jamais rééditer une facture
sous le même numéro.

**Quand émettre :** « la facture est émise **lors de la livraison du bien ou de la réalisation de la
prestation de services** ». Différés admis :

- livraison de biens **exonérée de TVA** → au plus tard **le 15 du mois suivant** ;
- prestation de services dont **la TVA est due par le client** → au plus tard **le 15 du mois
  suivant** ;
- **facture récapitulative** (plusieurs opérations avec le même client sur un mois) → au plus tard à
  la fin du mois.

★ **Facturer tard n'est pas une négligence commerciale, c'est un manquement.** Le principe est
l'émission au moment de la livraison ou de l'exécution ; les différés sont des **exceptions
limitées**. Facturer « quand j'aurai le temps » décale le fait générateur de la TVA et fait sortir de
l'exercice comptable — c'est l'une des erreurs les plus coûteuses des petites structures, parce
qu'elle contamine à la fois la TVA et le résultat.

## Conservation : deux horloges, pas une

| Obligation | Durée | Point de départ | Texte |
|---|---|---|---|
| **Comptable** — pièces justificatives (facture client et fournisseur, bon de commande, de livraison), livres et registres | **10** ans | **clôture de l'exercice** | art. L123-22 code de commerce |
| **Fiscale** — droit de contrôle | **6** ans | **dernière opération** ou date d'établissement du document | art. L102 B du livre des procédures fiscales |

★ **Les deux durées ET les deux points de départ diffèrent.** Retenir « 6 ans » parce que c'est le
délai fiscal, c'est détruire des pièces encore exigibles au titre du code de commerce. **La règle
utilisable est : 10 ans à compter de la clôture de l'exercice.** La fiche du 08/12/2025 sur les
documents commerciaux d'une société le confirme pour les factures.

⚠️ **Page source de la fiche « délais de conservation » : 01/07/2024** — plus de six mois, à recouper.

### ⛔ Ce que ce fichier NE dit PAS encore

- **La piste d'audit fiable** — la documentation qui garantit l'authenticité de l'origine, l'intégrité
  du contenu et la lisibilité d'une facture qui n'est ni signée électroniquement ni transmise en EDI.
  **Aucune page officielle admise n'a pu être atteinte le 2026-08-17** : les pages impots.gouv.fr sur
  la facturation électronique ne la mentionnent pas, le guide pratique PDF n'a pas pu être extrait, et
  la recherche BOFiP n'a pas répondu. ⛔ **Ne l'énoncez pas comme un fait.** À chercher dans le BOFiP,
  série TVA-DECLA.
- **La forme admise de l'archivage numérique** d'une facture reçue sur papier (conditions de
  numérisation, valeur du fichier face à l'original papier, durée sous forme électronique). La fiche
  service-public donne les **durées** mais **ne distingue pas les formats**. À chercher dans le BOFiP
  et dans l'arrêté relatif à la numérisation des factures papier.

## Acompte, avoir, facture rectificative, autofacturation

**Facture d'acompte.** Une facture émise **avant le fait générateur** de la vente ou de la prestation
est une facture d'acompte.

★ **Sur une prestation de services, la facture d'acompte rend la TVA exigible tout de suite** —
avant même que la prestation soit exécutée. C'est contre-intuitif et c'est un piège de trésorerie :
on encaisse un acompte, on ne l'a pas encore « gagné », mais **la TVA est déjà due**.
⚠️ Fiche source du **01/01/2023**, à recouper. Le détail de l'exigibilité est du ressort de `tva.md`.

**Corriger une facture déjà émise — la règle tient en une phrase : on n'y touche plus.**

| Situation | Ce qu'on fait |
|---|---|
| Erreur constatée **avant** le paiement | **facture rectificative**, portant la mention « **annule et remplace la facture n°…** » |
| Correction ou annulation **après** le paiement | **facture d'avoir** |

⛔ **Ne jamais modifier, réémettre ni supprimer une facture émise.** L'avoir et la rectificative
existent précisément pour laisser la trace — et c'est cette trace qui protège la continuité de la
numérotation.

**Autofacturation.** Le vendeur ou le prestataire peut autoriser **son client** à facturer pour son
compte (**auto-facturation**) ou un **tiers** (**sous-traitance de la facturation**). La facture doit
alors porter la mention « **Autofacturation** ».
⚠️ **L'obligation reste celle du fournisseur** : c'est lui qui répond des mentions manquantes, pas le
mandataire. Déléguer sa facturation ne délègue pas la sanction.

## Le devis

**Un devis n'est obligatoire que dans des cas listés** — mais dans ces cas, son absence est
sanctionnée par une **amende administrative** pouvant atteindre **3 000 €** pour un entrepreneur
individuel et **15 000 €** pour une société.

| Activité | Devis obligatoire |
|---|---|
| Travaux et dépannages du bâtiment (maçonnerie, plomberie, électricité…) | **sans seuil** |
| Déménagement | toujours |
| Location de voiture | toujours |
| Optique médicale, appareillage auditif | toujours |
| Prestations funéraires | toujours |
| Services à la personne | dès **100 €** TTC par mois pour la prestation ou l'ensemble |
| Produits et prestations de compensation de l'autonomie | dès **500 €** TTC |
| Chirurgie esthétique | dès **300 €**, **ou** dès qu'une anesthésie générale est nécessaire |

**Valeur contractuelle** : « Le devis est une offre de contrat qui **engage le professionnel** dès lors
que le client a accepté le devis. » Le client, lui, « n'est engagé qu'à partir du moment où **il le
signe** ».

★ **Les deux parties ne sont pas engagées au même instant, et ce décalage est asymétrique contre le
professionnel** : le devis remis l'engage sur son prix et son contenu, alors que le client reste libre
jusqu'à sa signature. ⇒ **Mettre une durée de validité sur tout devis** est la seule protection
simple. Le devis du bâtiment peut être **payant**, à condition de l'avoir annoncé ; les autres devis
listés sont gratuits.

⚠️ **Fiche devis du 09/09/2022** — la plus ancienne de ce fichier, à recouper avant d'annoncer un
seuil.

## ★ Les erreurs qui coûtent le plus à une petite structure

Dans l'ordre du coût réel, pas de la gravité apparente :

1. **Un modèle de facture faux, utilisé pendant des mois.** C'est l'erreur n°1 parce qu'elle se
   multiplie : **15 €** par mention manquante **et par facture**, sans plafond global.
   Les trois oublis les plus fréquents : le **SIREN**, la mention d'**escompte** (« néant » suffit,
   mais il faut l'écrire), les **pénalités de retard** et l'indemnité forfaitaire.
2. **Une mention de TVA fausse.** Facturer de la TVA en franchise en base, oublier
   « **Autoliquidation** » sur une prestation intracommunautaire, ou porter une exonération sans sa
   référence légale. ⚠️ **Facturer de la TVA qu'on ne devait pas collecter ne s'annule pas d'un trait
   de plume** : il faut un avoir, et la TVA facturée est due. → `tva.md`.
3. **La numérotation cassée.** Changement de logiciel, facture effacée : le trou est visible
   immédiatement et déplace le contrôle du détail vers la sincérité de la comptabilité.
4. **La facture émise trop tard.** Elle décale la TVA, sort de l'exercice, et fait courir le délai de
   paiement à partir d'une date qui n'est pas celle de la prestation.
5. **Croire être en règle parce qu'on envoie des PDF.** Au 1er septembre 2026, un PDF ordinaire par
   courriel n'est pas une facture électronique — et **la réception concerne tout le monde dès cette
   date**.

★ **Et le réflexe qui sauve** : dès qu'une erreur est repérée, **la réparer immédiatement**.
L'article 1737 V neutralise l'amende pour la première infraction si la réparation est spontanée ou
faite dans les **30** jours. **La rapidité vaut plus que l'explication.**

## Ce qui reste à écrire

Par ordre d'utilité décroissante :

- **★★ La piste d'audit fiable** — la plus utile des trois manquantes, parce que c'est la condition
  qui permet aujourd'hui encore de justifier une facture non EDI, et parce qu'elle conditionne la
  **déductibilité de la TVA** chez le client. Source à atteindre : BOFiP série TVA-DECLA.
- **★ La forme admise de l'archivage numérique** : peut-on jeter l'original papier après
  numérisation, et sous quelles conditions ? Question posée en permanence, réponse non sourcée ici.
- **Les montants du IV bis de l'article 1737** (défaut de plateforme de réception), à recouper
  **verbatim** sur Légifrance — ils ne sont ici qu'en résumé.
- **La facture d'acompte** : mentions propres, articulation avec la facture de solde, imputation.
  Seule l'exigibilité de la TVA est sourcée ici.
- **Le client étranger** : facturation intracommunautaire et hors UE, mentions et autoliquidation —
  l'essentiel est déjà dans `tva.md`, il reste à traiter **la facture elle-même**.
- **Les factures des marchés publics** (Chorus Pro, délais spécifiques), régime distinct.
- **Le sort des factures en cas de cessation d'activité** : qui conserve, où, pendant combien de
  temps.
- **Les conditions générales de vente** et leur articulation avec la facture → renvoi à établir vers
  le rôle `juriste`.

## Sources

Toutes fetchées le **2026-08-17**.

- Mentions obligatoires sur une facture (page du 11/08/2026) —
  <https://entreprendre.service-public.gouv.fr/vosdroits/F31808>
- Tout savoir sur la facturation (page du 07/08/2026) —
  <https://entreprendre.service-public.gouv.fr/vosdroits/F23208>
- Se préparer à l'obligation de facturation électronique (page du 07/08/2026) —
  <https://entreprendre.service-public.gouv.fr/vosdroits/F39785>
- Devis obligatoire : activités concernées (page du 09/09/2022) —
  <https://entreprendre.service-public.gouv.fr/vosdroits/F31144>
- Délais de conservation des documents (page du 01/07/2024) —
  <https://entreprendre.service-public.gouv.fr/vosdroits/F10029>
- Documents commerciaux d'une société (page du 08/12/2025) —
  <https://entreprendre.service-public.gouv.fr/vosdroits/F37371>
- Dates d'exigibilité en matière de TVA (page du 01/01/2023) —
  <https://entreprendre.service-public.gouv.fr/vosdroits/F31412>
- Délais de paiement entre professionnels et pénalités de retard (page du 07/08/2026) —
  <https://entreprendre.service-public.gouv.fr/vosdroits/F23211>
- À partir de quand suis-je concerné par la réforme ? (page du 16/01/2026) —
  <https://www.impots.gouv.fr/professionnel/questions/partir-de-quand-suis-je-concerne-par-la-reforme-de-la-facturation>
- Je découvre la facturation électronique (page du 26/05/2026) —
  <https://www.impots.gouv.fr/professionnel/je-decouvre-la-facturation-electronique>
- Je passe à la facturation électronique (page du 10/07/2026) —
  <https://www.impots.gouv.fr/professionnel/je-passe-la-facturation-electronique>
- La facturation électronique, qu'est-ce que ça change pour moi ? —
  <https://www.impots.gouv.fr/facturation-electronique-qu-est-ce-que-ca-change-pour-moi>
- Liste des plateformes agréées —
  <https://www.impots.gouv.fr/je-consulte-la-liste-des-plateformes-agreees>
- Code général des impôts, article 1737 (version en vigueur du 21/02/2026) —
  <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046869201>
- CGI, annexe II, article 242 nonies A (version en vigueur au 01/01/2025) —
  <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000050811276>
- Code de commerce, section « La facturation et les délais de paiement », article L441-9 —
  <https://www.legifrance.gouv.fr/codes/id/LEGISCTA000038411053>
- BOFiP, infractions aux règles de facturation, BOI-CF-INF-10-40-40 (document du 12/09/2012) —
  <https://bofip.impots.gouv.fr/bofip/724-PGP.html/identifiant=BOI-CF-INF-10-40-40-20120912>

## Rappel de cadrage

Ce fichier alimente le skill `comptable`, un outil d'**aide à la décision**. Il ne remplace ni un
expert-comptable inscrit à l'Ordre, ni un avocat inscrit à un barreau, ni l'administration compétente.

⚠️ **Sur ce sujet, deux réflexes passent avant toute explication.** Le premier : **vérifier le
calendrier de la facturation électronique sur impots.gouv.fr avant d'annoncer une date** — la loi
autorise elle-même un report par décret. Le second : dire à la personne que **réparer une erreur de
facturation immédiatement peut annuler l'amende** (art. 1737 V du CGI). Le reste vient après.
