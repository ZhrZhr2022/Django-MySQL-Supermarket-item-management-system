# Generated by Django 4.2.11 on 2024-04-10 15:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app01", "0003_remove_user_identity"),
    ]

    operations = [
        migrations.AddField(
            model_name="cars",
            name="status",
            field=models.IntegerField(default=0, verbose_name="状态信息"),
        ),
    ]