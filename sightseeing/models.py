from django.db import models
from places.models import Place
from django.urls import reverse

# Create your models here.
class Sightseeing(models.Model):
	sight_name 			= models.CharField(max_length=200, unique=True)
	slug 				= models.SlugField(max_length=200, unique=True)
	description 		= models.TextField(max_length=3000, blank=True)

	images 				= models.ImageField(upload_to='photos/sightseeing',)
	images_360_1 		= models.ImageField(upload_to='photos/image_360', null=True )
	images_360_2 		= models.ImageField(upload_to='photos/image_360', null=True )
	images_360_3 		= models.ImageField(upload_to='photos/image_360', null=True)

	yaw1				= models.IntegerField()
	yaw2				= models.IntegerField()
	yaw3				= models.IntegerField()

	is_available 		= models.BooleanField(default=True)
	place 				= models.ForeignKey(Place, on_delete=models.CASCADE)
	created_date 		= models.DateTimeField(auto_now_add=True)
	modified_date 		= models.DateTimeField(auto_now=True)

	def get_url(self):
		return reverse('sightseeing_detail', args=[self.place.slug, self.slug])

	def __str__(self):
		return self.sight_name