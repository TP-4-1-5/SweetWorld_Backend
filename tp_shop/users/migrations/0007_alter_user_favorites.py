# Generated by Django 4.2 on 2023-05-18 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_user_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='favorites',
            field=models.CharField(default='0,', max_length=100),
        ),
    ]
