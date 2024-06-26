from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/',views.signup, name="signup"),
    path('signin/',views.signin, name="signin"),
    path('logout/',views.logoutUser, name="logout"),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/',views.edit_profile, name='edit_profile'),
]