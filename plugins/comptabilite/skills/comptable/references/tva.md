# TVA : franchise, régimes, clients étrangers

> **État : `RÉDIGÉ`** pour la franchise en base et les prestations B2B internationales.
> **`PARTIEL`** pour les régimes réel simplifié et réel normal. Chiffres vérifiés le
> **2026-08-16** sur `impots.gouv.fr` et `entreprendre.service-public.gouv.fr`.

## ⚠️ L'erreur n°1 : confondre le seuil de la micro et celui de la TVA

Ce sont **deux régimes totalement indépendants**, avec des seuils différents. Et l'écart est
énorme :

| | Prestations de services |
|---|---|
| Plafond du régime **micro** | **83 600 €** |
| Seuil de la **franchise en base de TVA** | **37 500 €** |

★ **On devient redevable de la TVA à moins de la moitié du plafond de la micro.** Un
micro-entrepreneur qui facture 45 000 € reste micro — et doit facturer la TVA. C'est la
mauvaise surprise la plus fréquente du régime, et elle se découvre souvent après coup, quand il
faut réclamer 20 % à des clients déjà facturés.

## La franchise en base

Elle dispense de déclarer et de payer la TVA. En contrepartie, on ne récupère pas la TVA sur ses
achats, et les factures portent la mention *« TVA non applicable, art. 293 B du CGI »*.

**Seuils applicables en 2026** *(inchangés : le seuil unique de 25 000 € prévu par la loi de
finances 2025 a été abandonné)* :

| | Prestations de services |
|---|---|
| Seuil de base (chiffre d'affaires N-1) | **37 500 €** |
| Seuil majoré (chiffre d'affaires de l'année en cours) | **41 250 €** |

**Les deux dépassements n'ont pas du tout le même effet — c'est le point à retenir :**

- **Dépassement du seuil de base (37 500 €)** → assujettissement à la TVA au **1ᵉʳ janvier de
  l'année suivante**. On a le temps de s'organiser.
- **Dépassement du seuil majoré (41 250 €)** → assujettissement **dès le premier jour du
  dépassement**. Et le passage au régime réel s'applique **rétroactivement au 1ᵉʳ janvier de
  l'année du dépassement**.

⚠️ **C'est la rétroactivité qui fait mal.** Toutes les factures émises depuis janvier deviennent
des factures qui auraient dû porter la TVA. Il faut alors soit émettre des factures
rectificatives, soit absorber la taxe sur sa marge. Un dépassement du seuil majoré non anticipé
coûte 20 % du chiffre d'affaires de l'année.

**Le réflexe à installer** : surveiller le cumul **en cours d'année**, pas à la clôture. Dès que le
chiffre d'affaires approche 37 500 €, on prépare le passage.

## ⭐ Les prestations de services à un client étranger

C'est le sujet où l'intuition est la plus trompeuse, et il concerne tout indépendant du numérique.

### Client professionnel (assujetti), dans l'UE ou hors UE

**La prestation n'est pas soumise à la TVA française.** Le lieu de la prestation se situe là où le
preneur est établi, pas où le prestataire travaille.

| Client | Facture | Mention obligatoire |
|---|---|---|
| Assujetti établi **dans l'UE** | sans TVA | **« Autoliquidation »** |
| Assujetti établi **hors UE** | sans TVA | **« TVA non applicable – art. 259-1 du CGI »** |

**Obligation déclarative pour les clients de l'UE** : une **déclaration européenne de services
(DES)** doit être déposée dans les **10 jours** du mois suivant l'exigibilité — c'est-à-dire la
réalisation de la prestation ou l'encaissement d'un acompte.

★ **Dix jours, c'est court**, et l'oubli est courant chez ceux qui découvrent qu'ils devaient la
faire. La DES n'est pas une déclaration de TVA : elle est due même quand aucune TVA n'est
collectée.

Pour les opérations B2B internationales, le **numéro de TVA intracommunautaire** remplace le SIREN
sur les documents.

### ⚠️ Le point à faire confirmer : franchise en base + client dans l'UE

Être en franchise en base dispense de facturer la TVA en France. **Cela ne semble pas dispenser des
obligations liées aux prestations B2B intracommunautaires** — obtention d'un numéro de TVA
intracommunautaire et dépôt de la DES.

**Je n'ai pas trouvé de page officielle traitant explicitement ce cas de figure**, et ce dépôt
n'admet pas les sources secondaires. La valeur est donc marquée `a_verifier` dans
`data/parametres.json`.

⇒ **Si votre situation est celle-là — franchise en base et clients professionnels dans l'UE —
posez la question au service des impôts des entreprises avant la première facture.** Une DES
oubliée se rattrape ; un numéro de TVA obtenu après coup complique toutes les factures déjà émises.

### Client particulier (non assujetti)

Règles différentes, et elles ne sont **pas couvertes ici** : le lieu d'imposition dépend de la
nature du service, avec un régime spécifique pour les services électroniques et un guichet unique.
`À ÉCRIRE`.

## Les régimes d'imposition — `À ÉCRIRE`

Réel simplifié et réel normal : conditions, périodicité des déclarations, acomptes, obligations
comptables. À traiter avec les mêmes exigences de source.

## Ce qu'il faut vérifier avant de répondre à une question de TVA

Cinq éléments, et il en manque presque toujours un :

1. **Le régime actuel** — franchise en base, réel simplifié, réel normal ?
2. **La nature de l'opération** — vente de biens ou prestation de services ? Les règles diffèrent.
3. **Qui est le client** — professionnel assujetti, ou particulier ?
4. **Où il est établi** — France, autre État membre, hors UE ?
5. **Où en est le cumul de chiffre d'affaires** de l'année en cours par rapport aux deux seuils ?

Répondre avant d'avoir ces cinq éléments, c'est jouer à pile ou face — et sur la TVA, l'erreur se
paie en pourcentage du chiffre d'affaires.

## Sources

- Franchise en base de TVA —
  <https://entreprendre.service-public.gouv.fr/vosdroits/F21746>
- Suppression du seuil unique de franchise —
  <https://entreprendre.service-public.gouv.fr/actualites/A17995>
- Prestations entre assujettis —
  <https://www.impots.gouv.fr/professionnel/prestations-entre-assujettis>
- TVA, entreprise hors UE —
  <https://www.impots.gouv.fr/international-professionnel/tva-entreprise-hors-ue>
- BOFiP, lieu des prestations de services —
  <https://bofip.impots.gouv.fr/bofip/1488-PGP.html/identifiant=BOI-TVA-CHAMP-20-50-20-20190925>
- Les régimes d'imposition à la TVA —
  <https://www.impots.gouv.fr/professionnel/les-regimes-dimposition-la-tva>

## Rappel de cadrage

Ce fichier alimente le skill `comptable`, un outil d'**aide à la décision**. Il ne remplace pas un
expert-comptable inscrit à l'Ordre. Sur la TVA internationale en particulier, une erreur de
qualification se répercute sur toutes les factures d'un exercice — faites valider votre cas avant
d'émettre la première.
