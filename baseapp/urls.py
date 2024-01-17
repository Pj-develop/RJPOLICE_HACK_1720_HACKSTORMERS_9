from django.urls import path
from . import views


urlpatterns = [
    path('', views.dash_plot, name='base'),
    
    path('addcase/', views.addcase, name='addcase'),
    path('aichat/', views.aichat, name='aichat'),
    path('index/', views.dash_plot, name='index'),
]
