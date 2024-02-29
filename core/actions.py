from core import models

class OrderActions:
    def update_price_after_item_update(user_id: int):
        order = models.Order.objects.filter(
            user__id=user_id
        ).first()
        
        order.total_order_price = sum(item.order_item_price for item in order.items.all())
        order.save()
    
    
    