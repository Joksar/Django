# Generated by Django 3.2.7 on 2021-11-01 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basketapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basket',
            old_name='products',
            new_name='product',
        ),
    ]
