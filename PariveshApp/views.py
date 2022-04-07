from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView
from .models import Plantation
from django.contrib.auth.models import User
from .forms import AddPlantForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from decouple import config
import requests


# Create your views here.
def AboutUs(request):
    return render(request, 'about_us.html', {})

def Knowledge(request):
    return render(request, 'knowledge.html', {})

def News(request):
    url = "https://newsapi.org/v2/everything?q=environment&apiKey=" + config('api_key')
    response = requests.get(url)
    data = response.json()
    news_list = data['articles']

    context = {
        'news_list': news_list
    }

    return render(request, 'news.html', context)


class HomeView(ListView):
    model = Plantation
    template_name = 'home.html'
    ordering = ['-date_time']
    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        user_count = User.objects.all().count()
        plant_count = Plantation.objects.all().count()
        context["user_count"] = user_count
        context["plant_count"] = plant_count
        return context

class ImageGalleryView(ListView):
    model = Plantation
    template_name = 'image_gallery.html'
    ordering = ['-date_time']

class AddPlantView(CreateView):
    model = Plantation
    form_class  = AddPlantForm
    template_name = 'add_plant.html'
    
    def form_valid(self, form):
        form.instance.planter = self.request.user
        return super().form_valid(form)