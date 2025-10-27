from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('session/', views.session_page, name='session_page'),
    path('cache/', views.cache_page, name='cache_page'),
]
