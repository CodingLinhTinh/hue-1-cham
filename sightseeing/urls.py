from django.urls import path
from . import views


urlpatterns = [
    path('', views.sightseeing, name='sightseeing'),
    path('<slug:place_slug>/', views.sightseeing, name= 'sightseeing_by_places'),
    path('<slug:place_slug>/<slug:sightseeing_slug>', views.sightseeing_detail, name= 'sightseeing_detail'),

]
