# Generated by Django 4.1.5 on 2023-02-05 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("katalog", "0002_alter_towar_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="towar",
            name="description",
            field=models.TextField(blank=True, max_length=250),
        ),
    ]
