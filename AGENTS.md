# AGENTS.md — utiliser ce dépôt avec n'importe quel agent

Ce dépôt est packagé pour **Claude Code** (skills et plugins), mais **son contenu n'a rien de
propriétaire** : ce sont des fichiers Markdown et JSON. Ce fichier explique comment s'en servir
ailleurs — Cursor, Copilot, Windsurf, un GPT personnalisé, un RAG maison, un modèle local.

## Ce qui est portable, et ce qui ne l'est pas

| Portable partout | Propre à Claude Code |
|---|---|
| Les **61 fichiers `references/*.md`** — aucune syntaxe spécifique à l'intérieur | Le frontmatter YAML de `SKILL.md` (`name`, `description`) |
| Les **7 `data/parametres.json`** — sources et dates lisibles par n'importe quel outil | `.claude-plugin/plugin.json` et `marketplace.json` |
| Les **scripts de `scripts/`** — Python standard, aucune dépendance | Le **routage automatique** : Claude lit la `description` et charge le bon rôle seul |

⇒ Ailleurs, **le contenu marche tel quel ; c'est l'aiguillage qu'il faut refaire à la main.** Le
frontmatter YAML est inoffensif : les autres outils l'ignorent.

## Les sept rôles, et lequel charger

| Rôle | Charger quand la question porte sur… |
|---|---|
| `comptable` | une **entreprise** : forme juridique, micro, TVA, facturation, paie, clôture |
| `impots` | un **particulier** : déclaration, barème, placements, immobilier, IFI, contrôle |
| `juriste` | l'**activité** : contrats, sociétés, données personnelles, consommation, procédure |
| `travail` | un **salarié** : contrat, rupture, salaire, congés, harcèlement, prud'hommes |
| `logement` | un **bail** : entrée, charges, congé, dépôt de garantie, impayés, copropriété |
| `famille` | le **couple et la filiation** : union, séparation, enfants, succession, protection |
| `immigration` | le **séjour** : titres, travail, famille, recours, naturalisation |
| `financement` | l'**argent de l'activité** : compte pro et droit au compte, crédit et rupture de crédit, caution du dirigeant, trésorerie, médiation du crédit, assurances obligatoires |
| `patrimoine` | l'**argent personnel** : arnaques et vérification d'un agrément, enveloppes et supports, frais, risque et horizon, épargne réglementée, retraite, budget et surendettement |

⛔ **Deux règles à conserver pour `financement` et `patrimoine`, sous peine de faire commettre à votre
agent une infraction** : ils **informent** et **expliquent**, ils n'émettent **aucune recommandation
personnalisée portant sur un instrument financier** — c'est le conseil en investissement, service
réglementé. Et ils ne recommandent **aucun établissement, produit ou prestataire**. L'analyse de la
frontière est dans [`docs/taxonomie-comptabilite.md`](docs/taxonomie-comptabilite.md).

**Un rôle n'est pas un thème** : c'est une méthode d'entrée, une posture et des règles d'arrêt. Le
critère qui décide qu'un sujet mérite son propre rôle est dans [`docs/taxonomie.md`](docs/taxonomie.md).

## La règle qui doit survivre au portage — c'est la seule qui compte

Chaque rôle a un `data/parametres.json` où **toute valeur porte sa `source` officielle et sa
`date_verifiee`**. Trois conséquences à préserver quel que soit l'outil :

1. **Le JSON fait autorité.** En cas de divergence avec un fichier de méthode, le JSON gagne.
2. **Une valeur `a_verifier: true` n'est pas une valeur.** Elle se dit comme telle, avec un renvoi à
   la source — jamais énoncée comme un fait.
3. **Au-delà de six mois, la valeur est périmée** : l'agent doit le dire et renvoyer à la source
   plutôt que d'actualiser au jugé.

⛔ **Si votre portage perd ces trois règles, il perd la seule chose qui distingue ce dépôt** d'un
résumé de droit français écrit de mémoire.

## Recettes concrètes

**GPT personnalisé / assistant à instructions**
Collez le `SKILL.md` du rôle en instructions système, chargez ses `references/*.md` et son
`parametres.json` en fichiers de connaissance. ⚠️ Un assistant = **un** rôle : l'aiguillage entre les
sept n'existe pas hors de Claude, donc sept assistants, ou un routeur écrit à la main sur le tableau
ci-dessus.

**Cursor / Windsurf / Copilot**
Référencez le `SKILL.md` du rôle comme fichier de règles et laissez les `references/` dans le
contexte du dépôt.

**RAG maison ou modèle local**
Les `.md` sont découpés par sujet et déjà titrés : ce sont des chunks utilisables sans retraitement.
Indexez le `parametres.json` **séparément** et faites-le primer sur le texte — c'est lui qui porte
les sources et les dates.

**API (Claude, OpenAI, Mistral, autres)**
Le `SKILL.md` en message système, les `references/` du sujet en contexte. Faites lire le
`parametres.json` du rôle **avant** toute réponse chiffrée.

## Le contrôle tourne partout

```bash
python scripts/generer-avancement.py   # régénère le tableau de bord
python scripts/verifier-parametres.py  # sort en erreur si une valeur n'est pas sourcée et datée
```

Python standard, aucune dépendance, aucun réseau. Le second contrôle aussi que **chaque fichier de
`references/` est routé par le `SKILL.md` de son rôle** : un fichier non routé est un fichier
invisible, et c'est un défaut qui ne se voit pas à la lecture.

## ⚖️ Ce que ces rôles ne sont pas

Des outils d'**aide à la décision**. Ils ne remplacent ni un expert-comptable inscrit à l'Ordre, ni
un avocat inscrit à un barreau. Chaque fichier porte son propre rappel de cadrage et ses lignes
d'arrêt — **gardez-les dans votre portage** : ce sont eux qui empêchent un agent de donner une
consultation juridique.
