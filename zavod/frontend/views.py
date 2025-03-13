from django.shortcuts import render, redirect
from django.contrib import messages
import requests
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

import asyncio
from asgiref.sync import sync_to_async
import json
from django.http import JsonResponse, StreamingHttpResponse


def home(request):
    user_likes = []
    user_id = None
    url = 'http://127.0.0.1:8000/api/news/'
    
    response = requests.get(url)
    response.raise_for_status()
    
    if request.user.is_authenticated:
        user_url = f'http://127.0.0.1:8000/api/users/{request.user.id}/'
        
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user_likes = user_response.json().get("likes", [])
        user_id = user_response.json()['id']
    
    context = {
        'news' : response.json(),
        'name':'home',
        'user': request.user.is_authenticated,
        'user_likes':user_likes,
        'user_id': user_id
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

@csrf_exempt
def like(request):
    if request.method == "POST" and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            news_id = request.POST.get('news_id')
            user_id = request.POST.get('user_id')
            
            url = f'http://127.0.0.1:8000/api/news/{news_id}/'
    
            response = requests.get(url)
            response.raise_for_status()
            news_likes = response.json()['likes']
            
            payload = {
                    "id": news_id,
                    "likes": news_likes+1,
                }
            
            news_edit_likes = requests.patch(url, json=payload)
            news_edit_likes.raise_for_status()
            
            user_url = f'http://127.0.0.1:8000/api/users/{user_id}/'
            
            user_response = requests.get(user_url)
            user_response.raise_for_status()
            
            user_data = user_response.json()
            user_likes = user_data['likes']
            
            if news_id not in user_likes:
                user_likes.append(news_id)
            
            payload = {
                    "likes": user_likes
                }
            
            user_edit_likes = requests.patch(user_url, json=payload)
            user_edit_likes.raise_for_status()
            
            return JsonResponse({"success": True, "message": "Form submitted successfully!"})
        
    return render(request, 'home.html')

@csrf_exempt
def unlike(request):
    if request.method == "POST" and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            news_id = request.POST.get('news_id')
            user_id = request.POST.get('user_id')
            
            url = f'http://127.0.0.1:8000/api/news/{news_id}/'
    
            response = requests.get(url)
            response.raise_for_status()
            news_likes = response.json()['likes']
            
            payload = {
                    "id": news_id,
                    "likes": news_likes-1,
                }
            
            news_edit_likes = requests.patch(url, json=payload)
            news_edit_likes.raise_for_status()
            
            user_url = f'http://127.0.0.1:8000/api/users/{user_id}/'
            
            user_response = requests.get(user_url)
            user_response.raise_for_status()
            
            user_data = user_response.json()
            user_likes = user_data['likes']
            
            user_likes.remove(int(news_id))
            
            payload = {
                    "likes": user_likes
                }
            
            user_edit_likes = requests.patch(user_url, json=payload)
            user_edit_likes.raise_for_status()
            
            return JsonResponse({"success": True, "message": "Form submitted successfully!"})
        
    return render(request, 'home.html')

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
        messages.success(request, 'You have successfully logged in')
        return redirect('home')
    redirect ('home')

def sign_out(request):
    logout(request)
    return redirect('home')


url = "http://127.0.0.1:8000/api/news/"
likes_cache = {}
@csrf_exempt
async def likes_stream(request):
    async def event_stream():
        global likes_cache

        while True:
            response = await sync_to_async(requests.get)(url)
            news_likes = response.json()

            updates = []
            for news in news_likes:
                news_id = news["id"]
                likes_count = news["likes"]

                if likes_cache.get(news_id) != likes_count:
                    likes_cache[news_id] = likes_count
                    updates.append({"news_id": news_id, "likes": likes_count})

            if updates:
                yield f"data: {json.dumps(updates)}\n\n"

            await asyncio.sleep(1)

    return StreamingHttpResponse(event_stream(), content_type="text/event-stream")