from django.db import models  
from .human_model import Human

# Car model
class Car(models.Model):
	person      = models.ForeignKey(Human, on_delete=models.CASCADE)
	brand       = models.CharField(max_length=100, default='Benz')
	color       = models.CharField(max_length=100, default='Black')
	price       = models.IntegerField(default=80000)

	def __str__(self):
		return self.brand
