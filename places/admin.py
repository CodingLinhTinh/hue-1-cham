from django.contrib import admin
from .models import Place

# Register your models here.
class PlaceAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('place_name', )}
	list_display = ('place_name', 'slug')

admin.site.register(Place, PlaceAdmin)