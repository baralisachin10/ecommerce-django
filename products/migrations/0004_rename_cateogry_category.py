# Generated by Django 4.1.3 on 2023-08-22 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_cateogry_name_cateogry_category_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cateogry',
            new_name='Category',
        ),
    ]
