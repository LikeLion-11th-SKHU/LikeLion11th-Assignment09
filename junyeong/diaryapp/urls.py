from django.contrib import admin
from django.urls import path
import diaryapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new/', diaryapp.views.new, name='new'),
    path('diary/', diaryapp.views.diary, name='diary'),
    path('new/create/', diaryapp.views.create, name='create'),
    path('detail/<str:diary_id>/', diaryapp.views.detail, name='detail'),
    path('edit/<str:diary_id>/', diaryapp.views.edit, name='edit'),
    path('delete/<str:diary_id>/', diaryapp.views.delete, name='delete'),
    path('update/<str:diary_id>/', diaryapp.views.update, name='update'),
]
    