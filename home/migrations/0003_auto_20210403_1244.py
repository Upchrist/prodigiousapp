# Generated by Django 3.1.7 on 2021-04-03 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210403_1146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='setting',
            old_name='banner',
            new_name='cart_icon',
        ),
        migrations.RenameField(
            model_name='setting',
            old_name='offer',
            new_name='menu_icon',
        ),
    ]
