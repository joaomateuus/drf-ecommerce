from django_filters import filterset, widgets
from core import models
from account import filter_options as options

class ProductFilter(filterset.FilterSet):
    id = filterset.NumberFilter(
        lookup_expr=options.EXACT,
        label='Product ID'
    )
    name = filterset.CharFilter(
        lookup_expr=options.ICONTAINS,
        label='Name'
    )
    description = filterset.CharFilter(
        lookup_expr=options.ICONTAINS,
        label='Description'
    )
    availability = filterset.CharFilter(
        lookup_expr=options.EXACT,
        label='Availability'
    )
    sku = filterset.CharFilter(
        lookup_expr=options.ICONTAINS,
        label='SKU'
    )
    category_id = filterset.NumberFilter(
        lookup_expr=options.EXACT,
        field_name='subcategory__parent_category__id', 
        label='Category ID',
    )
    category_name = filterset.CharFilter(
        lookup_expr=options.ICONTAINS,
        field_name='subcategory__parent_category__name', 
        label='Category Name', 
    )
    subcategory_id = filterset.NumberFilter(
        lookup_expr=options.EXACT,
        field_name='subcategory__id', 
        label='Subcategory ID',
    )
    subcategory_name = filterset.CharFilter(
        lookup_expr=options.ICONTAINS,
        field_name='subcategory__name', 
        label='Subcategory Name', 
    )
    price = filterset.NumberFilter(
        lookup_expr=options.EXACT,
        label='Price'
    )
    quantity = filterset.NumberFilter(
        lookup_expr=options.EXACT,
        label='Quantity'
    )

    class Meta:
        model = models.Product
        fields = [
            'id',
            'name',
            'description',
            'availability',
            'sku',
            'category_id',
            'category_name',
            'subcategory_id',
            'subcategory_name',
            'price',
            'quantity',
        ]