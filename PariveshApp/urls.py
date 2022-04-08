from django.urls import path

from .views import *
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('plantations-on-parivesh/', PlantationView.as_view(), name="plant-list"),
    path('image-gallery/', ImageGalleryView.as_view(), name="gallery"),
    path('add-plant/', AddPlantView.as_view(), name="add-plant"),
    path('about-us/', AboutUs, name="about-us"),
    path('environment-updates/', News, name="news"),
    path('knowledge/', Knowledge, name="knowledge"),
]