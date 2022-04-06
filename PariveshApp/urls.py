from django.urls import path
<<<<<<< HEAD
from .views import *
=======
from .views import HomeView, AboutUs, AddPlantView, ImageGalleryView, Knowledge, News
>>>>>>> 9973761da383d491b43a454e51805aa157c08f21

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('image-gallery', ImageGalleryView.as_view(), name="gallery"),
    path('add-plant/', AddPlantView.as_view(), name="add-plant"),
    path('about-us/', AboutUs, name="about-us"),
    path('environment-updates/', News, name="news"),
    path('knowledge/', Knowledge, name="knowledge"),
]