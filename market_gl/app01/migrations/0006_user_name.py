# Generated by Django 4.2.11 on 2024-04-15 06:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app01", "0005_tags"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="name",
            field=models.CharField(default="", max_length=10, verbose_name="名字"),
        ),
    ]
