# Generated by Django 3.2.19 on 2023-06-20 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0004_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='approved',
        ),
    ]
