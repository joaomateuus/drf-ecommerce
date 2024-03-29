# Generated by Django 5.0.2 on 2024-02-29 13:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_created', null=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_modified', null=True, verbose_name='Modified at')),
                ('is_active', models.BooleanField(db_column='cs_active', default=True, verbose_name='Active')),
                ('name', models.CharField(db_column='tx_name', max_length=50, verbose_name='Name')),
            ],
            options={
                'db_table': 'tb_brands',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_created', null=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_modified', null=True, verbose_name='Modified at')),
                ('is_active', models.BooleanField(db_column='cs_active', default=True, verbose_name='Active')),
                ('name', models.CharField(db_column='tx_name', max_length=50, verbose_name='Name')),
                ('description', models.TextField(blank=True, db_column='tx_description', null=True, verbose_name='Description')),
            ],
            options={
                'db_table': 'tb_products_categories',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_created', null=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_modified', null=True, verbose_name='Modified at')),
                ('is_active', models.BooleanField(db_column='cs_active', default=True, verbose_name='Active')),
                ('quantity', models.IntegerField(db_column='nb_quantity', default=1, verbose_name='Quantity')),
                ('ordered', models.BooleanField(db_column='cs_ordered', default=False, verbose_name='Ordered')),
                ('order_item_price', models.FloatField(blank=True, db_column='nb_order_item_price', null=True, verbose_name='Order Item Price')),
                ('user', models.ForeignKey(db_column='id_user', db_index=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_order_items', to=settings.AUTH_USER_MODEL, verbose_name='User Order Items')),
            ],
            options={
                'db_table': 'tb_orderitems',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('PD', 'Paid'), ('WP', 'Waiting Payment'), ('RJ', 'Rejected')], default='WP', max_length=2, verbose_name='Order Status')),
                ('total_order_price', models.FloatField(blank=True, db_column='nb_total_order_price', null=True, verbose_name='Total Order Price')),
                ('user', models.ForeignKey(db_column='id_user', db_index=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_orders', to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('items', models.ManyToManyField(related_name='order_items', to='core.orderitem', verbose_name='Order Items')),
            ],
            options={
                'db_table': 'tb_orders',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_created', null=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_modified', null=True, verbose_name='Modified at')),
                ('is_active', models.BooleanField(db_column='cs_active', default=True, verbose_name='Active')),
                ('name', models.CharField(db_column='tx_name', max_length=50, verbose_name='Name')),
                ('description', models.TextField(blank=True, db_column='tx_description', null=True, verbose_name='Description')),
                ('availability', models.CharField(blank=True, choices=[('A', 'Available'), ('U', 'Unavailable')], max_length=1)),
                ('sku', models.CharField(blank=True, db_column='tx_sku', max_length=100, verbose_name='Sku')),
                ('price', models.FloatField(db_column='nb_price', verbose_name='Price')),
                ('quantity', models.IntegerField(db_column='nb_quantity', verbose_name='Quantity')),
                ('image_url', models.CharField(blank=True, db_column='tx_image_url', max_length=250, null=True, verbose_name='Image Url')),
                ('brand', models.ForeignKey(blank=True, db_column='id_brand', db_index=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_brands', to='core.brand', verbose_name='Product Brand')),
            ],
            options={
                'db_table': 'tb_products',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(db_column='id_product', db_index=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ordem_item_product', to='core.product', verbose_name='Order Item Product'),
        ),
        migrations.CreateModel(
            name='ProductSubCategory',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_created', null=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_modified', null=True, verbose_name='Modified at')),
                ('is_active', models.BooleanField(db_column='cs_active', default=True, verbose_name='Active')),
                ('name', models.CharField(db_column='tx_name', max_length=50, verbose_name='Name')),
                ('description', models.TextField(blank=True, db_column='tx_description', null=True, verbose_name='Description')),
                ('parent_category', models.ForeignKey(db_column='id_parent_category', db_index=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategory_categories', to='core.productcategory', verbose_name='Parent Category')),
            ],
            options={
                'db_table': 'tb_products_sub_categories',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(blank=True, db_column='id_product_subcategory', db_index=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_subcategories', to='core.productsubcategory', verbose_name='Product Sub Category'),
        ),
    ]
