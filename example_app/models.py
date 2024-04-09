from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


# These are example models to show how form and formset can work
class Author(models.Model):
    first_name = models.CharField(
        _("First name"), max_length=250, null=False, blank=False
    )
    last_name = models.CharField(
        _("Last name"), max_length=250, null=False, blank=False
    )
    birth_date = models.DateField(_("Birth date"), null=True, blank=True)

    class Meta:
        verbose_name = _("Author")


class Genre(models.Model):
    code = models.CharField(_("Code"), max_length=15, null=False, blank=False)
    designation = models.CharField(
        _("Designation"), max_length=250, null=False, blank=False
    )
    help_text = models.CharField(_("Help text"), max_length=250, blank=True)

    def __str__(self):
        return str(self.designation)

    class Meta:
        verbose_name = _("Genre")


BOOK_FORMAT = (
    ("PAPER", _("Paper")),
    ("NUM", _("Digital")),
)


class Book(models.Model):
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=False, blank=False
    )
    title = models.CharField(_("Title"), max_length=250, null=False, blank=False)
    number_of_pages = models.CharField(_("Number of pages"), max_length=6, blank=True)
    book_format = models.CharField(
        _("Format"), choices=BOOK_FORMAT, max_length=10, blank=True
    )
    genre = models.ManyToManyField(Genre)

    class Meta:
        verbose_name = _("Book")
