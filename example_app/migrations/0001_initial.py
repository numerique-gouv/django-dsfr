# Generated by Django 4.2 on 2023-04-15 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=250, verbose_name="Prénom")),
                ("last_name", models.CharField(max_length=250, verbose_name="Nom")),
                ("birth_date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(max_length=15, verbose_name="Code")),
                (
                    "designation",
                    models.CharField(max_length=250, verbose_name="Désignation"),
                ),
                (
                    "help_text",
                    models.CharField(
                        blank=True,
                        max_length=250,
                        null=True,
                        verbose_name="Texte d’aide",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250, verbose_name="Titre")),
                (
                    "number_of_pages",
                    models.CharField(
                        blank=True,
                        max_length=6,
                        null=True,
                        verbose_name="Nombre de pages",
                    ),
                ),
                (
                    "book_format",
                    models.CharField(
                        blank=True,
                        choices=[("PAPER", "Papier"), ("NUM", "Numérique")],
                        max_length=10,
                        null=True,
                        verbose_name="Format",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="example_app.author",
                    ),
                ),
                ("genre", models.ManyToManyField(to="example_app.genre")),
            ],
        ),
    ]
