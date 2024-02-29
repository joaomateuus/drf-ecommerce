from core import models
from account import models as auth_models
from django.db import transaction

class OrderUseCase:
    def __init__(self, user: auth_models.User, product: models.Product, quantity: int) -> None:
        self.user = user
        self.product = product
        self.quantity = quantity

    def main(self) -> 'models.Order':
        try:
            with transaction.atomic():
                order_item = models.OrderItem.objects.create(
                    user=self.user,
                    product=self.product,
                    quantity=self.quantity
                ) 
                
                order, _ = models.Order.objects.get_or_create(
                    user=self.user,
                )
                order.items.add(order_item.id)
                
                total_order_price = sum(item.order_item_price for item in order.items.all())
                order.total_order_price = total_order_price
                order.save()
            return order
        except Exception as e:
            print(str(e))
            
        
            