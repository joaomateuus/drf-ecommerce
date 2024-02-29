# Generated by Django 5.0.2 on 2024-02-29 07:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_orderitem_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(db_column='id_product', db_index=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ordem_item_product', to='core.product', verbose_name='Order Item Product'),
        ),
    ]