# Generated by Django 4.2.1 on 2023-05-13 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productscategory', '0002_alter_productcategory_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='name',
            field=models.TextField(max_length=128),
        ),
    ]
