# Generated by Django 4.2.1 on 2023-05-12 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productscategory', '0002_alter_productcategory_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=512)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(upload_to='products_image')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productscategory.productcategory')),
            ],
        ),
    ]
