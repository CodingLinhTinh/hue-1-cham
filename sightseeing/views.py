from django.shortcuts import render, get_object_or_404
from .models import Sightseeing
from places.models import Place

from django.db.models import Q


# Create your views here.
def sightseeing(request, place_slug=None):
	places = None
	sightseeings = None

	if place_slug != None:
		places = get_object_or_404(Place, slug=place_slug)
		sightseeings = Sightseeing.objects.filter(place=places, is_available=True)
	else:
		sightseeings = Sightseeing.objects.all().filter(is_available=True).order_by('id')

	context = {
		'sightseeings':sightseeings,
	}

	return render(request, 'sightseeing/sightseeing.html', context)


def sightseeing_detail(request, place_slug=None, sightseeing_slug=None):
	try:
		single_sightseeing = Sightseeing.objects.get(place__slug=place_slug, slug=sightseeing_slug)

	except Exception as e:
		raise e

	context = {
		'single_sightseeing': single_sightseeing,
	}
	return render(request, 'sightseeing/sightseeing_detail.html', context)


