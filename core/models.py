from django.db import models
import uuid

class ModelBase(models.Model):
    id = models.BigAutoField(
        db_column='id',
        primary_key=True
    )
    created_at = models.DateTimeField(
        db_column='dt_created',
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name = 'Created at'
    )
    modified_at = models.DateTimeField(
        db_column='dt_modified',
        auto_now=True,
        null=True,
        blank=True,
        verbose_name = 'Modified at'
    )
    is_active = models.BooleanField(
        db_column='cs_active',
        null=False,
        default=True,
        verbose_name = 'Active'
    )

    class Meta:
        abstract = True


class ProductCategory(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        max_length=50,
        null=False,
        blank=False,
        verbose_name='Name'
    )
    description = models.TextField(
        db_column='tx_description',
        null=True,
        blank=True,
        verbose_name='Name'
    )

    class Meta:
        managed = True
        db_table = 'tb_product_category'


class Product(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        max_length=50,
        null=False,
        blank=False,
        verbose_name='Name'
    )
    description = models.TextField(
        db_column='tx_description',
        null=True,
        blank=True,
        verbose_name='Description'
    )
    sku = models.CharField(
        db_column='tx_sku',
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Sku',
    )
    category = models.ForeignKey(
        'ProductCategory',
        on_delete=models.DO_NOTHING,
        db_column='id_product_category',
        db_index=False,
        null=False,
        related_name='product_categories',
        verbose_name='Product Category'
    )
    price = models.FloatField(
        db_column='nb_price',
        null=False,
        blank=False,
        verbose_name='Price'
    )
    quantity = models.IntegerField(
        db_column='nb_quantity',
        null=False,
        blank=False,
        verbose_name='Quantity'
    )

    def generate_sku(self):
        sku_base = f"{self.category.name}-{self.name[:3]}-{self.price:.2f}"
        sku_uuid = str(uuid.uuid4().hex)[:8]
        return f"{sku_base}-{sku_uuid}"
    
    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = self.generate_sku()
        super().save(*args, **kwargs)

    class Meta:
        managed = True
        db_table = 'tb_products'
