from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='base'),
    path('addcase/', views.addcase, name='addcase'),
    path('index/', views.index, name='index'),
]
