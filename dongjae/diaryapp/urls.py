from django.contrib import admin
from django.urls import path
import diaryapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new/', diaryapp.views.new, name='new'),
    path('new/create/', diaryapp.views.create, name='create'),
    path('diary/', diaryapp.views.diary, name='diary'),
    path('detail/<int:id>/', diaryapp.views.detail, name='detail'),

    path('edit/<int:id>/', diaryapp.views.edit, name='edit'),
    path('update/<int:id>/', diaryapp.views.update, name='update'),
    path('delete/<int:id>/', diaryapp.views.delete, name='delete')
]
