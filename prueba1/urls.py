from django.urls import re_path
from  . import views

urlpatterns = [
    #re_path(r'^$', views.muestra_datos, name= 'prueba1'),
    re_path(r'^$', views.inicio, name= 'inicio'),
    re_path(r'^registros/', views.muestra_datos, name= 'registros'),
    re_path(r'^knn/', views.algknn, name= 'knn'),
    re_path(r'^ingenuo/', views.ingenuo, name= 'ingenuo'),
    re_path(r'^logistica/', views.logistica, name= 'logistica'),
    re_path(r'^regresion/', views.regresion, name = 'regresion'),
    
]