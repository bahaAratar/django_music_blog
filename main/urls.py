"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from music.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', get_hello),
    path('music/', get_music),
    path('music/create/', post_music),
    path('music/delete/<str:title>/', delete_music),
    path('music/search/<int:id>/', get_song),
    path('music/search/<str:title>/', get_title),
    path('music/update/<int:pk>/', update_music),

    path('music/class/', MusicView.as_view()),

    
]
