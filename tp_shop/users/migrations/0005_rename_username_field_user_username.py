# Generated by Django 4.2.1 on 2023-05-11 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_username_user_username_field_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='USERNAME_FIELD',
            new_name='username',
        ),
    ]
