from django.db import models
from shop.models import product

from django.contrib.auth.models import User
# Create your models here.
class Cart(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    date_added=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product.name

    def subtotal(self):
        return self.quantity*self.product.price
