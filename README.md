# le-cabinet

**Deux skills pour agents IA : un comptable et un avocat, en droit français.**
Entreprise **et** vie privée.

> ⚖️ **Ces skills ne remplacent ni un expert-comptable inscrit à l'Ordre, ni un avocat inscrit
> à un barreau.** Ce sont des outils d'**aide à la décision** : ils structurent une question,
> posent les bonnes, et disent **où vérifier**. Pour tout acte engageant — statuts, contrat signé,
> déclaration fiscale, contentieux — consultez un professionnel couvert par une assurance
> responsabilité civile professionnelle.

---

## Ce que c'est

| Skill | Couvre |
|---|---|
| **`comptable`** | Comptabilité et fiscalité, côté entreprise **et** côté particulier : formes juridiques, micro-entreprise, TVA, PCG et écritures, clôture et liasse, facturation, impôt sur le revenu, revenus financiers, aides et chômage, paie. |
| **`avocat`** | Droit, côté entreprise **et** côté particulier : sociétés, contrats commerciaux, international, propriété intellectuelle, activités réglementées, travail, consommation, données personnelles, vie privée, procédure. |

## ★ Ce qui distingue ce dépôt : **aucun chiffre n'est écrit de mémoire**

Le droit fiscal et social français change tous les ans, parfois en cours d'année. Un skill qui
récite un taux de 2023 avec assurance est **plus dangereux que pas de skill du tout** : il produit
une erreur confiante, que l'utilisateur n'a aucune raison de vérifier.

Donc, ici :

1. **Les fichiers de méthode ne contiennent pas de valeurs volatiles.** Ils contiennent le
   *raisonnement*, les *questions à poser*, les *arbres de décision*, et **l'adresse officielle
   où lire la valeur**.
2. **Les valeurs volatiles vivent dans [`data/parametres.json`](data/parametres.json)**, chacune
   avec sa `source` (URL officielle) et sa `date_verifiee`.
3. **Le skill refuse d'affirmer une valeur périmée.** Si `date_verifiee` a plus de 6 mois, il le
   dit et renvoie à la source au lieu de deviner.

Sources retenues, par ordre d'autorité : **Légifrance** · **BOFiP** · **impots.gouv.fr** ·
**urssaf.fr** · **service-public.fr** / **entreprendre.service-public.fr** · **BPI Création**.
Un blog, un forum ou un comparateur n'est jamais une source.

## Installation

Depuis un terminal `claude` interactif :

```bash
/plugin marketplace add Sjrazaviebra/le-cabinet
```

Ou copiez le dossier `comptable/` et/ou `avocat/` dans vos skills.

## État d'avancement

Ce dépôt est en construction publique. Chaque fichier de référence porte en tête son état :
**`RÉDIGÉ`**, **`PARTIEL`** ou **`À ÉCRIRE`**. Un fichier `À ÉCRIRE` est un titre, pas un contenu —
il n'induit personne en erreur. Voir [`docs/avancement.md`](docs/avancement.md).

## Licence

MIT. Utilisation libre, y compris commerciale.

## Contribuer

Une contribution utile ici, c'est presque toujours **une source**. Si vous corrigez un chiffre,
joignez l'URL officielle et la date. Voir [`CONTRIBUTING.md`](CONTRIBUTING.md).
