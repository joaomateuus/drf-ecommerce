from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from core import models
from core import actions

@receiver(post_save, sender=models.OrderItem)
def update_order_price_for_update(sender, instance: models.OrderItem, created, **kwargs):
    if not created:
        actions.OrderActions.update_price_after_item_update(instance.user.id)


@receiver(post_delete, sender=models.OrderItem)
def update_order_price_for_delete(sender, instance: models.OrderItem, **kwargs):
    actions.OrderActions.update_price_after_item_update(instance.user.id)

