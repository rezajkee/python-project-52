# Generated by Django 4.1.2 on 2022-11-11 18:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tasks", "0005_alter_task_doer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="doer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
                verbose_name="DoerTitle",
            ),
        ),
    ]
