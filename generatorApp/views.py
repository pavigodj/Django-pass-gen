from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generatorApp/home.html')

def password(request):
    my_pass = ''
    char_lst = list(('abcdefghijklmnopqrstuvwxyz'))
    leng = int(request.GET.get("length",18))

    if request.GET.get("uppercase"):
        char_lst.extend(list('ABCDEFGHILJKMNOPQRSTUVWXYZ'))

    if request.GET.get("numbers"):
        char_lst.extend(list('0123456789'))
    
    if request.GET.get("special"):
        char_lst.extend(list('!@#$%^&*()_+~?'))
    
    for i in range(leng):
        my_pass+= random.choice(char_lst)

    return render(request, 'generatorApp/password.html', {"password":my_pass} )

def about(request):
    return render(request, 'generatorApp/about.html')
