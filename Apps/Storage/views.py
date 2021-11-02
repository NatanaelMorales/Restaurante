from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):

    allBebida = Bebidas.objects.all()
    allPostre = Postres.objects.all()
    allExtra = Extras.objects.all()
    return render(request, 'index.html', {'allBebida':allBebida,
                                          'allPostre':allPostre,
                                          'allExtra':allExtra})
def Contact(request):
    return render(request, 'contact.html')

def About(request):
    return render(request, 'about.html')


def Carrito(request):
    return render(request, 'carrito.html')