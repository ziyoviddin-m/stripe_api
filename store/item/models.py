import stripe
from django.conf import settings
from django.db import models

stripe.api_key = settings.STRIPE_SECRET_KEY


class Item(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stripe_item_price_id = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.name
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.stripe_item_price_id:
            stripe_product_price = self.create_stripe_product_price()
            self.stripe_item_price_id = stripe_product_price['id']
        super().save(force_insert, force_update, using, update_fields)
    
    def create_stripe_product_price(self):
        stripe_product = stripe.Product.create(name=self.name)
        stripe_product_price = stripe.Price.create(
            product=stripe_product['id'], unit_amount=round(self.price * 100), currency='rub')
        return stripe_product_price


class OrderQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(order.items.price for order in self)


class Order(models.Model):
    items = models.ForeignKey(Item, on_delete=models.CASCADE)

    objects = OrderQuerySet.as_manager()

    def __str__(self):
        return self.items.name

