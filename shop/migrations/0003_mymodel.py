# Generated by Django 3.0.5 on 2020-05-02 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuff', models.CharField(default=None, max_length=255, verbose_name='Stuff')),
            ],
        ),
    ]
