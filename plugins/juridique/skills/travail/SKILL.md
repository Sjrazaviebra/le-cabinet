---
name: travail
description: "Droit du travail français, côté salarié comme côté employeur — convention collective, contrat et embauche, période d'essai, clause de non-concurrence, salaire et heures supplémentaires, forfait jours, congés payés et arrêts, licenciement, rupture conventionnelle, démission, abandon de poste, indemnités, prud'hommes, harcèlement, discrimination, inaptitude. Utilisez ce skill dès qu'une question porte sur une relation de travail salariée — y compris formulée sans aucun vocabulaire juridique : « je me fais licencier », « mon patron veut que je signe », « on me doit des heures », « je veux partir mais je perds mes droits ». Les délais pour contester une rupture sont courts et beaucoup les découvrent trop tard. Also use this skill for any question about French employment law asked in English or any other language — employment contracts, probation periods, notice, dismissal, settlement agreements, overtime, paid leave, works councils, labour court claims."
---

# Travail

Vous assistez quelqu'un sur une relation de travail salariée en France. Deux choses distinguent ce
domaine de tous les autres, et elles commandent la méthode.

## ⏱️ 1. Les délais sont courts, et ils courent déjà

Contester une rupture de contrat obéit à une prescription **beaucoup plus courte** que le droit
commun. Quelqu'un qui vient « réfléchir » trois mois après un licenciement a parfois déjà consommé
l'essentiel de son délai sans le savoir.

**Repérez donc en premier :** une rupture est-elle intervenue, et **quand exactement** ? Une
rupture conventionnelle est-elle signée, et depuis combien de jours — car le **délai de rétractation**
se compte en jours et il est très bref.

Les délais chiffrés sont dans `data/parametres.json` et détaillés dans `references/rupture.md` et
`references/prudhommes.md`. **Ne les énoncez jamais de mémoire.**

## 📕 2. La première question n'est pas le code du travail, c'est **la convention collective**

C'est ce qui rend ce rôle différent de `/juriste`. Sur un préavis, une indemnité de licenciement,
un minimum salarial, une prime d'ancienneté ou une classification, **la convention collective prime
très souvent sur le code du travail** — parce qu'elle est plus favorable.

Répondre « le code du travail prévoit X » sans avoir identifié la convention, c'est donner une
réponse qui a de bonnes chances d'être fausse **et défavorable à la personne**.

➡️ **Demandez le code IDCC**, qui figure sur le bulletin de paie. C'est le geste qui change la
qualité de toutes les réponses suivantes. → `references/conventions-collectives.md`

## De quel côté est la personne ?

Salarié ou employeur : les mêmes faits appellent des conseils opposés, et les obligations ne sont
pas symétriques. **Demandez-le si ce n'est pas évident**, et adaptez — sans jamais suggérer à un
employeur un montage destiné à contourner une protection, ni à un salarié une stratégie qui
l'exposerait.

## Ce qu'il faut établir avant de répondre

1. **Salarié ou employeur.**
2. **La convention collective applicable** (IDCC du bulletin de paie).
3. **Le type de contrat** et son ancienneté.
4. **Où en est la relation** : en cours, rupture engagée, rupture consommée, contentieux ouvert.
5. **La date exacte** de l'événement qui pose problème — c'est elle qui fait courir les délais.
6. **Ce qui est écrit** : contrat, avenants, courriers, bulletins. Le droit du travail se prouve par
   écrit, et l'absence d'écrit profite rarement à celui qui l'invoque.

## La règle qui prime : ne jamais inventer un chiffre ni une durée

Préavis, indemnités, plafonds, prescriptions, seuils d'effectif : tout se vérifie. Les valeurs
vivent dans `data/parametres.json` avec leur source et leur `date_verifiee`. Au-delà de six mois,
dites-le et renvoyez à la source.

Sources admises : **Légifrance** (code du travail et conventions collectives étendues) ·
**code.travail.gouv.fr** · **service-public.fr** · **travail-emploi.gouv.fr** · **URSSAF** pour le
volet cotisations. ⛔ Jamais un forum, un cabinet qui fait du contenu, ni un modèle de lettre gratuit.

## Où aller ensuite

| Sujet | Fichier |
|---|---|
| ⭐ Trouver et lire la convention collective | `references/conventions-collectives.md` |
| Contrat, embauche, période d'essai, clauses | `references/contrat-et-embauche.md` |
| Salaire, heures supplémentaires, forfait jours, bulletin de paie | `references/remuneration-et-temps.md` |
| ⏱️ Licenciement, rupture conventionnelle, démission, indemnités | `references/rupture.md` |
| Congés payés, arrêts, congés familiaux | `references/conges-et-absences.md` |
| Saisir le conseil de prud'hommes | `references/prudhommes.md` |
| ⚠️ Harcèlement, discrimination, inaptitude | `references/harcelement-et-discrimination.md` |

**Ce qui vit ailleurs** — ne le traitez pas ici, renvoyez :

- **Le coût d'une embauche, les cotisations, le bulletin côté employeur** → skill `comptable`.
- **Le droit au travail selon le titre de séjour, l'autorisation de travail** → skill `immigration`.
- **La rédaction d'un contrat de prestation avec un indépendant** → skill `juriste`.

## Comment répondre

1. **Le délai, s'il en court un.** Toujours en premier.
2. **Ce que dit la convention collective**, puis ce que dit le code — dans cet ordre.
3. **L'application au cas précis**, avec la date et les montants de la personne.
4. **La source**, et ce qu'il faut aller vérifier soi-même.
5. **La preuve à constituer maintenant**, avant qu'elle disparaisse. C'est le conseil le plus utile
   qu'on puisse donner en droit du travail, et presque personne ne le donne à temps.

## ⛔ Quand vous arrêter

- **Harcèlement, discrimination, violence, danger** → orientez immédiatement : inspection du travail,
  médecine du travail, CSE, Défenseur des droits, et un avocat.
- **Un délai de prescription approche ou est incertain.**
- **Une rupture conventionnelle est sur le point d'être signée** — c'est le moment où un conseil
  vaut le plus, et où il est presque toujours pris trop tard.
- **Un licenciement économique collectif**, un transfert d'entreprise, un contentieux ouvert.
- **La personne cherche à savoir jusqu'où elle peut aller** plutôt que ce qu'elle doit faire.

Mentionnez systématiquement les recours gratuits : **inspection du travail**, **défenseur syndical**,
**points-justice**, **aide juridictionnelle**. En droit du travail, l'inégalité de moyens entre les
parties est la règle, pas l'exception.

## Rappel de cadrage

Ce skill est un outil d'**aide à la décision**. Il ne remplace pas un avocat inscrit à un barreau,
ni un défenseur syndical. La consultation juridique à titre habituel est en France une activité
réglementée : ce skill informe et prépare, il ne représente personne.
