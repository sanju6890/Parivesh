from django.shortcuts import get_object_or_404, render
from django.urls.base import reverse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView, CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, ChangePasswordForm, ProfilePageForm, EditProfilePageForm
from PariveshApp.models import Profile, Plantation

# Create your views here.

def password_changed(request):
    return render(request, 'registration/password_changed.html',{})

class ChangePasswordView(PasswordChangeView):
    form_class = ChangePasswordForm
    success_url = reverse_lazy('password-changed')

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_profile_page.html'
        
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)  

class EditProfilePageView(generic.UpdateView):
    model = Profile
    form_class = EditProfilePageForm
    template_name = 'registration/edit_profile_page.html'
    success_url = reverse_lazy('home')

class UserSettingsEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_user_settings.html'
    success_url = reverse_lazy('home')
    def get_object(self):
        return self.request.user

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        context["user_plants"] = Plantation.objects.filter(planter = page_user.user)
        return context 