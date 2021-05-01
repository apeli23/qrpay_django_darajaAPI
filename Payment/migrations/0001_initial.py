# Generated by Django 3.2 on 2021-04-29 20:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.IntegerField(default=0)),
                ('amount', models.IntegerField(default=0)),
                ('code', models.ImageField(blank=True, upload_to='qr_codes')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Payment.product')),
            ],
        ),
    ]
