from django.db import models
from django.urls import reverse

# Create your models here.

class Place(models.Model):
	place_name 		= models.CharField(max_length=100, unique=True)
	slug 			= models.SlugField(max_length=100, unique=True)
	description 	= models.TextField(max_length=2000, blank=True)
	place_img 		= models.ImageField(upload_to='photos/places', blank=True)

	class Meta:
		verbose_name = 'place'
		verbose_name_plural = 'places'

	def __str__(self):
		return self.place_name

	def get_url(self):
		return reverse('sightseeing_by_places', args=[self.slug])




