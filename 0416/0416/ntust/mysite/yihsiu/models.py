from django.db import models

# Create your models here.
class Myid(models.Model):
	name = models.CharField(max_length=20)
	phone_number = models.CharField(max_length=15)
	adress=models.CharField(max_length=50,blank=True)
	def __str__(self):
		return self.name


