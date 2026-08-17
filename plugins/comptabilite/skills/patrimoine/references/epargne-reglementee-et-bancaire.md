# Epargne reglementee et produits bancaires

> **État : `À ÉCRIRE`** — ce fichier est un périmètre, pas encore un contenu.
> Ne présentez jamais ce qui suit comme une réponse.

## Ce que ce fichier doit couvrir

- Les livrets reglementes : conditions d ouverture, plafonds, taux et qui le fixe, cumul possible entre livrets.
- ★ Le taux administre : comment il est revise et par qui - donc pourquoi il n a pas a etre negocie.
- Les comptes a terme et les plans d epargne logement : blocage, remuneration, conditions.
- ★ La GARANTIE DES DEPOTS : son plafond par personne et par etablissement, ce qu elle couvre et ce qu elle NE couvre pas (les titres relevent d une autre garantie).
- Les comptes multiples dans un meme etablissement : la garantie se compte par etablissement, pas par compte.
- Renvoi au role financement pour les frais bancaires et les incidents.

## Sources à utiliser

Toute valeur chiffrée va dans `data/parametres.json` avec sa source officielle et sa
`date_verifiee`. ⚠️ Les plafonds et les taux réglementés **changent chaque année**.

- <https://www.amf-france.org/> — dont les guides pedagogiques et la **liste noire**
- <https://www.abe-infoservice.fr/> — Assurance Banque Epargne Info Service (AMF + ACPR + Banque de France)
- <https://acpr.banque-france.fr/> — dont le **Regafi** et les mises en garde
- <https://www.banque-france.fr/> — education financiere, surendettement
- <https://www.service-public.gouv.fr/>
- <https://www.legifrance.gouv.fr/codes/id/LEGITEXT000006072026/> — code monetaire et financier

## Rappel de cadrage

Ce fichier alimente le skill `patrimoine`, un outil d'**information et de protection**.
⛔ Il **n'émet aucune recommandation personnalisée** portant sur un instrument financier :
c'est le **conseil en investissement**, service réglementé — voir
`activites-reglementees.md` du rôle `juriste` et [`docs/taxonomie-comptabilite.md`]
pour l'analyse de la frontière. Expliquer une mécanique est licite ; dire *« prenez
ceci »* ne l'est pas.
