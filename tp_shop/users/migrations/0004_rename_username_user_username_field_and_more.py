# Generated by Django 4.2.1 on 2023-05-11 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_favorites'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='USERNAME_FIELD',
        ),
        migrations.AlterField(
            model_name='user',
            name='favorites',
            field=models.CharField(default='0', max_length=100),
        ),
    ]
