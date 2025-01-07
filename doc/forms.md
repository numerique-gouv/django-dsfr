# Formulaires – Documentation
- <a class="fr-link fr-icon-external-link-line fr-link--icon-right fr-link--lg" href="https://www.systeme-de-design.gouv.fr/composants-et-modeles/blocs-fonctionnels/formulaires" target="_blank" rel="noopener noreferrer">
        Voir la page de documentation du composant sur le Système de Design de l’État
        <span class="fr-sr-only">Ouvre une nouvelle fenêtre</span>
  </a>
- <a class="fr-link fr-icon-external-link-line fr-link--icon-right fr-link--lg" href="https://main--ds-gouv.netlify.app/example/component/form/" target="_blank" rel="noopener noreferrer">
        Voir la page d’exemple du Système de Design de l’État
        <span class="fr-sr-only">Ouvre une nouvelle fenêtre</span>
  </a>
- <a class="fr-link fr-icon-external-link-line fr-link--icon-right fr-link--lg" href="https://storybook.systeme-de-design.gouv.fr/?path=/docs/form--docs" target="_blank" rel="noopener noreferrer">
        Voir la page du composant sur Storybook
        <span class="fr-sr-only">Ouvre une nouvelle fenêtre</span>
  </a>

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
Les formulaires sont appelés avec la balise `{{ form }}` (ou `{{ my_custom_form }}` le cas échéant).

La balise `{% dsfr_form %}` est maintenant dépréciée depuis Django-DSFR 2.0.0.

## Composants

### `dsfr.enums.ExtendedChoices` {: #extended-choices }

Extension de [Django's `models.Choices`][1] pour supporter l'ajout d'attributs
arbitraires aux enums en utilisant un dictionnaire.

Exemple d'utilisation :

```python
from dsfr.enums import ExtendedChoices

class TemperatureChoices(ExtendedChoices):
  COLD = {
    "value": "COLD",
    "label": "Cold",
    "temperature": "<12°c"
  }
  OK = {
    "value": "OK",
    "label": "ok",
    "temperature": ">=12°c,<25°c"
  }
  HOT = {
    "value": "HOT",
    "label": "Hot!",
    "temperature": ">=25°c"
  }

TemperatureChoices.OK.temperature == ">=12°c,<25°c"
```

Dans l'exemple précédent, en plus de `TemperatureChoices.<enum instance>.value`,
`TemperatureChoices.<enum instance>.label` et
`TemperatureChoices.<enum instance>.name`, `ExtendedChoices` ajoute une propriété
`temperature` pour chaque instance de instance d'enum.

Exemple : `TemperatureChoices.<enum instance>.temperature`.

Notez que `"value"` est la seule clé obligatoire dans le dictionnaire. Lorsqu'un
dictionnaire ne contient que `« value »`, les exemples suivants sont équivalents :

```python
from django.db import models
from dsfr.enums import ExtendedChoices

class TemperatureChoices(models.Choices):
    COLD = "COLD"

class TemperatureChoices(ExtendedChoices):
    COLD = {"value": "COLD"}
```

Voir [cette section sur la façon de fournir des valeurs par défaut pour des attributs supplémentaires](#default-values)

#### Utilisation avec `enum.auto()`

`ExtendedChoices` supporte l'utilisation de [`enum.auto()`][2] :

```python
from enum import auto
from django.db import models
from dsfr.enums import ExtendedChoices

class TemperatureChoices(ExtendedChoices, models.TextChoices):
  COLD = {
    "value": auto(),
    "label": "Cold",
    "temperature": "<12°c"
  }
  OK = {
    "value": auto(),
    "label": "ok",
    "temperature": ">=12°c,<25°c"
  }
  HOT = {
    "value": auto(),
    "label": "Hot!",
    "temperature": ">=25°c"
  }
```

`ExtendedChoices` peut être utilisé en combinaison `django.db.models.TextChoices`
ou `django.db.models.IntegerChoices` pour calculer automatiquement l'attribut
`value` avec `enum.auto()` ou peut définir une méthode `_generate_next_value_` pour
fournir la valeur (voir [[2]][2]) :

```python
from enum import auto
from dsfr.enums import ExtendedChoices

class TemperatureChoices(ExtendedChoices):
  COLD = {
    "value": auto(),
    "label": "Cold",
    "temperature": "<12°c"
  }
  OK = {
    "value": auto(),
    "label": "ok",
    "temperature": ">=12°c,<25°c"
  }
  HOT = {
    "value": auto(),
    "label": "Hot!",
    "temperature": ">=25°c"
  }

  def _generate_next_value_(name, start, count, last_values):
      return f"{name}: {count}"
```

#### Fournir des valeurs par défaut aux attributs supplémentaires {: #default-values}

Il peut arriver que vous souhaitiez fournir dynamiquement des valeurs pour un
attribut supplémentaire. Si vous ne spécifiez pas de valeur pour un attribut
supplémentaire lors de la déclaration de l'enum, vous pouvez la fournir
dynamiquement avec la méthode `dynamic_attribute_value` :

```python
from enum import auto
from django.conf import settings
from django.db import models
from dsfr.enums import ExtendedChoices
class TemperatureChoices(ExtendedChoices, models.IntegerChoices):
    COLD = {
        "value": auto(),
        "temperature": {"lorem": "ipsum 1"},
    }
    OK = auto()

    def dynamic_attribute_value(self, name):
      if name == "temperature":
        return settings.TEMPERATURES[self.value]
      else:
        return -1
```

Dans l'exemple précédent, la valeur de `temperature` n'est pas spécifiée pour
`TemperatureChoices.OK`. Accéder à la propriété `TemperatureChoices.OK.temperature`
appellera `TemperatureChoices.OK.dynamic_attribute_value("temperature")` pour .

#### Utilisation avancée

Par défaut, lorsque vous spécifiez des attibuts supplémentaires, `ExtendedChoices`
stocke cette valeur dans un membre de l'instance. Le nom de se membre correspond
au nom de l'attribut spécifié précédé de `__`. Exemple :

```python
from enum import auto
from dsfr.enums import ExtendedChoices

class TemperatureChoices(ExtendedChoices):
  COLD = {
    "value": auto(),
    "label": "Cold",
    "temperature": "<12°c"
  }
  OK = {
    "value": auto(),
    "label": "ok",
    "temperature": ">=12°c,<25°c"
  }
  HOT = {
    "value": auto(),
    "label": "Hot!",
    "temperature": ">=25°c"
  }

TemperatureChoices.OK.__temperature == TemperatureChoices.OK.temperature
```

Si, pour quelque raison que ce soit, vous souhaitez utiliser un autre nom pour
l'instance qui stocke la valeur, vous pouvez déclarer une méthode statique
`private_variable_name` :

```python
from enum import auto
from dsfr.enums import ExtendedChoices

class TemperatureChoices(ExtendedChoices):
  COLD = {
    "value": auto(),
    "label": "Cold",
    "temperature": "<12°c"
  }
  OK = {
    "value": auto(),
    "label": "ok",
    "temperature": ">=12°c,<25°c"
  }
  HOT = {
    "value": auto(),
    "label": "Hot!",
    "temperature": ">=25°c"
  }

  @staticmethod
  def private_variable_name(name):
    return f"m_{name}"

TemperatureChoices.OK.m_temperature == TemperatureChoices.OK.temperature
```

[1]: https://docs.djangoproject.com/en/5.1/ref/models/fields/#enumeration-types
[2]: https://docs.python.org/3/library/enum.html#enum.auto

### `dsfr.enums.RichRadioButtonChoices` {: #rich-choices }

Version spécialisée de [`RichRadioButtonChoices`](#extended-choices) à utiliser avec
`dsfr.widgets.RichRadioSelect`. Cette version déclare en plus les propriétés
`pictogram`, `pictogram_alt` et `html_label` :

```python
from enum import auto
from django.db.models import IntegerChoices
from dsfr.utils import lazy_static
from dsfr.enums import RichRadioButtonChoices

class ExampleRichChoices(IntegerChoices, RichRadioButtonChoices):
  ITEM_1 = {
      "value": auto(),
      "label": "Item 1",
      "html_label": "<strong>Item 1</strong>",
      "pictogram": lazy_static("img/placeholder.1x1.png"),
  }
  ITEM_2 = {
      "value": auto(),
      "label": "Item 2",
      "html_label": "<strong>Item 2</strong>",
      "pictogram": lazy_static("img/placeholder.1x1.png"),
  }
  ITEM_3 = {
      "value": auto(),
      "label": "Item 3",
      "html_label": "<strong>Item 3</strong>",
      "pictogram": lazy_static("img/placeholder.1x1.png"),
  }
```

Voir [`dsfr.widgets.RichRadioSelect`](#rich-radio-select) pour plus de détails.

### `dsfr.widgets.RichRadioSelect` {: #rich-radio-select }

Widget permettant de produire des boutons radio riches. Ce widget fonctionne avec
[`dsfr.enums.ExtendedChoices`](#rich-choices).

`RichRadioSelect.__init__` prend obligatoirement un argument `rich_choices` de type
`RichRadioButtonChoices`.

Utilisation :

```python
from enum import auto
from django.db.models import IntegerChoices
from django import forms
from dsfr.forms import DsfrBaseForm
from dsfr.utils import lazy_static
from dsfr.enums import RichRadioButtonChoices
from dsfr.widgets import RichRadioSelect

class ExampleRichChoices(RichRadioButtonChoices, IntegerChoices):
    ITEM_1 = {
        "value": auto(),
        "label": "Item 1",
        "html_label": "<strong>Item 1</strong>",
        "pictogram": lazy_static("img/placeholder.1x1.png"),
    }
    ITEM_2 = {
        "value": auto(),
        "label": "Item 2",
        "html_label": "<strong>Item 2</strong>",
        "pictogram": lazy_static("img/placeholder.1x1.png"),
    }
    ITEM_3 = {
        "value": auto(),
        "label": "Item 3",
        "html_label": "<strong>Item 3</strong>",
        "pictogram": lazy_static("img/placeholder.1x1.png"),
    }

class ExampleForm(DsfrBaseForm):
    sample_rich_radio = forms.ChoiceField(
        label="Cases à cocher",
        required=False,
        choices=ExampleRichChoices.choices,
        help_text="Exemple de boutons radios riches",
        widget=RichRadioSelect(rich_choices=ExampleRichChoices),
    )
```

#### `html_label`

L'attribut `html_label` peut-être utilisé pour déclarer du HTML à insérer dans
`<label>`. Le code est automatiquement marqué sûr avec
[`django.utils.safestring.mark_safe`][1] et ne produira pas de
[problème d'échappement du HTML][2] dans vos templates.

Si `html_label` n'est pas déclaré par un membre de l'enum, la propriété `html_label`
renvoie la valeur de la propriété `label` à la place.

#### `pictogram`

L'attribut `pictogram` peut être utilisé pour spécifier le pictogramme du bouton
radio riche. Il peut être utilisé en combinaison avec [`dsfr.utils.lazy_static`](#lazy-static)
pour charger une ressource statique.

#### `pictogram_alt`

L'attribut `pictogram_alt` définit la valeur à mettre dans l'attribut `alt` de la
balise `<img>` utilisée dans le bouton radio riche. S'il n'est pas déclaré par
l'enum, `RichRadioSelect` ajoute un `alt=""`.

[1]: https://docs.djangoproject.com/en/5.1/ref/utils/#django.utils.safestring.mark_safe
[2]: https://docs.djangoproject.com/en/5.1/ref/templates/language/#automatic-html-escaping

### `dsfr.utils.lazy_static` {: #lazy-static }

Équivalent du tag Django `{% static %}` à utiliser dans le code. Exemple :

```python
from dsfr.utils import lazy_static

lazy_static("img/logo.png")
```
