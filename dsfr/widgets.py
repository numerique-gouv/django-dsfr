from typing import Type

from django.forms.widgets import RadioSelect, ChoiceWidget

from dsfr.enums import RichRadioButtonChoices


__all__ = ["RichRadioSelect"]


class _RichChoiceWidget(ChoiceWidget):
    inline = False

    def __init__(
        self, rich_choices: Type[RichRadioButtonChoices], inline=None, attrs=None
    ):
        super().__init__(attrs)
        self.rich_choices = rich_choices
        if inline is not None:
            self.inline = inline

    @property
    def choices(self):
        return self.rich_choices.choices

    @choices.setter
    def choices(self, value):
        """
        Superseded by self.rich_choices;
        kept for compatibility with ChoiceWidget.__init__
        """
        ...

    def __deepcopy__(self, memo):
        obj = super().__deepcopy__(memo)
        obj.rich_choices = self.rich_choices
        return obj

    def create_option(
        self, name, value, label, selected, index, subindex=None, attrs=None
    ):
        opt = {
            **super().create_option(
                name, value, label, selected, index, subindex, attrs
            ),
            "inline": self.inline,
        }

        opt.update(
            {
                k: getattr(self.rich_choices(value), k)
                for k in self.rich_choices.additional_attributes
            }
        )

        return opt


class RichRadioSelect(_RichChoiceWidget, RadioSelect):
    """
    Widget permettant de produire des boutons radio riches. Ce widget fonctionne avec
    `dsfr.enums.RichRadioButtonChoices`.

    `RichRadioSelect.__init__` prend obligatoirement un argument `rich_choices` de type
    `RichRadioButtonChoices`.

    Utilisation :

    ```python
    >>> from enum import auto
    >>> from django.db.models import IntegerChoices
    >>> from django import forms
    >>> from dsfr.forms import DsfrBaseForm
    >>> from dsfr.utils import lazy_static

    >>> class ExampleRichChoices(RichRadioButtonChoices, IntegerChoices):
    ...     ITEM_1 = {
    ...         "value": auto(),
    ...         "label": "Item 1",
    ...         "html_label": "<strong>Item 1</strong>",
    ...         "pictogram": lazy_static("img/placeholder.1x1.png"),
    ...     }
    ...     ITEM_2 = {
    ...         "value": auto(),
    ...         "label": "Item 2",
    ...         "html_label": "<strong>Item 2</strong>",
    ...         "pictogram": lazy_static("img/placeholder.1x1.png"),
    ...     }
    ...     ITEM_3 = {
    ...         "value": auto(),
    ...         "label": "Item 3",
    ...         "html_label": "<strong>Item 3</strong>",
    ...         "pictogram": lazy_static("img/placeholder.1x1.png"),
    ...     }

    >>> class ExampleForm(DsfrBaseForm):
    ...     sample_rich_radio = forms.ChoiceField(
    ...         label="Cases à cocher",
    ...         required=False,
    ...         choices=ExampleRichChoices.choices,
    ...         help_text="Exemple de boutons radios riches",
    ...         widget=RichRadioSelect(rich_choices=ExampleRichChoices),
    ...     )
    ```

    ## `html_label`

    L'attribut `html_label` peut-être utilisé pour déclarer du HTML à insérer dans
    `<label>`. Le code est automatiquement marqué sûr avec
    [`django.utils.safestring.mark_safe`][1] et ne produira pas de
    [problème d'échappement du HTML][2] dans vos templates.

    Si `html_label` n'est pas déclaré par un membre de l'enum, la propriété `html_label`
    renvoie la valeur de la propriété `label` à la place.

    ## `pictogram`

    L'attribut `pictogram` peut être utilisé pour spécifier le pictogramme du bouton
    radio riche. Il peut être utilisé en combinaison avec `dsfr.utils.lazy_static`
    pour charger une ressource statique.

    ## `pictogram_alt`

    L'attribut `pictogram_alt` définit la valeur à mettre dans l'attribut `atl` de la
    balise `<img>` utilisée dans le bouton radio riche. S'il n'est pas déclaré par
    l'enum, `RichRadioSelect` ajoute un `alt=""`.

    [1]: https://docs.djangoproject.com/en/5.1/ref/utils/#django.utils.safestring.mark_safe
    [2]: https://docs.djangoproject.com/en/5.1/ref/templates/language/#automatic-html-escaping
    """

    template_name = "dsfr/widgets/rich_radio.html"
    option_template_name = "dsfr/widgets/rich_radio_option.html"
