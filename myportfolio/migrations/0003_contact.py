# Generated by Django 5.1.3 on 2024-11-30 08:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myportfolio", "0002_rename_create_at_projects_created_at"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("message", models.TextField()),
                ("create_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
