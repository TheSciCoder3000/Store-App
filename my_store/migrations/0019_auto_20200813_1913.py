# Generated by Django 3.0.8 on 2020-08-13 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_store', '0018_auto_20200813_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='discount',
            field=models.FloatField(default=0.1),
        ),
    ]
