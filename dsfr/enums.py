from django import VERSION
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.version import PY311

if PY311:
    from enum import property as enum_property
else:
    from types import DynamicClassAttribute as enum_property

if VERSION >= (5, 0):
    from django.db.models.enums import ChoicesType
else:
    from django.db.models.enums import ChoicesMeta as ChoicesType

__all__ = ["ExtendedChoices", "RichRadioButtonChoices"]


def _is_dunder(name):
    """Returns True if a __dunder__ name, False otherwise."""
    return (
        len(name) > 4
        and name[:2] == name[-2:] == "__"
        and name[2] != "_"
        and name[-3] != "_"
    )


def _is_sunder(name):
    """Returns True if a _sunder_ name, False otherwise."""
    return (
        len(name) > 2
        and name[0] == name[-1] == "_"
        and name[1:2] != "_"
        and name[-2:-1] != "_"
    )


class _ExtendedChoicesType(ChoicesType):
    @classmethod
    def __prepare__(metacls, cls, bases, **kwds):
        classdict = super().__prepare__(cls, bases, **kwds)

        class _EnumDict(classdict.__class__):
            def __init__(self, old_classdict):
                super().__init__()
                self._additional_attributes = {}
                # Copy absent old_classdict members into self
                for member_name, member_value in old_classdict.__dict__.items():
                    self.__dict__.setdefault(member_name, member_value)

                # Copy dict content
                self.update(old_classdict)

            def __setitem__(self, member, value):
                """Allows to handle declaring enum members as dicts"""
                if not PY311 and isinstance(value, (list, tuple)):
                    # Prior to Python 3.11, EnumDict does not interpret auto() when
                    # wrapped in a tuple so we need to set the value alone a first time
                    # before wrapping it in a tuple.
                    if len(value) == 1:
                        return super().__setitem__(member, value[0])

                    if len(value) == 2:
                        value, label = value
                    else:
                        *value, label = value

                    super().__setitem__(member, value)
                    dict.__setitem__(self, member, (self[member], label))
                    return

                if not isinstance(value, dict):
                    return super().__setitem__(member, value)

                if "value" not in value:
                    raise ValueError(
                        "enum value for {member} should contain member 'value' "
                        "when using a dict as value; got {member} = {value}".format(
                            member=member, value=repr(value)
                        )
                    )

                if PY311:
                    if "label" in value:
                        super().__setitem__(
                            member, (value.pop("value"), value.pop("label"))
                        )
                    else:
                        super().__setitem__(member, value.pop("value"))
                else:
                    # Prior to Python 3.11, EnumDict does not interpret auto() when
                    # wrapped in a tuple so we need to set the value alone a first time
                    # before wrapping it in a tuple.
                    super().__setitem__(member, value.pop("value"))
                    if "label" in value:
                        dict.__setitem__(
                            self, member, (self[member], value.pop("label"))
                        )

                for attr_name, attr_value in value.items():
                    if _is_sunder(attr_name) or _is_dunder(attr_name):
                        raise ValueError(
                            (
                                "enum value for {member} contains key {key}. "
                                "Names surrounded with single or double underscores are "
                                "not authorized as dict values"
                            ).format(member=member, key=attr_name)
                        )
                    self._additional_attributes.setdefault(attr_name, {})
                    self._additional_attributes[attr_name][member] = attr_value

        return _EnumDict(classdict)

    def __new__(metacls, classname, bases, classdict, **kwds):
        cls = super().__new__(metacls, classname, bases, classdict, **kwds)
        cls._additional_attributes = list(classdict._additional_attributes.keys())

        def instance_property_getter(name):
            @enum_property
            def _instance_property_getter(enum_item):
                private_name = enum_item.private_variable_name(name)
                if hasattr(enum_item, private_name):
                    return getattr(enum_item, private_name)
                elif hasattr(enum_item, "dynamic_attribute_value"):
                    return enum_item.dynamic_attribute_value(name)
                else:
                    raise AttributeError(
                        (
                            "{}.{} does not contain key '{}'. Please add key or "
                            "implement a 'dynamic_attribute_value(self, name)' method "
                            "in you enum to provide a value"
                        ).format(cls.__name__, instance.name, name)
                    )

            return _instance_property_getter

        for instance in cls:
            for attr_name, attr_value in classdict._additional_attributes.items():
                if hasattr(instance, cls.private_variable_name(attr_name)):
                    raise ValueError(
                        (
                            "Can't set '{}' on {}.{}; instance already has a private "
                            "'{}' attribute; please choose a different name or remove "
                            "from the member value"
                        ).format(
                            attr_name,
                            cls.__name__,
                            instance.name,
                            cls.private_variable_name(attr_name),
                        )
                    )

                if instance.name in attr_value:
                    setattr(
                        instance,
                        cls.private_variable_name(attr_name),
                        attr_value[instance.name],
                    )

                if not hasattr(instance, attr_name):
                    setattr(cls, attr_name, instance_property_getter(attr_name))

        return cls

    @property
    def additional_attributes(cls):
        """Enum additionnal attributes that were set from dict"""
        return cls._additional_attributes


class ExtendedChoices(models.Choices, metaclass=_ExtendedChoicesType):
    """
    Extension de [Django's `models.Choices`][1] pour supporter l'ajout d'attributs
    arbitraires aux enums en utilisant un dictionnaire.

    Exemple d'utilisation :

    ```python
    >>> class TemperatureChoices(ExtendedChoices):
    ...   COLD = {
    ...     "value": "COLD",
    ...     "label": "Cold",
    ...     "temperature": "<12°c"
    ...   }
    ...   OK = {
    ...     "value": "OK",
    ...     "label": "ok",
    ...     "temperature": ">=12°c,<25°c"
    ...   }
    ...   HOT = {
    ...     "value": "HOT",
    ...     "label": "Hot!",
    ...     "temperature": ">=25°c"
    ...   }
    >>> TemperatureChoices.OK.temperature
    ">=12°c,<25°c"
    ```

    Dans l'exemple précédent, en plus de `TemperatureChoices.<enum instance>.value`,
    `TemperatureChoices.<enum instance>.label` et
    `TemperatureChoices.<enum instance>.name`, `ExtendedChoices` ajoute une propriété
    `temperature` pour chaque instance de instance d'enum.

    Exemple : `TemperatureChoices.<enum instance>.temperature`.

    Notez que `"value"` est la seule clé obligatoire dans le dictionnaire. Lorsqu'un
    dictionnaire ne contient que `« value »`, les exemples suivants sont équivalents :

    ```python
    >>> from django.db import models
    >>> class TemperatureChoices(models.Choices):
    ...     COLD = "COLD"

    >>> class TemperatureChoices(ExtendedChoices):
    ...     COLD = {"value": "COLD"}
    ```

    Voir [cette section sur la façon de fournir des valeurs par défaut pour des attributs supplémentaires](#default-values)

    ## Utilisation avec `enum.auto()`

    `ExtendedChoices` supporte l'utilisation de [`enum.auto()`][2] :

    ```python
    >>> from enum import auto
    >>> from django.db import models
    >>> class TemperatureChoices(ExtendedChoices, models.TextChoices):
    ...   COLD = {
    ...     "value": auto(),
    ...     "label": "Cold",
    ...     "temperature": "<12°c"
    ...   }
    ...   OK = {
    ...     "value": auto(),
    ...     "label": "ok",
    ...     "temperature": ">=12°c,<25°c"
    ...   }
    ...   HOT = {
    ...     "value": auto(),
    ...     "label": "Hot!",
    ...     "temperature": ">=25°c"
    ...   }
    ```

    `ExtendedChoices` peut être utilisé en combinaison `django.db.models.TextChoices`
    ou `django.db.models.IntegerChoices` pour calculer automatiquement l'attribut
    `value` avec `enum.auto()` ou peut définir une méthode `_generate_next_value_` pour
    fournir la valeur (voir [[2]][2]) :

    ```python
    >>> from enum import auto
    >>> class TemperatureChoices(ExtendedChoices):
    ...   COLD = {
    ...     "value": auto(),
    ...     "label": "Cold",
    ...     "temperature": "<12°c"
    ...   }
    ...   OK = {
    ...     "value": auto(),
    ...     "label": "ok",
    ...     "temperature": ">=12°c,<25°c"
    ...   }
    ...   HOT = {
    ...     "value": auto(),
    ...     "label": "Hot!",
    ...     "temperature": ">=25°c"
    ...   }
    ...
    ...   def _generate_next_value_(name, start, count, last_values):
    ...       return f"{name}: {count}"
    ```

    ## Fournir des valeurs par défaut aux attributs supplémentaires {: #default-values}

    Il peut arriver que vous souhaitiez fournir dynamiquement des valeurs pour un
    attribut supplémentaire. Si vous ne spécifiez pas de valeur pour un attribut
    supplémentaire lors de la déclaration de l'enum, vous pouvez la fournir
    dynamiquement avec la méthode `dynamic_attribute_value` :

    ```python
    >>> from enum import auto
    >>> from django.conf import settings
    >>> from django.db import models
    >>> class TemperatureChoices(ExtendedChoices, models.IntegerChoices):
    ... COLD = {
    ...     "value": auto(),
    ...     "temperature": {"lorem": "ipsum 1"},
    ... }
    ... OK = auto()
    ...
    ... def dynamic_attribute_value(self, name):
    ...   if name == "temperature":
    ...     return settings.TEMPERATURES[self.value]
    ...   else:
    ...     return -1
    ```

    Dans l'exemple précédent, la valeur de `temperature` n'est pas spécifiée pour
    `TemperatureChoices.OK`. Accéder à la propriété `TemperatureChoices.OK.temperature`
    appellera `TemperatureChoices.OK.dynamic_attribute_value("temperature")` pour .

    ## Utilisation avancée

    Par défaut, lorsque vous spécifiez des attibuts supplémentaires, `ExtendedChoices`
    stocke cette valeur dans un membre de l'instance. Le nom de se membre correspond
    au nom de l'attribut spécifié précédé de `__`. Exemple :

    ```python
    >>> from enum import auto
    >>> class TemperatureChoices(ExtendedChoices):
    ...   COLD = {
    ...     "value": auto(),
    ...     "label": "Cold",
    ...     "temperature": "<12°c"
    ...   }
    ...   OK = {
    ...     "value": auto(),
    ...     "label": "ok",
    ...     "temperature": ">=12°c,<25°c"
    ...   }
    ...   HOT = {
    ...     "value": auto(),
    ...     "label": "Hot!",
    ...     "temperature": ">=25°c"
    ...   }

    >>> TemperatureChoices.OK.__temperature == TemperatureChoices.OK.temperature
    ```

    Si, pour quelque raison que ce soit, vous souhaitez utiliser un autre nom pour
    l'instance qui stocke la valeur, vous pouvez déclarer une méthode statique
    `private_variable_name` :

    ```python
    >>> from enum import auto
    >>> class TemperatureChoices(ExtendedChoices):
    ...   COLD = {
    ...     "value": auto(),
    ...     "label": "Cold",
    ...     "temperature": "<12°c"
    ...   }
    ...   OK = {
    ...     "value": auto(),
    ...     "label": "ok",
    ...     "temperature": ">=12°c,<25°c"
    ...   }
    ...   HOT = {
    ...     "value": auto(),
    ...     "label": "Hot!",
    ...     "temperature": ">=25°c"
    ...   }
    ...
    ...   @staticmethod
    ...   def private_variable_name(name):
    ...     return f"m_{name}"

    >>> TemperatureChoices.OK.m_temperature == TemperatureChoices.OK.temperature
    ```

    [1]: https://docs.djangoproject.com/en/5.1/ref/models/fields/#enumeration-types
    [2]: https://docs.python.org/3/library/enum.html#enum.auto
    """

    @staticmethod
    def private_variable_name(name):
        return f"__{name}"


class RichRadioButtonChoices(ExtendedChoices):
    """
    Version spécialisée de `ExtendedChoices` à utiliser avec
    `dsfr.widgets.RichRadioSelect`. Cette version déclare en plus les propriétés
    `pictogram`, `pictogram_alt` et `html_label` :

    ```python
    >>> from enum import auto
    >>> from django.db.models import IntegerChoices
    >>> from dsfr.utils import lazy_static
    >>> class ExampleRichChoices(IntegerChoices, RichRadioButtonChoices):
    ...   ITEM_1 = {
    ...       "value": auto(),
    ...       "label": "Item 1",
    ...       "html_label": "<strong>Item 1</strong>",
    ...       "pictogram": lazy_static("img/placeholder.1x1.png"),
    ...   }
    ...   ITEM_2 = {
    ...       "value": auto(),
    ...       "label": "Item 2",
    ...       "html_label": "<strong>Item 2</strong>",
    ...       "pictogram": lazy_static("img/placeholder.1x1.png"),
    ...   }
    ...   ITEM_3 = {
    ...       "value": auto(),
    ...       "label": "Item 3",
    ...       "html_label": "<strong>Item 3</strong>",
    ...       "pictogram": lazy_static("img/placeholder.1x1.png"),
    ...   }
    ```

    Voir `dsfr.widgets.RichRadioSelect` pour plus de détails.
    """

    @enum_property
    def pictogram(self):
        return getattr(self, self.private_variable_name("pictogram"), "")

    @enum_property
    def pictogram_alt(self):
        return getattr(self, self.private_variable_name("pictogram_alt"), None)

    @enum_property
    def html_label(self):
        return (
            mark_safe(getattr(self, self.private_variable_name("html_label")))  # nosec
            if hasattr(self, self.private_variable_name("html_label"))
            else self.label
        )
