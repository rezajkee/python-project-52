# Generated by Django 4.1.2 on 2022-11-14 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("labels", "0001_initial"),
        ("tasks", "0014_alter_task_executor"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="labels",
            field=models.ManyToManyField(
                to="labels.label", verbose_name="Labels"
            ),
        ),
    ]
