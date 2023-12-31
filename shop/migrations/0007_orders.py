# Generated by Django 4.1 on 2023-07-15 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0006_contact"),
    ]

    operations = [
        migrations.CreateModel(
            name="Orders",
            fields=[
                ("order_id", models.AutoField(primary_key=True, serialize=False)),
                ("items_json", models.CharField(max_length=100000)),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=50)),
                ("address", models.CharField(max_length=100)),
                ("address_line_2", models.CharField(max_length=500)),
                ("city", models.CharField(max_length=50)),
                ("state", models.CharField(max_length=50)),
                ("zip_code", models.CharField(max_length=30)),
                ("phone", models.CharField(max_length=40)),
            ],
        ),
    ]
