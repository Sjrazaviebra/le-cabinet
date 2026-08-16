# Contribuer

Merci. Ici, une contribution utile est presque toujours **une source**.

## La règle unique

**Aucun taux, seuil, plafond, barème ou délai n'entre dans ce dépôt sans son URL officielle et sa
date de vérification.** Pas d'exception, même pour une valeur « que tout le monde connaît ».

La raison est simple : le droit fiscal et social français change chaque année, parfois en cours
d'année. Un chiffre périmé énoncé avec assurance est plus nuisible qu'une absence de chiffre —
personne ne le vérifie, et des décisions se construisent dessus.

## Où va quoi

| Vous apportez… | Ça va dans… |
|---|---|
| Un raisonnement, une méthode, un arbre de décision, un piège à connaître | `<skill>/references/<sujet>.md` |
| Un taux, un seuil, un délai, un barème | `data/parametres.json`, **et nulle part ailleurs** |
| Un modèle de document | `avocat/assets/modeles/` |

## Sources admises

Légifrance · BOFiP · impots.gouv.fr · urssaf.fr · service-public.fr et
entreprendre.service-public.fr · BPI Création · les autorités compétentes (AMF, ACPR, CNIL,
DGCCRF, INPI, France Travail).

⛔ **Non admis** : blogs, forums, comparateurs, agrégateurs, cabinets qui font du contenu. Ils
peuvent vous aider à *trouver* le texte ; ils ne peuvent pas le *remplacer*.

## Format d'une valeur

```json
"seuils_franchise_en_base": {
  "valeur": null,
  "unite": "EUR/an",
  "a_verifier": true,
  "source": "https://www.impots.gouv.fr/professionnel/la-franchise-en-base",
  "date_verifiee": null,
  "note": "Seuil de base et seuil majoré ; règles de dépassement en cours d'année."
}
```

Quand vous vérifiez : renseignez `valeur`, mettez `a_verifier` à `false`, et datez
`date_verifiee` au jour où vous avez lu la source. C'est tout.

## Rédiger un fichier de référence

Reprenez le périmètre déjà écrit en tête du fichier — il a été pensé pour être complet. Remplacez
l'état `À ÉCRIRE` par `PARTIEL` ou `RÉDIGÉ` selon ce que vous avez couvert. Un fichier `PARTIEL`
honnête vaut mieux qu'un fichier `RÉDIGÉ` optimiste.

Écrivez pour quelqu'un qui doit **décider**, pas pour quelqu'un qui révise : la règle, son
application au cas concret, la source, et ce qui ferait changer la réponse.

## Ce que ce dépôt n'est pas

Ce n'est pas un service de conseil. Les skills disent explicitement quand s'arrêter et renvoyer à
un professionnel assuré — merci de ne pas retirer ces garde-fous, ils sont la condition pour que
l'outil reste utilisable.
