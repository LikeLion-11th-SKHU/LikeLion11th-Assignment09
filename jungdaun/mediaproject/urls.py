"""
URL configuration for mediaproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls import include
import mainapp.views
from django.conf import settings
from django.conf.urls.static import static
from diaryapp import views as diaryapp_views
from journalapp import views as journalapp_views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', mainapp.views.index, name='index'),
    
    path('diary/', include('diaryapp.urls')),
    path('journal/', include('journalapp.urls')),
    
    path('edit/<str:id>/', diaryapp_views.edit, name='edit'),
    path('update/<str:id>/', diaryapp_views.update, name='update'),
    path('delete/<str:id>/', diaryapp_views.delete, name='delete'),
    
    path('edit/<str:id>/', journalapp_views.edit, name='edit'),
    path('update/<str:id>/', journalapp_views.update, name='update'),
    path('delete/<str:id>/', journalapp_views.delete, name='delete'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
