# Politique de sécurité

## ⚠️ D'abord : la surface d'attaque de ce dépôt n'est pas celle qu'on imagine

Il n'y a ici ni serveur, ni binaire, ni dépendance à l'exécution. Un seul script Python, qui ne
lit que des fichiers du dépôt.

**Le vrai risque est que ce dépôt est du contenu EXÉCUTABLE.** Ses fichiers sont chargés dans le
contexte d'un agent IA et orientent son comportement. Une contribution malveillante n'a besoin
d'aucun code : il lui suffit d'être **lue**.

Sont donc traitées comme des vulnérabilités, et pas comme de simples bugs :

- une instruction cachée dans une fiche ou un `SKILL.md` visant à détourner l'agent
  (« ignore les consignes précédentes », « n'affiche pas cet avertissement ») ;
- la suppression ou l'affaiblissement discret d'une **ligne d'arrêt** ou d'un avertissement légal ;
- une `source` pointant vers un domaine qui **ressemble** à un domaine officiel sans en être un ;
- un contenu qui pousserait un lecteur vers un acteur non autorisé, ou le dissuaderait d'exercer
  un droit dans un délai qui court.

★ La dernière est la plus grave et la moins visible : **une erreur bien écrite ne déclenche aucune
alerte.** Elle est recopiée, citée, et sert de base à une décision.

## Ce qui n'est pas une vulnérabilité

Un chiffre faux ou périmé de bonne foi. C'est important, mais ça se traite au grand jour :
[ouvrez une issue](https://github.com/Sjrazaviebra/le-cabinet/issues) avec le modèle
« chiffre faux ou périmé ». La transparence des erreurs est un principe du projet, pas une faille.

## Signaler en privé

Utilisez le **signalement privé de GitHub** :
[Security → Report a vulnerability](https://github.com/Sjrazaviebra/le-cabinet/security/advisories/new).

À défaut : **s.javad_rz@yahoo.com**. Merci de ne pas ouvrir d'issue publique pour les cas listés
plus haut avant qu'ils soient corrigés.

Indiquez le fichier, ce qu'un agent ferait de travers en le lisant, et si possible la révision où
c'est apparu.

## Ce à quoi vous pouvez vous attendre

- Accusé de réception sous quelques jours.
- Correction en priorité sur tout le reste.
- Mention de votre signalement dans le correctif, sauf si vous préférez l'anonymat.

⚠️ Projet maintenu par une seule personne, gratuitement. Il n'y a pas de programme de
récompense et pas d'engagement de délai contractuel.

## Versions concernées

Seule la branche `main` est maintenue. Une copie locale ancienne connaît d'anciennes dates de
vérification : mettez-la à jour (`/plugin marketplace update le-cabinet`).
