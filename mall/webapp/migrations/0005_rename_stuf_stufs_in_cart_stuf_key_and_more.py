# Generated by Django 4.1.2 on 2022-12-13 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_stufs_in_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stufs_in_cart',
            old_name='stuf',
            new_name='stuf_key',
        ),
        migrations.RemoveField(
            model_name='stufs_in_cart',
            name='amount_stufs',
        ),
        migrations.AddField(
            model_name='stufs_in_cart',
            name='amount_stuf',
            field=models.PositiveIntegerField(default=1, verbose_name='amount_stuf'),
            preserve_default=False,
        ),
    ]