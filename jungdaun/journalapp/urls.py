from django.contrib import admin
from django.urls import path
import journalapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('write/', journalapp.views.write, name = 'new'),
    path('write/create/', journalapp.views.create, name = 'create'),
    path('useform/', journalapp.views.useform, name = 'useform'),
]