# Generated by Django 3.2 on 2021-05-03 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0004_alter_product_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='account',
            field=models.CharField(choices=[('SELECT PRODUCT', 'SELECT PRODUCT'), ('Speaker', 'speaker'), ('Headphones', 'headphones'), ('Laptop', 'laptop'), ('Fridge', 'fridge')], default='PRODUCT AMOUNT', max_length=200),
        ),
    ]
