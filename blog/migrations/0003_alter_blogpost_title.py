# Generated by Django 4.1 on 2023-07-19 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_blogpost_chead01_blogpost_chead02_blogpost_chead11_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="title",
            field=models.CharField(max_length=500),
        ),
    ]
