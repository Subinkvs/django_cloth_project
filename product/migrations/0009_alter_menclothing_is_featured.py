# Generated by Django 4.2.6 on 2023-10-27 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_menclothing_is_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menclothing',
            name='is_featured',
            field=models.BooleanField(default=True),
        ),
    ]