# Generated by Django 3.1.3 on 2020-12-01 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='buyer_name',
            new_name='buyer_username',
        ),
    ]
