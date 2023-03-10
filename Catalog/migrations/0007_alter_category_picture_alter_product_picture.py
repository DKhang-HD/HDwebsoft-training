# Generated by Django 4.1.7 on 2023-02-23 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0006_product_price_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='picture',
            field=models.ImageField(blank=True, upload_to='Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, upload_to='Product'),
        ),
    ]
