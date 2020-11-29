from django.urls import path, include
from .api import RegistrationAPI, LoginAPI, UserAPI
from knox import views as knox_views
from . import views
from rest_framework import routers

urlpatterns = [
    path('register/', RegistrationAPI.as_view()),
    path('login/', LoginAPI.as_view()),
    path('user/', UserAPI.as_view()),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('profile/<username>/', views.profile, name='profile'),
    path('project/<post>', views.project, name='project')
]
