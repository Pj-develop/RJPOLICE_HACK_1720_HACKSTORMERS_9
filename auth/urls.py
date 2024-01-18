from .views import RegisterView, UsernameValidationView,EmailValidationView,LoginView,export_to_pdf,ViewCase,hdfcapi
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('validate-username', csrf_exempt(UsernameValidationView.as_view()), name='validate-username'),
    path('validate-email',csrf_exempt(EmailValidationView.as_view()),name='validate-email'),
    path('export_to_pdf/', export_to_pdf, name='export_to_pdf'),
    path('viewcase/', ViewCase.as_view(), name='viewcase'),
    path('hdfcapi/', hdfcapi, name='hdfcapi')
    
    ]
