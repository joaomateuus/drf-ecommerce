from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from core import models
from core import actions

@receiver(pre_save, sender=models.OrderItem)
def update_product_quantity(sender, instance: models.OrderItem, **kwargs):
    if instance.id:
        actions.OrderActions.update_product_quantity(instance)


@receiver(post_save, sender=models.OrderItem)
def update_order_price_for_update(sender, instance: models.OrderItem, created, **kwargs):
    if not created:
        actions.OrderActions.update_order_total_value(instance)
        
        
@receiver(post_delete, sender=models.OrderItem)
def update_order_price_for_delete(sender, instance: models.OrderItem, **kwargs):
    actions.OrderActions.update_order_total_value(instance)

