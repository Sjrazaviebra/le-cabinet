# Propriété intellectuelle : code, cession, open source

> **État : `PARTIEL`** — la **titularité des droits sur un logiciel** et le **formalisme de la
> cession** sont rédigés et vérifiés le **2026-08-17** sur Légifrance. Les licences open source, les
> marques et les brevets restent `À ÉCRIRE`.

## ⚠️ Le logiciel est une exception : la règle générale du droit d'auteur ne s'y applique pas

C'est le point qui retourne l'intuition de presque tous les développeurs, et il faut le poser en
premier.

**Article L113-9 du code de la propriété intellectuelle** : sauf dispositions statutaires ou
stipulations contraires, les **droits patrimoniaux** sur les **logiciels et leur documentation**
créés par un ou plusieurs **employés dans l'exercice de leurs fonctions** ou d'après les
**instructions de leur employeur** sont **dévolus à l'employeur**, seul habilité à les exercer.

- **Aucune cession n'est nécessaire.** La dévolution est **automatique**. C'est l'inverse du régime
  de droit commun du droit d'auteur, où l'employeur doit obtenir une cession écrite.
- **Aucune rémunération supplémentaire** n'est due de ce seul fait.
- La disposition s'applique aussi aux **agents de l'État**, des collectivités et des établissements
  publics administratifs.
- Les litiges relèvent du **tribunal judiciaire du siège social de l'employeur**.

### Le miroir, et c'est là que l'argent se perd

**La dévolution automatique ne joue QUE pour les salariés.**

Un **indépendant**, un **freelance**, un **stagiaire non salarié**, un **associé non employé**, un
**ami qui a donné un coup de main** : rien ne se transfère automatiquement. **Sans cession écrite, ils
restent titulaires des droits sur le code qu'ils ont écrit** — même si la facture a été payée, même
si le code tourne en production chez le client depuis trois ans.

★ **Conséquence concrète, et elle est brutale** : une entreprise qui a fait développer son produit par
des freelances sans cession valable **ne détient pas son propre produit**. C'est le point qui fait
échouer les audits juridiques lors d'une levée de fonds ou d'un rachat — et il se découvre au pire
moment.

*(Un régime particulier existe pour les auteurs de logiciels non salariés accueillis par une
personne morale réalisant de la recherche : voir l'article L113-9-1, issu de l'ordonnance du
15 décembre 2021. Cas limité, à vérifier avant de s'en prévaloir.)*

## Le formalisme de la cession : quatre éléments, à peine de nullité

**Article L131-3 du code de la propriété intellectuelle** : la transmission des droits est
subordonnée à ce que **chacun des droits cédés fasse l'objet d'une mention distincte** dans l'acte de
cession, et à ce que le **domaine d'exploitation** des droits cédés soit délimité :

1. quant à son **étendue** ;
2. quant à sa **destination** ;
3. quant au **lieu** ;
4. quant à la **durée**.

⇒ **Une clause du type « le prestataire cède au client tous ses droits sur les livrables » ne remplit
aucune de ces quatre conditions.** C'est la formule la plus répandue dans les contrats de prestation
informatique, et c'est celle qui expose le plus.

★ **Et elle coupe dans les deux sens**, ce qu'il faut dire à qui que l'on conseille :

- **Le client** croit avoir acquis les droits et ne les a peut-être pas.
- **Le prestataire** croit s'être dépouillé et détient peut-être encore des droits qu'il pourrait
  faire valoir.

Aucun des deux ne le sait, jusqu'au jour où l'un des deux a besoin de le savoir.

## Ce qu'une cession bien rédigée doit énoncer

- **Quels droits** précisément : reproduction, représentation, adaptation, traduction, modification,
  correction, décompilation, distribution — chacun **mentionné distinctement**.
- **Pour quel usage** — la destination.
- **Sur quel territoire** — le lieu. « Le monde entier » est une réponse valable, encore faut-il
  l'écrire.
- **Pour combien de temps** — la durée. « La durée légale de protection des droits d'auteur » est une
  réponse valable, elle aussi à écrire.
- **Le code source et la documentation** sont-ils remis, et sous quelle forme ? Une cession de droits
  n'est pas une remise de sources : ce sont deux obligations distinctes, et l'oubli de la seconde
  rend la première inutilisable en pratique.
- **Le sort des composants tiers** et des bibliothèques open source intégrés.

⚠️ **Le droit moral n'est pas cessible.** On peut aménager son exercice, on ne peut pas l'acheter. Une
clause qui prétend céder le droit moral est, sur ce point, sans effet.

## Ce qui reste à écrire

- **Les licences open source** : compatibilité entre licences, obligations de la GPL et des licences
  à réciprocité, ce que publier sous MIT engage réellement, l'audit des dépendances.
- **Les marques** : disponibilité, classes, dépôt à l'INPI, déchéance faute d'usage.
- **Les brevets** et l'exclusion des programmes d'ordinateur « en tant que tels ».
- **Les bases de données** et leur protection propre.
- **Le code produit avec l'aide d'une IA** : la titularité, et l'état des sources officielles sur
  ce point — sujet mouvant, à traiter avec des sources datées.

## Ce qui vit ailleurs

- **La clause de cession dans un contrat de prestation** et sa négociation → `contrats-commerciaux.md`.
- **Le contrat de travail** et les clauses qui l'entourent → skill `travail`.
- **Le régime fiscal** des redevances et cessions → skill `impots`.

## Sources

- Article L113-9 du code de la propriété intellectuelle —
  <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000039279818>
- Article L113-9-1 (auteurs non salariés accueillis en recherche) —
  <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044502241/>
- Article L131-3, formalisme de la cession —
  <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006278958>
- Titulaires du droit d'auteur, articles L113-1 à L113-10 —
  <https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069414/LEGISCTA000006161635/>
- Exploitation des droits, articles L131-1 et suivants —
  <https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069414/LEGISCTA000006161639/>
- INPI — <https://www.inpi.fr/>

## Rappel de cadrage

Ce fichier alimente le skill `juriste`, un outil d'**aide à la décision**. Une cession de droits mal
rédigée ne se répare pas toujours après coup : si le titulaire d'origine n'est plus joignable, ou
n'a plus d'intérêt à signer, le défaut devient définitif. **Faites rédiger ou relire toute cession
par un avocat avant signature** — c'est le type d'acte où le coût du conseil est dérisoire au regard
de l'enjeu.
