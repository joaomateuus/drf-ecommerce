# Generated by Django 5.0.2 on 2024-02-29 07:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_order_user_alter_orderitem_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(db_column='id_product', db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='ordem_item_product', to='core.product', verbose_name='Order Item Product'),
        ),
    ]