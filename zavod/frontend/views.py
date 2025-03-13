from django.shortcuts import render, redirect
from django.contrib import messages
import requests
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout

def home(request):
    url = 'http://127.0.0.1:8000/api/news/'
    
    response = requests.get(url)
    response.raise_for_status()
    
    context = {
        'news' : response.json(),
        'name':'home',
        'user': request.user.is_authenticated,
        'user_like':request.user
    }
    
    return render(request, 'home.html', context)

def tagged(request):
    url = 'http://127.0.0.1:8000/api/news/'
    
    response = requests.get(url)
    response.raise_for_status()
    
    context = {
        'news' : response.json(),
        'name':'home',
        'user': request.user.is_authenticated,
        'user_like':request.user
    }
    
    print (context)
    
    return render(request, 'tagged.html', context)

def news(request, id):
    url = f'http://127.0.0.1:8000/api/news/{id}/'
    
    response = requests.get(url)
    response.raise_for_status()
    views = response.json()['views']
    
    payload = {
            "id": id,
            "views": views+1,
        }
    
    edit_view = requests.patch(url, json=payload)
    edit_view.raise_for_status()
    
    new_response = requests.get(url)
    new_response.raise_for_status()
    
    context = {
        'news' : new_response.json(),
        'name': new_response.json()['title'],
        'user': request.user.is_authenticated
    }
    
    return render(request, 'news.html', context)

def delete(request, id):
    url = f'http://127.0.0.1:8000/api/news/{id}/'
    
    response = requests.delete(url)
    response.raise_for_status()
    
    context = {
        'name':'home',
        'user': request.user.is_authenticated
    }
    
    return render(request, 'home.html', context)

def sign_in(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        return redirect('home')

def sign_out(request):
    logout(request)
    return redirect('home')