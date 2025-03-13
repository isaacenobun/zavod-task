from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tagged/', views.tagged, name='tagged'),
    path('news/<int:id>', views.news, name='news'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('sign-in', views.sign_in, name='sign-in'),
    path('sign-out', views.sign_out, name='sign-out'),
]