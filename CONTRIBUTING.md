# Contribuer à Django-DSFR

## Installation en local
L’installation a été testée sur Ubuntu 22.04 avec Python 3.10 et poetry installé.

- Faire un `git clone` du projet sur votre machine et ouvrir un terminal

- Installer l’environnement virtuel, les dépendances et initialiser le site d’exemple
```
make init
```

## Tests

Pour faire tourner les tests :

```
make test
```

## Gestion des dépendances avec Poetry

Le projet utilise [Poetry](https://python-poetry.org/) pour gérer les dépendances de paquets Python et produire des *builds* déterministes, ainsi que pour créer les nouvelles versions du paquet et les publier sur Pypi.

Pour installer les dépendances du projet :

```
poetry install
```

Pour installer un nouveau paquet et l’ajouter aux dépendances :

```
poetry add <paquet>
```

Pour un paquet ne servant que pour le développement, par exemple `black` :

```
poetry add --group dev <paquet>
```

Pour activer l’environnement virtuel :
```
poetry shell
```

## Conventions de style et vérifications automatique

Ce projet suit globalement les [conventions de style de Django](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/).

Il utilise `ruff` et `black` pour la mise en forme et `bandit` pour repérer les failles de sécurité les plus communes.

Concernant les langues :
- le code est en anglais, y compris les commentaires, de même que le nom des branches git ;
- la documentation est en français, de même que les exemples de composants et le nom des PR ;
- Les *issues* peuvent être ouvertes dans l’une ou l’autre langue.

Pour vérifier son code, on peut intégrer le linter adapté à son IDE et aussi faire ceci :

```
make checkstyle
```

## Mise à jour du système de design

Quand une nouvelle version du système de design de l'État est publiée, il est possible de le mettre à jour automatiquement via la commande 
```
make update_dsfr
```

La commande va récupérer la dernière version sur le dépôt Github, la met dans le répertoire `dsfr/static/dsfr/dist/`, retire des fichiers pour réduire la taille du paquet python et met à jour les sommes de contrôle d'intégrités dans le fichier `dsfr/checksums`.

Une fois la mise à jour faite, il reste à :
- lancer les tests unitaires avec `make test` ;
- ouvrir le site de test et vérifier que tous les composants s’affichent toujours bien ;
- mettre à jour la liste des composants en vérifiant depuis le site du système de design de l’État ;
- mettre à jour les composants si nécessaire, en se basant sur le site du système de design de l’État (ou ouvrir des *issues*)

## Publication d’une nouvelle version

Lorsque qu’une release est publiée sur Github, une tâche Github Actions ([publish-package.yml]([./.github/workflows/publish-package.yml)) est lancée pour automatiquement générer une nouvelle version du paquet et la publier sur Pypi.

Attention ! Il faut mettre à jour le numéro de version dans le fichier `pyproject.toml` avant de faire la release, sinon la tâche échouera.

La numérotation suit le principe de [versionnage sémantique](https://semver.org/).

## Mise à jour de la documentation

De la même manière, lorsqu’une PR est mergée dans la branche `main`, une tâche Github Actions ([deploy-doc.yml]([./.github/workflows/deploy-doc.yml)) met à jour la documentation statique en faisant un export statique du site d’exemple.
