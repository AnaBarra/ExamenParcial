from django.urls import path
from  . import views

urlpatterns = [
    path('prueba1/', views.muestra_datos, name= 'prueba1'),
    
]