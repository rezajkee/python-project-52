# Generated by Django 4.1.2 on 2022-11-11 08:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("statuses", "0002_alter_status_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
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
                    "name",
                    models.CharField(max_length=100, verbose_name="NameTitle"),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, verbose_name="DescriptionTitle"
                    ),
                ),
                (
                    "creation_date",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="CreationDateTitle",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="AuthorTitle",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "doer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="DoerTitle",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="StatusTitle",
                        to="statuses.status",
                    ),
                ),
            ],
        ),
    ]