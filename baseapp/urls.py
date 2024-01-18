from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    
    path('addcase/', views.addcase, name='addcase'),
    path('aichat/', views.aichat, name='aichat'),
    path('analyzeai/', views.dash_plot, name='analyzeai'),
    path('home/', views.home, name='home'),
]