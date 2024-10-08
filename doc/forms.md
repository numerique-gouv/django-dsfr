# Formulaires – Documentation

## Initialisation des formulaires
Les formulaires sont construits en se basant sur la classe `DsfrBaseForm`, par exemple :

```{ .python }
# votre_app/forms.py

from dsfr.forms import DsfrBaseForm


class ExampleForm(DsfrBaseForm):
    # basic fields
    user_name = forms.CharField(label="Nom d’utilisateur", max_length=100)

    user_email = forms.EmailField(
        label="Adresse électronique",
        help_text="Format attendu : prenom.nom@domaine.fr",
        required=False,
    )
```

Il est possible de multi-classer :

```{ .python }
class AuthorCreateForm(ModelForm, DsfrBaseForm):
```

## Classes CSS
Le formulaire ajoute la ou les classes appropriées (`fr-input`, `fr-select`, etc.) en fonction du type de champ, mais uniquement si une classe n’a pas déjà été ajoutée.

Si c’est le cas, il faut soit forcer manuellement les classes à utiliser :

```{ .python }
    password = forms.CharField(
        label="Mot de passe", widget=forms.PasswordInput(
            "autocomplete": "current-password",
            "required": True,
            "class": "fr-input my-custom-class"
        )
    )
```

soit les ajouter dans la méthode `init` du formulaire (en faisant attention à laisser une espace au début) :

```{ .python }
class AuthorCreateForm(ModelForm, DsfrBaseForm):

# [...]

def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields["password"].widget.attrs["class"] += " my custom class"
```

## Utilisation

La balise `{% dsfr_form %}` est maintenant dépréciée et sera retirée à la fin de l’année 2024.

Il faut donc remplacer les instances de `{% dsfr_form %}` par ``{{ form }}`` et `{% dsfr_form my_custom_form %}` par `{{ my_custom_form }}`.
