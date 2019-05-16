from django.shortcuts import render, redirect, HttpResponse
from .models import Pedido, Prato

# Create your views here.
def calcularValor(request, id):
    pedido = Pedido.objects.filter(id=id).get()
    #print(dir(pedido))
    pedido.zerar() #zera o acumulador 
    pedido.calcular_prato() #calcula novamente

    return redirect('/admin/pedido/pedido')

# def pagina(request, id):
#     pedido = Pedido.objects.filter(id=id)
#     print(pedido)
#     return render(request, 'calcular_pedido.html')