# Generated by Django 3.2 on 2022-07-28 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20220716_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_limited_edition',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
