# Generated by Django 5.0.2 on 2024-03-01 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(db_column='tx_name', max_length=256, verbose_name='Name'),
        ),
    ]
