from django.db import models
from shop.models import *
# Create your models here.

class cartList(models.Model):
	cart_id=models.CharField(max_length=250,unique=True)
	date_added=models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.cart_id
class items(models.Model):
	product=models.ForeignKey(products,on_delete=models.CASCADE)
	cart=models.ForeignKey(cartList,on_delete=models.CASCADE)
	qty=models.IntegerField()
	active=models.BooleanField(default=True)

	def __str__(self):
		return self.product

	def total(self):
		return self.product.price*self.qty