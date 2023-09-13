from django.urls import path
from autenticazione import views
from django.http import  HttpResponse

urlpatterns = [
    path('acceuil', views.acceuil, name='acceuil'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name='logout')
]
