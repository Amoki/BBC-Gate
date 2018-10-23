# Generated by Django 2.1.2 on 2018-10-08 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Code",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(help_text="The digicode", max_length=32)),
                (
                    "expires_at",
                    models.DateTimeField(
                        blank=True, help_text="The expiration date if needed", null=True
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="A short description of why this code has been created",
                        null=True,
                    ),
                ),
            ],
        )
    ]