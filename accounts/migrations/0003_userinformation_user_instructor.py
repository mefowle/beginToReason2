# Generated by Django 3.1.2 on 2021-02-20 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_userinformation_user_instructor'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinformation',
            name='user_instructor',
            field=models.BooleanField(default=False),
        ),
    ]