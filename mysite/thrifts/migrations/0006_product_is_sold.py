# Generated by Django 3.1.3 on 2020-12-12 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thrifts', '0005_delete_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_sold',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]