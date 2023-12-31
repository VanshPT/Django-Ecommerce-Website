# Generated by Django 4.1 on 2023-07-15 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0007_orders"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orders",
            name="address",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="orders",
            name="address_line_2",
            field=models.CharField(default="", max_length=500),
        ),
        migrations.AlterField(
            model_name="orders",
            name="city",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.AlterField(
            model_name="orders",
            name="email",
            field=models.EmailField(default="", max_length=50),
        ),
        migrations.AlterField(
            model_name="orders",
            name="items_json",
            field=models.CharField(default="", max_length=100000),
        ),
        migrations.AlterField(
            model_name="orders",
            name="name",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="orders",
            name="phone",
            field=models.CharField(default="", max_length=40),
        ),
        migrations.AlterField(
            model_name="orders",
            name="state",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.AlterField(
            model_name="orders",
            name="zip_code",
            field=models.CharField(default="", max_length=30),
        ),
    ]
