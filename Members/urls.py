from django.urls import path
from .views import UserSettingsEditView, ShowProfilePageView, EditProfilePageView, CreateProfilePageView, ChangePasswordView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/',views.signup, name="signup"),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('edit-settings/',UserSettingsEditView.as_view(), name="edit-settings"),    
    path('password/',ChangePasswordView.as_view(template_name='registration/change_password.html'), name="change-password"),
    path('password-changed/',views.password_changed, name="password-changed"),
    # path('change-password/',auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html', success_url = 'registration/password_changed.html'), name='change-password'),
    path('<int:pk>/profile',ShowProfilePageView.as_view(), name="show-profile-page"),
    path('<int:pk>/edit-profile-page',EditProfilePageView.as_view(), name="edit-profile-page"),
    path('create-profile-page',CreateProfilePageView.as_view(), name="create-profile-page"),
]