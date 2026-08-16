# Micro-entreprise : seuils, abattements, cotisations, obligations

> **État : `RÉDIGÉ`** pour le volet fiscal (seuils, abattements, versement libératoire),
> **`PARTIEL`** pour les cotisations sociales — le taux n'a pas pu être confirmé sur une page
> officielle et reste `a_verifier`. Chiffres vérifiés le **2026-08-16** sur
> `entreprendre.service-public.gouv.fr` (page datée du 13/05/2026).

## Ce que « micro » désigne exactement

La micro-entreprise n'est **pas une forme juridique**. C'est une **entreprise individuelle** à
laquelle s'applique un **régime fiscal simplifié** — et, automatiquement, le **régime micro-social**
pour le calcul des cotisations. On ne « crée pas une micro-entreprise » : on crée une entreprise
individuelle et on relève du régime micro tant qu'on reste sous les seuils.

Cette précision n'est pas de la pédanterie : elle explique pourquoi on ne « transforme » pas une
micro en société — on **crée une société** et on ferme l'entreprise individuelle.

## Les seuils de chiffre d'affaires

| Activité | Seuil |
|---|---|
| Commerce, hébergement (BIC) | **203 100 €** |
| **Prestations de services et professions libérales** | **83 600 €** |
| Location de meublés non classés | **15 000 €** |
| Activités mixtes — seuil global | **203 100 €** |

⚠️ **Le dépassement d'une seule année ne fait pas sortir du régime.** Il faut un dépassement sur
**deux années consécutives** (N-1 *et* N-2). C'est l'erreur la plus répandue : beaucoup basculent
en société dans la panique après une bonne année isolée.

★ **Ne confondez pas ces seuils avec ceux de la TVA.** Ce sont deux régimes indépendants, avec des
seuils différents : on peut rester en micro tout en devenant redevable de la TVA. Voir `tva.md`.

## Les abattements forfaitaires

Le régime micro ne déduit pas les frais réels : il applique un **abattement forfaitaire** sur le
chiffre d'affaires, et l'impôt porte sur le reste.

| Activité | Abattement |
|---|---|
| Commerce et hébergement (BIC) | **71 %** |
| **Prestations de services (BIC)** | **50 %** |
| **Activités libérales (BNC)** | **34 %** |
| Location de meublés classés | 50 % |
| Location de meublés non classés | 30 % |

Abattement minimum : **305 €** (610 € pour les activités mixtes).

★ **C'est là que se joue l'intérêt réel du régime.** L'abattement est un forfait, pas un
remboursement : si vos frais réels dépassent l'abattement, vous payez de l'impôt sur de l'argent que
vous n'avez pas gagné. En BNC, l'abattement de 34 % suppose donc que vos charges représentent moins
d'un tiers du chiffre d'affaires — vrai pour une activité intellectuelle sans matériel lourd,
faux dès qu'il y a de la sous-traitance, du matériel ou des licences.

**La question à poser** : *« quelles sont vos charges annuelles, en euros ? »* Comparez-les à
l'abattement. Si elles le dépassent nettement et durablement, le régime réel devient plus favorable
— et c'est un vrai déclencheur de changement, bien avant les seuils.

## Le versement libératoire de l'impôt sur le revenu

Option qui remplace l'imposition au barème par un prélèvement proportionnel au chiffre d'affaires :

| Activité | Taux |
|---|---|
| BIC commerce | **1 %** |
| Autres BIC (prestations de services) | **1,7 %** |
| **BNC** | **2,2 %** |

**Condition d'accès** : le revenu fiscal de référence du foyer (N-2) ne doit pas dépasser un
plafond, de **29 579 €** pour une personne seule à **88 737 €** pour un couple avec deux enfants.

⚠️ **L'option n'est pas toujours avantageuse**, et c'est contre-intuitif : le versement libératoire
se paie **dès le premier euro de chiffre d'affaires**, alors que le barème progressif comporte une
tranche à 0 %. Un micro-entrepreneur dont le foyer est peu imposable **paie plus** avec l'option.

**La règle pratique** : le versement libératoire est intéressant quand le foyer est déjà imposé à
un taux marginal supérieur au taux de l'option. Il ne l'est pas quand le revenu du foyer est faible
— typiquement une première année, ou un foyer dont l'autre revenu est modeste.

## Cotisations sociales — `a_verifier`

Le régime micro-social calcule les cotisations en pourcentage du **chiffre d'affaires encaissé**,
sans possibilité de déduire quoi que ce soit. Une documentation secondaire annonce un taux de
**25,6 %** pour « autre prestation de services » au 1ᵉʳ janvier 2026, **mais je n'ai pas pu
confirmer ce chiffre sur une page officielle Urssaf** — elle n'a pas répondu au moment de la
vérification. Le taux reste donc `a_verifier` dans `data/parametres.json`.

★ **Conséquence structurelle, elle, certaine** : on cotise sur le chiffre d'affaires, pas sur le
bénéfice. **Un mois à perte coûte quand même des cotisations.** C'est le revers exact de la
simplicité du régime.

## Les obligations réelles

Beaucoup moins lourdes qu'en société, mais elles existent :

- **Déclarer le chiffre d'affaires** chaque mois ou chaque trimestre, **même à zéro**.
- **Tenir un livre des recettes** (et un registre des achats pour les activités d'achat-revente).
- **Un compte bancaire dédié** dès que l'activité dépasse un certain niveau de chiffre d'affaires
  sur deux années consécutives — un compte courant ordinaire suffit, un « compte pro » facturé
  n'est pas obligatoire.
- **La CFE** — cotisation foncière des entreprises, due même sans local, avec une exonération la
  première année.
- **Les mentions obligatoires sur les factures**, voir `facturation.md`.

## Quand la micro cesse d'être le bon choix

Quatre déclencheurs, par ordre de fréquence réelle :

1. **Les charges dépassent durablement l'abattement** — le plus fréquent, et le plus ignoré.
2. **On veut embaucher** — les salaires ne se déduisent pas d'un abattement forfaitaire. La micro
   n'est pas conçue pour employer. → `formes-juridiques.md`
3. **Le chiffre d'affaires approche les seuils** sur deux années consécutives.
4. **Un client important exige une société** — cela arrive, surtout à l'international.

★ Le bon réflexe : **fixer le déclencheur à l'avance**, quand tout va bien. Une bascule décidée
dans l'urgence après une bonne année se paie en trésorerie et en erreurs.

## Sources

- Régime fiscal de la micro-entreprise —
  <https://entreprendre.service-public.gouv.fr/vosdroits/F23267>
- Versement libératoire — <https://www.impots.gouv.fr/professionnel/le-versement-liberatoire>
- Statut du micro-entrepreneur, Urssaf —
  <https://www.autoentrepreneur.urssaf.fr/portail/accueil/sinformer-sur-le-statut/lessentiel-du-statut.html>
- Seuils 2026 —
  <https://www.autoentrepreneur.urssaf.fr/portail/accueil/sinformer-sur-le-statut/toutes-les-actualites/2026--modification-des-seuils-de.html>

## Rappel de cadrage

Ce fichier alimente le skill `comptable`, un outil d'**aide à la décision**. Il ne remplace pas un
expert-comptable inscrit à l'Ordre.
