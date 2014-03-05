from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
	name = models.CharField(max_length=100)
	# add more properties here.
	# examples: https://docs.djangoproject.com/en/dev/topics/db/models/
	def __str__(self):
		return self.name
	
class Rating(models.Model):
	restaurant = models.ForeignKey("Restaurant",related_name="ratings")
	rating = models.FloatField()
	dimension = models.CharField(max_length=100)
	# link to a user here
	# voter = models.ForeignKey(User,related_name="ratings")
	
	date = models.DateField(auto_now_add=True)
	def __str__(self):
		return self.dimension
