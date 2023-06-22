from django.contrib import admin
from django.urls import path
from diaryapp import views as diaryapp_views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('new/', diaryapp_views.new, name = 'new'),
    path('new/create/', diaryapp_views.create, name = 'create'),
    path('notform/', diaryapp_views.notform, name='notform'),
]

