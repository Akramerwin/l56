# Generated by Django 4.1.2 on 2022-12-13 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_rename_stuf_stufs_in_cart_stuf_key_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stufs_in_cart',
            name='amount_stuf',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='amount_stuf'),
        ),
    ]
