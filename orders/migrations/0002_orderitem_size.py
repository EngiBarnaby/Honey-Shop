# Generated by Django 3.0.5 on 2020-05-11 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='size',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=5),
            preserve_default=False,
        ),
    ]