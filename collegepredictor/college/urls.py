from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('predict/', views.result, name='result'),
    path('about/', views.about, name='about'),
]
