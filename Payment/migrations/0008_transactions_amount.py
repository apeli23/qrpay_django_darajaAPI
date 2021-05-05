# Generated by Django 3.2 on 2021-05-03 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0007_auto_20210503_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='amount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='price', to='Payment.product'),
        ),
    ]
