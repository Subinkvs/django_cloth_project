# Generated by Django 4.2.1 on 2023-10-25 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_menclothing_name_alter_category_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menclothing',
            name='title',
            field=models.TextField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]