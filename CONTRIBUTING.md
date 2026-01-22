# Contribuer à Django-DSFR

## Rester en contact avec l'équipe

Pour toute question relative à django-dsfr, n'hésitez pas à passer sur [le canal Mattermost du projet](https://mattermost.incubateur.net/betagouv/channels/django-dsfr).

## Installation en local
L’installation a été testée sur Ubuntu 24.04 avec Python 3.10 et uv installé.

- Faire un `git clone` du projet sur votre machine et ouvrir un terminal

- Installer l’environnement virtuel, les dépendances, les *pre-commit hooks* et initialiser le site d’exemple :
```{ .bash }
just init
```

## Tests

Pour faire tourner les tests :

```{ .bash }
just test
```

## Commandes
Le projet utilise [just](https://just.systems/) pour gérer le lancement de séries de commandes spécifiques, appelées recettes.

Il est possible d’avoir une liste des recettes implémentées en tapant simplement `just`.

Pour les commandes Django spécifiquement, il est possible d’en obtenir la liste avec la commande

```sh
uv run python manage.py
```

## Gestion des dépendances avec uv

Le projet utilise [uv](https://docs.astral.sh/uv/) pour gérer les dépendances de paquets Python et produire des *builds* déterministes, ainsi que pour créer les nouvelles versions du paquet et les publier sur Pypi (via Github Actions).

Pour installer les dépendances du projet :

```{ .bash }
uv sync
```

Pour installer un nouveau paquet et l’ajouter aux dépendances :

```{ .bash }
uv add <paquet>
```

Pour un paquet ne servant que pour le développement, par exemple `black` :

```{ .bash }
uv add --dev <paquet>
```

## Conventions de style et vérifications automatique

Ce projet suit globalement les [conventions de style de Django](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/).

Il utilise `ruff` et `black` pour la mise en forme et `bandit` pour repérer les failles de sécurité les plus communes.

Concernant les langues :

- le code est en anglais, y compris les commentaires, de même que le nom des branches git ;
- la documentation est en français, de même que les exemples de composants et le nom des PR ;
- Les *issues* peuvent être ouvertes dans l’une ou l’autre langue.

Pour vérifier son code, on peut intégrer le linter adapté à son IDE et aussi faire ceci :

```{ .bash }
just quality
```

Une vérification automatique est faite via des *pre-commit hooks*, qui ont normalement été installés via le `just init`.

Il est possible de les mettre à jour avec la commande :

```{ .bash }
pre-commit update
```

## Workflow avec les mainteneurs

Quelques recommandations :

- Au moment d’ouvrir une PR, merci de structurer (dans la mesure du possible) les commits pour que chacun d’entre eux concerne un seul composant ; cela permet aux mainteneurs d’effectuer une relecture commit par commit s’ils en ont envie ;
- Ne pas hésiter à solliciter la relecture de la part de l’ensemble des mainteneurs ; ça permet d’obtenir une bonne réactivité, et les mainteneurs se répartiront les PR en s’assurant que chacune d’entre elles soit relue par au moins deux d’entre eux ;
- Pendant le process de relecture, identifier les commits liés à des retours des relecteurs (pas besoin cependant de faire des commits de fixup, parce que point suivant) ;
- Pour les mainteneurs : au moment du merge, utiliser le "Squash and merge", qui permet de masquer dans l'historique final les (parfois nombreux) commits de la PR.

## Mise à jour du système de design

Quand une nouvelle version du système de design de l’État est publiée, il est possible de le mettre à jour automatiquement via la commande :

```{ .bash }
just update_dsfr
```

La commande télécharge la dernière version depuis le dépôt Github, la met dans le répertoire `dsfr/static/dsfr/dist/`, retire des fichiers pour réduire la taille du paquet Python et met à jour les sommes de contrôle d’intégrité dans le fichier `dsfr/checksums`.

Une fois la mise à jour faite, il reste à :

- lancer les tests unitaires avec `just test` ;
- ouvrir le site de test et vérifier que tous les composants s’affichent toujours bien ;
- mettre à jour la liste des composants en vérifiant depuis le site du système de design de l’État ;
- mettre à jour le fichier README.md pour indiquer la nouvelle version du DSFR ;
- mettre à jour les composants si nécessaire, en se basant sur le site du système de design de l’État (ou ouvrir des *issues*)

## Publication d’une nouvelle version

Lorsque qu’une release est publiée sur Github, une tâche Github Actions ([publish-package.yml](https://github.com/numerique-gouv/django-dsfr/blob/main/.github/workflows/publish-package.yml)) est lancée pour automatiquement générer une nouvelle version du paquet et la publier sur Pypi.

Attention ! Il faut mettre à jour le numéro de version dans le fichier `pyproject.toml` avant de faire la release, sinon la tâche échouera.

La numérotation suit le principe de [versionnage sémantique](https://semver.org/).

## Mise à jour de la documentation

De la même manière, lorsqu’une PR est mergée dans la branche `main`, une tâche Github Actions ([deploy-doc.yml](https://github.com/numerique-gouv/django-dsfr/blob/main/.github/workflows/deploy-doc.yml)) met à jour la [documentation statique](https://numerique-gouv.github.io/django-dsfr/) en faisant un export statique du site d’exemple.
