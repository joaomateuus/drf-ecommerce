from core import models

class OrderActions:
    def update_product_quantity(
        instance: models.OrderItem,
    ):
        old_instance = models.OrderItem.objects.get(id=instance.id)
        same_product = old_instance.product == instance.product
        changed_quantity = old_instance.quantity != instance.quantity

        if same_product and changed_quantity:
            OrderActions.update_quantity_for_same_product(
                instance,
                old_instance
            )
            return
        
        if not same_product:
            OrderActions.handle_order_product_change(
                instance,
                old_instance
            )
            return
        
        
    def update_quantity_for_same_product(
        instance: models.OrderItem,
        old_instance: models.OrderItem
    ):
        difference = instance.quantity - old_instance.quantity
            
        if instance.quantity > old_instance.quantity:     
            instance.product.quantity += abs(difference)
            instance.product.save()
            return
        
        instance.product.quantity -= abs(difference)
        instance.product.save()
        return 
           
           
    def handle_order_product_change(
        instance: models.OrderItem,
        old_instance: models.OrderItem
    ):
        old_product = models.Product.objects.filter(
            id=old_instance.product.id
        ).first()
        
        old_product.quantity += old_instance.quantity
        old_product.save()
        
        instance.product.quantity -= instance.quantity
        instance.product.save()
        

    def update_order_total_value(instance: models.OrderItem):
        order = models.Order.objects.filter(
            user=instance.user
        ).first()
        
        order.total_order_price = sum(item.order_item_price for item in order.items.all())
        order.save()
    
    
    