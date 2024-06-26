# Generated by Django 5.0.6 on 2024-06-08 15:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0007_version"),
    ]

    operations = [
        migrations.AlterField(
            model_name="version",
            name="product",
            field=models.ForeignKey(
                help_text="Выберите продукт",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="versions",
                to="catalog.product",
                verbose_name="Продукт",
            ),
        ),
    ]
