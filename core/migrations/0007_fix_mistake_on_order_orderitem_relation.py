# Generated by Django 5.0.2 on 2024-02-29 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_create_orders_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(related_name='order_items', to='core.orderitem', verbose_name='Order Items'),
        ),
    ]