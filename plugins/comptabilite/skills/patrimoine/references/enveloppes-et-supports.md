# Les enveloppes et ce qu elles contiennent - mecanique, pas recommandation

> **État : `À ÉCRIRE`** — ce fichier est un périmètre, pas encore un contenu.
> Ne présentez jamais ce qui suit comme une réponse.

## Ce que ce fichier doit couvrir

- ⛔ CE FICHIER EXPLIQUE COMMENT CA MARCHE. Il ne dit jamais quoi prendre.
- La distinction ENVELOPPE (compte-titres, PEA, assurance-vie, PER) et SUPPORT (action, obligation, OPCVM, ETF, fonds euros, unites de compte). ★ La confondre est l erreur de vocabulaire qui rend tout le reste incomprehensible.
- Pour chaque enveloppe : plafond, disponibilite des fonds, ce qui la ferme ou la reinitialise. La FISCALITE de chacune est traitee par le role impots - renvoi, pas duplication.
- Les livrets reglementes : plafonds, taux fixe par l Etat, disponibilite.
- Ce qu est un OPCVM, un ETF, un fonds euros, une unite de compte - en mecanique.
- ★ La difference entre une garantie en CAPITAL et une absence de garantie, et qui porte le risque.

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
