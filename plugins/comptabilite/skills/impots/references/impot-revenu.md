# Impôt sur le revenu : barème, foyer, réductions

> **État : `PARTIEL`** — le barème, le mécanisme du quotient familial et la distinction taux marginal /
> taux moyen sont vérifiés le **2026-08-17** (page service-public du **15/04/2026**). La décote, le
> détail des réductions et crédits, et le prélèvement à la source restent `À ÉCRIRE`.

## Le barème progressif — revenus 2025, imposition 2026

| Tranche de revenu imposable par part | Taux |
|---|---|
| jusqu'à **11 600 €** | **0 %** |
| de **11 601 €** à **29 579 €** | **11 %** |
| de **29 580 €** à **84 577 €** | **30 %** |
| de **84 578 €** à **181 917 €** | **41 %** |
| au-delà de **181 917 €** | **45 %** |

## ★★ La croyance fausse la plus répandue de toute la fiscalité française

**« Si je passe dans la tranche à 30 %, tout mon revenu est taxé à 30 %. » C'est faux.**

Le barème est **progressif par tranches** : seule la **fraction** du revenu qui dépasse une borne est
imposée au taux de la tranche suivante. Passer une borne ne réimpose **jamais** ce qui est en dessous.

⇒ **Deux taux à ne pas confondre** :

- le **taux marginal d'imposition (TMI)** = le taux de la **dernière** tranche atteinte ;
- le **taux moyen** = l'impôt total divisé par le revenu total, **toujours plus bas que le TMI**.

★★ **Cette confusion fait refuser des augmentations, des heures supplémentaires et des missions.**
C'est la première chose à corriger dans une conversation fiscale — et le TMI reste néanmoins le bon
taux pour arbitrer *une* décision marginale : un versement sur un plan d'épargne retraite, une charge
déductible, un revenu supplémentaire. **Le TMI sert à décider, le taux moyen à comprendre ce qu'on
paie.** ⇒ `epargne-retraite-per.md`.

## Le foyer fiscal et le quotient familial

Le revenu imposable est **divisé par le nombre de parts** du foyer, qui dépend de la situation
matrimoniale et des personnes à charge ; l'impôt est calculé sur ce quotient, puis remultiplié.

★ **C'est ce mécanisme, et non un abattement, qui fait la différence pour une famille** : diviser
avant d'appliquer un barème progressif fait tomber le revenu par part dans des tranches plus basses.

⚠️ **L'avantage est plafonné** — le « plafonnement du quotient familial ». **Le montant lu est de
1 807 €, mais l'assiette exacte — par demi-part ou par enfant — n'a pas été confirmée sur la page
source.** L'entrée est donc en `a_verifier: true` dans `data/parametres.json`. ⛔ **Ne l'annoncez pas
comme un chiffre acquis** : c'est précisément le genre de valeur qu'on croit connaître et qu'on énonce
de travers.

## Ce qui reste à écrire — par ordre d'utilité

- ★★ Le **prélèvement à la source** : taux personnalisé, **taux neutre**, **taux individualisé** au
  sein d'un couple, la **modulation** en cours d'année et les acomptes des indépendants. **C'est ce que
  les gens manipulent réellement**, et c'est le trou le plus visible de ce fichier.
- ★ La **décote** : elle annule ou réduit l'impôt des revenus modestes et explique pourquoi entrer
  dans une tranche ne signifie pas payer.
- Les **réductions et crédits d'impôt** fréquents avec leurs **conditions réelles** : dons, emploi à
  domicile, garde d'enfants, travaux — et l'annexe **2042-RICI** déjà signalée dans
  `declaration-annuelle.md` comme la plus oubliée.
- Les **catégories de revenus** et leur traitement : traitements et salaires et l'abattement de 10 %
  ou les frais réels, BIC, BNC, revenus fonciers, revenus de capitaux mobiliers.
- Le **rattachement** d'un enfant majeur : le calcul comparatif qui décide s'il est favorable.
- Les **personnes à charge**, l'année de mariage, de divorce ou de décès.
- La **contribution exceptionnelle sur les hauts revenus** → `hauts-revenus-cehr-cdhr.md`.

## Sources

- Barème de l'impôt sur le revenu —
  <https://www.service-public.gouv.fr/particuliers/vosdroits/F1419>
- Direction générale des finances publiques — <https://www.impots.gouv.fr/>
- Documentation fiscale officielle — <https://bofip.impots.gouv.fr/>
- Déclaration et calendrier → `declaration-annuelle.md`

## Rappel de cadrage

Ce fichier alimente le skill `impots`, un outil d'**aide à la décision**. Il ne remplace pas un
professionnel inscrit et assuré, et **il ne calcule aucun impôt** : le barème sert à comprendre un
ordre de grandeur et à arbitrer une décision marginale, pas à produire un montant. ⚠️ **Le barème est
révisé chaque année** — vérifiez le millésime avant de vous en servir.
