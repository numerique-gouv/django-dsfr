from django.contrib import admin

from example_app.models import Author, Genre, Book


# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """
    Admin model for Author
    """

    list_display = (
        "first_name",
        "last_name",
        "birth_date",
    )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """
    Admin model for Genre
    """

    list_display = (
        "code",
        "designation",
        "help_text",
    )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Admin model for Book
    """

    pass
