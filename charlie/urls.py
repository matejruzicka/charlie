"""charlie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from website import views
from website_en import views as views_en

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('gallery/', views.gallery, name="gallery"),
    path('magazine/', views.magazine, name="magazine"),
    path('downloads/download/<str:slug>', views.download_file, name="download_file"),
    path('downloads/view/<str:slug>', views.view_file, name="view_file"),
]

urlpatterns_en = [
    path('en', views_en.home_en, name="home_en"),
    path('en/about/', views_en.about_en, name="about_en"),
]

urlpatterns += urlpatterns_en
