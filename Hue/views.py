from django.shortcuts import render
from places.models import Place

def home(request):
	places = Place.objects.all().filter()

	context = {
		'places': places,
	}
	return render(request, 'home.html', context)

def about(request):
	return render(request, 'about.html')

