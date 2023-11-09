Le système de design propose [un certain nombre de composants](https://www.systeme-de-design.gouv.fr/elements-d-interface/composants), et Django-DSFR vise à les implémenter sous forme de balises utilisables dans les templates Django, soit en passant directement les paramètres, soit en les passant depuis la vue via un dictionnaire.

Par exemple, il est possible de créer un bouton soit en passant directement les paramètres :

```{.django}
{% dsfr_button label="Bouton principal" onclick="alert('Vous avez cliqué sur le bouton principal')" %}
```

Soit en définissant un dictionnaire dans la vue :

```{ .python }
context["data_dict"] = {
    "label": "Bouton principal",
    "onclick": "alert('Vous avez cliqué sur le bouton principal')",
}
```

et en l’appelant depuis le template :

```{.django}
{% dsfr_button data_dict %}
```

L’implémentation de ces balises est un travail en cours, mais il est tout à fait possible d’utiliser directement l’ensemble du système de design de l’État en utilisant directement le code HTML tel que défini dans la documentation officielle :

```{.html}
<button class="fr-btn" onclick="alert('Vous avez cliqué sur le bouton principal')" type="submit">
  Bouton principal
</button>
```

Toutes ces options produisent le même résultat :

<button class="fr-btn" onclick="alert('Vous avez cliqué sur le bouton principal')" type="submit">
  Bouton principal
</button>
