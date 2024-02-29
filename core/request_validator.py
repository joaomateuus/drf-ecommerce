from rest_framework import serializers
from core import models
from account import models as auth_models

class CreateOrderItemSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=auth_models.User.objects.all()
    )
    product = serializers.PrimaryKeyRelatedField(
        queryset=models.Product.objects.all()
    )
    quantity = serializers.IntegerField()

    class Meta:
        model = models.Order
        fields = ['user', 'product', 'quantity']