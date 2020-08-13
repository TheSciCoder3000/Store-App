# Generated by Django 3.0.8 on 2020-08-13 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_store', '0013_auto_20200813_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('available', models.BooleanField()),
                ('item_count', models.IntegerField()),
                ('price', models.IntegerField(default=0)),
                ('price_per', models.CharField(default='kg', max_length=50)),
                ('product_category', models.CharField(choices=[('Fruits', 'Fruits'), ('Meat', 'Meat'), ('Seafood', 'Seafood'), ('Vegetable', 'Vegetable')], default='Seafood', max_length=100)),
                ('last_Updated', models.DateTimeField(auto_now=True)),
                ('item_thresh', models.IntegerField(blank=True, null=True)),
                ('discount', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['product_category', 'title'],
            },
        ),
    ]