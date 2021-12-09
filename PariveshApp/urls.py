from django.urls import path
from .views import HomeView, AboutUs, AddPlantView, ImageGalleryView, Knowledge

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('image-gallery', ImageGalleryView.as_view(), name="gallery"),
    path('add-plant/', AddPlantView.as_view(), name="add-plant"),
    path('about-us/', AboutUs, name="about-us"),
    path('knowledge/', Knowledge, name="knowledge"),
]