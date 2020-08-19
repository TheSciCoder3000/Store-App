# Generated by Django 3.0.8 on 2020-08-19 04:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import my_store.models


class Migration(migrations.Migration):

    replaces = [('my_store', '0001_initial'), ('my_store', '0002_remove_orderitem_person'), ('my_store', '0003_auto_20200816_1430'), ('my_store', '0004_remove_orderitem_order'), ('my_store', '0005_orderitem_ref_code'), ('my_store', '0006_auto_20200816_1450'), ('my_store', '0007_remove_orders_ref_code'), ('my_store', '0008_orders_ref_code'), ('my_store', '0009_auto_20200816_1507'), ('my_store', '0010_auto_20200816_1511'), ('my_store', '0011_remove_orders_item_list'), ('my_store', '0012_remove_request_item_list'), ('my_store', '0013_auto_20200817_1710'), ('my_store', '0014_auto_20200817_1711'), ('my_store', '0015_auto_20200817_1713'), ('my_store', '0016_orders_ref_code'), ('my_store', '0017_request_ref_code'), ('my_store', '0018_auto_20200817_2108'), ('my_store', '0019_auto_20200817_2121'), ('my_store', '0020_auto_20200818_1642'), ('my_store', '0021_auto_20200818_1925'), ('my_store', '0022_auto_20200818_2346'), ('my_store', '0023_auto_20200819_0044')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=25)),
                ('my_image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='PrductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryTitle', models.CharField(max_length=20)),
                ('summary', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Product Categories',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('available', models.BooleanField()),
                ('item_count', models.FloatField(default=0)),
                ('price', models.FloatField(default=0)),
                ('price_per', models.CharField(default='kg', max_length=50)),
                ('last_Updated', models.DateTimeField(auto_now=True)),
                ('item_thresh', models.FloatField(blank=True, null=True)),
                ('discount', models.FloatField(default=0.1)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('product_category', models.ForeignKey(default='None', on_delete=django.db.models.deletion.SET_DEFAULT, to='my_store.PrductCategory')),
            ],
            options={
                'verbose_name_plural': 'Products',
                'ordering': ['product_category', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(null=True)),
                ('number', models.IntegerField(null=True)),
                ('add_message', models.TextField(blank=True, null=True)),
                ('time_ordered', models.DateTimeField(default=django.utils.timezone.now)),
                ('Person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ref_code', models.CharField(default=my_store.models.Orders.get_uuid, max_length=25, null=True, unique=True)),
                ('completed', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(null=True)),
                ('number', models.IntegerField(null=True)),
                ('add_message', models.TextField(blank=True, null=True)),
                ('time_ordered', models.DateTimeField(default=django.utils.timezone.now)),
                ('Person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ref_code', models.CharField(default=my_store.models.Request.get_uuid, max_length=25, null=True, unique=True)),
                ('completed', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Requests',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10000, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_store.Products')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='my_store.Orders')),
            ],
        ),
        migrations.CreateModel(
            name='RequestItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10000, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_store.Products')),
                ('request', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='my_store.Request')),
            ],
        ),
    ]
