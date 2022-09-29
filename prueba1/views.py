from django.shortcuts import render
from .models import Prueba1
# Create your views here.
 
def muestra_datos(request):
    consulta = Prueba1.objects.all()
    dic = {'valor': consulta} 
    sumas = []
    for i in consulta:
        suma = 0
        suma = i.dato1 + i.dato3 + i.dato4
        sumas.append(suma)
    dic["sumas"] = sumas


    

    return render(request, 'Prueba1/indext.html', dic)
