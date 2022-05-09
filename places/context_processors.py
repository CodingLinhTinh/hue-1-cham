from .models import Place

def menu_links(request):
	links = Place.objects.all()
	return dict(links=links)