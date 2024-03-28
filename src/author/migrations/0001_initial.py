# Generated by Django 4.1.13 on 2024-03-28 16:58

from django.db import migrations, models


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
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Время создания записи"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Время обновления записи"
                    ),
                ),
                ("resume_url", models.URLField(verbose_name="Ссылка на резюме")),
                ("github_url", models.URLField(verbose_name="Ссылка GitHub")),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
            ],
            options={
                "verbose_name": "Информация об авторе",
                "verbose_name_plural": "Информация об авторе",
            },
        ),
    ]