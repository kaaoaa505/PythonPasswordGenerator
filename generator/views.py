from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    data = {'password': 'lkajsdf;lkajdsflkj'}
    return render(request, 'generator/home.html', data)

def about(request):
    return render(request, 'generator/about.html')

def test(request):
    return HttpResponse('<h1>just for test.</h1>')

def password(request):
    characters = list('abcdefghigklmnopqrstuvwxyz')
    length = request.GET.get('length')
    length = int(length)

    if(request.GET.get('uppercase') == 'on'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    if(request.GET.get('numbers') == 'on'):
        characters.extend('1234567890')

    if(request.GET.get('special') == 'on'):
        characters.extend('!@#$%^&*()')

    result = ''

    for _ in range(length):
        result += random.choice(characters)

    return render(request, 'generator/password.html', {'password': result})