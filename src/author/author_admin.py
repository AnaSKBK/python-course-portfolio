"""
Функции панели управления для приложения "Автор".
"""

from django.contrib import author_admin
from author.models import Author


@author_admin.register(Author)
class AuthorAdmin(author_admin.ModelAdmin):
    list_display = (
        "resume_url",
        "github_url",
        "email",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "github_url",
        "resume_url",
        "email",
    )

    list_filter = (
        "created_at",
        "updated_at",
    )