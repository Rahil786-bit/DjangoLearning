# Generated by Django 4.0.3 on 2022-04-10 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
