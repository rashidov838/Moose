# Generated by Django 4.2.2 on 2023-06-13 04:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0003_contact_is_solved"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
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
                ("name", models.CharField(max_length=250)),
                ("email", models.EmailField(max_length=254)),
                ("website", models.URLField(blank=True)),
                ("message", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
