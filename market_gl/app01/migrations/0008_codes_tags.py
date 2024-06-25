# Generated by Django 4.2.11 on 2024-04-18 09:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app01", "0007_codes_code_id_alter_codes_location"),
    ]

    operations = [
        migrations.CreateModel(
            name="Codes_Tags",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="编号"
                    ),
                ),
                ("code_id", models.IntegerField(verbose_name="二维码ID")),
                ("goods_id", models.IntegerField(verbose_name="商品id")),
            ],
        ),
    ]