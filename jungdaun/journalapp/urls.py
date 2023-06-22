from django.contrib import admin
from django.urls import path
from journalapp import views as journalapp_views

urlpatterns = [
    path('custom-admin/', admin.site.urls, name='custom-admin'),
    path('write/', journalapp_views.write, name = 'write'),
    path('write/create/', journalapp_views.create, name = 'create'),
    path('useform/', journalapp_views.useform, name = 'useform'),
] 