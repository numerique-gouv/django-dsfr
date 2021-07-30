**Django-dsfr** est une application django permettant d'utiliser le Design system de l’État dans des projets Django.

Elle a été développée dans le cadre du défi [Open Collectivités](https://github.com/entrepreneur-interet-general/opencollectivites) et est un travail en cours (les composants sont actuellement développés au fur et à mesure de leur utilisation dans le cadre d’Open Collectivités), cf. la section « Avancement » ci-dessous.

## Table des matières
* [Avancement](#avancement)
* [Installation](#installation)
* [Utilisation](#utilisation)
* [Notes](#notes)


<a name="avancement"></a>
## Avancement 
La liste des composants est basée sur la version 1.1.0 du DSFR.

### Composants intégrés sous forme de balises (tags)

[ ] Accordéon - Accordion
[ ] Alertes - Alerts
[ ] Barre de recherche - Search
[ ] Boutons - Buttons
[ ] Groupe de boutons
[ ] Boutons radio - radio button
[ ] Boutons radio riches - radio button extended
[ ] Case à cocher - checkbox
[x] Carte - Card
[x] Champ de saisie - Input
[ ] Citation - Quote
[ ] Contenus médias - Responsive medias
[x] Fil d’Ariane - Breadcrumb
[ ] Gestionnaire de consentement - Consent banner
[x] Icônes de favoris - Favicons
[ ] Interrupteur - Toggle Switch
[ ] Lettre d'information et réseaux sociaux - Newsletter & Follow us
[ ] Liens - Links
[ ] Liens d’évitement - Skiplinks
[x] Liste déroulante - Select
[ ] Menu latéral - Side menu
[x] Mise en avant - Call-out
[ ] Mise en exergue - Highlight
[ ] Modale - Modal
[ ] Navigation principale - Main navigation
[ ] Onglets - Tabs
[x] Pagination - Pagination
[x] Paramètres d'affichage - Switch theme (Theme modale)
[ ] Partage - Share
[x] Sommaire - Summary
[x] Tableau - Table
[ ] Tag
[x] Tuile - Tile

### Composants intégrés sous forme de templates à inclure

[x] En-tête - Header
[x] Pied de page - Footer

### Autres balises
[x] global css: Appelle la feuille de style générale. À inclure dans le <header> des pages web.
[x] global js : Appelle le javascript général. À inclure en bas du <body> des pages web

<a name="installation"></a>
## Installation
Voir la section dédiée dans le [README](https://github.com/entrepreneur-interet-general/django-dsfr/blob/main/README.rst)

<a name="utilisation"></a>
## Utilisation
Le fichier https://github.com/entrepreneur-interet-general/django-dsfr/blob/main/dsfr/templatetags/dsfr_tags.py décrit chaque balise avec un exemple d'utilisation.

<a name="notes"></a>
## Notes
- Il est possible d'utiliser tous les composants du DSFR directement avec leur code HTML, y compris ceux pour lesquels in’existe pas encore de balise
- Pour certains composants très simples (comme les liens ou les boutons), il n’est pas forcément pertinent de créer une balise, qui n'apporterait que peu par rapport à l'utilisation directe du code HTML.
- De même pour certains où il vaut mieux créer un template ad-hoc à chaque utilisation, comme les modales.