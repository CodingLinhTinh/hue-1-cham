from django.contrib import admin
from .models import Sightseeing
# Register your models here.


class SightseeingAdmin(admin.ModelAdmin):
	list_display = ('sight_name', 'description', 'slug', 'images_360_1','images_360_2','images_360_3','yaw1','yaw2','yaw3','place', 'created_date', 'modified_date', 'is_available')
	prepopulated_fields = {'slug': ('sight_name',)}

admin.site.register(Sightseeing, SightseeingAdmin)