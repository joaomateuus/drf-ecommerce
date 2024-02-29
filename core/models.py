from typing import Iterable
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
        verbose_name='Description'
    )
    
    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        managed = True
        db_table = 'tb_products_categories'


class ProductSubCategory(ModelBase):
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
    parent_category = models.ForeignKey(
        'ProductCategory',
        on_delete=models.CASCADE,
        db_column='id_parent_category',
        db_index=False,
        null=True,
        related_name='subcategory_categories',
        verbose_name='Parent Category'
    )
    
    def __str__(self) -> str:
        return f'{self.name} - {self.parent_category.name}'
    
    class Meta:
        managed = True
        db_table = 'tb_products_sub_categories'


class Brand(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        max_length=50,
        null=False,
        blank=False,
        verbose_name='Name'
    )
    
    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        managed = True
        db_table = 'tb_brands'


class Product(ModelBase):
    class Availability(models.TextChoices):
        AVAILABLE = 'A', ('Available')
        UNAVAILABLE = 'U', ('Unavailable')
    
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
    availability = models.CharField(
        max_length=1,
        null=False,
        blank=True,
        choices=Availability.choices
    )
    sku = models.CharField(
        db_column='tx_sku',
        max_length=100,
        null=False,
        blank=True,
        verbose_name='Sku',
    )
    subcategory = models.ForeignKey(
        'ProductSubCategory',
        on_delete=models.SET_NULL,
        db_column='id_product_subcategory',
        db_index=False,
        null=True,
        blank=True,
        related_name='product_subcategories',
        verbose_name='Product Sub Category'
    )
    brand = models.ForeignKey(
        'Brand',
        on_delete=models.SET_NULL,
        db_column='id_brand',
        db_index=False,
        null=True,
        blank=True,
        related_name='product_brands',
        verbose_name='Product Brand'
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
    image_url = models.CharField(
        db_column='tx_image_url',
        max_length=250,
        null=True,
        blank=True,
        verbose_name='Image Url'
    )

    def generate_sku(self):
        sku_uuid = str(uuid.uuid4().hex)[:8]
        prefix = f"{self.subcategory.parent_category.name}-{sku_uuid}"
        
        sku_uuid =  str(uuid.uuid4().hex)[8:16]
        sufix = f'{self.name[:3]}{self.price:.2f}-{sku_uuid}'
        
        return f"{prefix}{sufix}"
    
    def save(self, *args, **kwargs):
        self.sku = self.generate_sku()
        
        if self.quantity > 0:
            self.availability = self.Availability.AVAILABLE
        else:
            self.availability = self.Availability.UNAVAILABLE
        
            
        super().save(*args, **kwargs)
        
    def __str__(self) -> str:
        return f'{self.name} - {self.sku}'

    class Meta:
        managed = True
        db_table = 'tb_products'


class OrderItem(ModelBase):
    user = models.ForeignKey(
        'account.User',
        on_delete=models.CASCADE,
        db_column='id_user',
        db_index=False,
        null=False,
        related_name='user_order_items',
        verbose_name='User Order Items'
    )
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        db_column='id_product',
        db_index=False,
        null=False,
        related_name='ordem_item_product',
        verbose_name='Order Item Product'
    )
    quantity = models.IntegerField(
        db_column='nb_quantity',
        null=False,
        blank=False,
        default=1,
        verbose_name='Quantity'
    )
    ordered = models.BooleanField(
        db_column='cs_ordered',
        null=False,
        default=False,
        verbose_name='Ordered'
    )
    order_item_price = models.FloatField(
        db_column='nb_order_item_price',
        null=True,
        blank=True,
        verbose_name='Order Item Price', 
    )

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def save(self, *args, **kwargs):
        self.order_item_price = self.get_total_item_price()

    class Meta:
        managed = True
        db_table = 'tb_order_items'


class Order(models.Model):
    class Status(models.TextChoices):
        PAID = 'PD', ('Paid')
        WAITING_PAYMENT = 'WP', ('Waiting Payment')
        REJECTED = 'RJ', ('Rejected')

    user = models.ForeignKey(
        'account.User',
        on_delete=models.CASCADE,
        db_column='id_user',
        db_index=False,
        null=False,
        related_name='user_orders',
        verbose_name='User'
    )
    items = models.ManyToManyField(
        'Product',
        related_name='order_products',
        verbose_name='Order Items'
    )
    status = models.CharField(
        max_length=2,
        null=False,
        blank=True,
        choices=Status.choices,
        default=Status.WAITING_PAYMENT,
        verbose_name='Order Status'
    )
    total_order_price = models.FloatField(
        db_column='nb_total_order_price',
        null=True,
        blank=True,
        verbose_name='Total Order Price',
    )

    def calculate_total_order_price(self):
        self.total_order_price = sum(
            item.order_item_price for item in self.items.all()
        )
    
    class Meta:
        managed = True
        db_table = 'tb_orders'
