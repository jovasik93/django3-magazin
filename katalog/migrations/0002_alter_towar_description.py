# Generated by Django 4.1.5 on 2023-02-05 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("katalog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="towar",
            name="description",
            field=models.CharField(blank=True, max_length=250),
        ),
    ]