# Generated by Django 4.1 on 2023-07-25 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0015_orders_razor_pay_order_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orders",
            name="amount",
            field=models.IntegerField(default="", max_length=100),
        ),
    ]
