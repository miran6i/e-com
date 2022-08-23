from django.contrib.auth import get_user_model
from django.db import models

from product.models import Product


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='order_items')


class Order(models.Model):
    items = models.ManyToManyField('OrderItem')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    ordered_at = models.DateTimeField()


