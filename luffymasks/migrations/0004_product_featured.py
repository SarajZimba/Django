# Generated by Django 4.1.7 on 2023-04-11 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("luffymasks", "0003_alter_product_name_alter_product_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="featured",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
