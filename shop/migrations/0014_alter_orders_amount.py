# Generated by Django 4.1 on 2023-07-24 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0013_alter_orders_amount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orders",
            name="amount",
            field=models.CharField(default="", max_length=100),
        ),
    ]
