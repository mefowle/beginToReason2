# Generated by Django 3.0.3 on 2020-04-28 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200212_1351'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Code_Template',
        ),
        migrations.DeleteModel(
            name='Reference',
        ),
    ]
