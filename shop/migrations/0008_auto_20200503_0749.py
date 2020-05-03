# Generated by Django 3.0.5 on 2020-05-03 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20200503_0608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='prices',
        ),
        migrations.AddField(
            model_name='valueandprices',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Product'),
        ),
    ]
