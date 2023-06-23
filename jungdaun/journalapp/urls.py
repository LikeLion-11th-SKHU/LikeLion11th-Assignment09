from django.contrib import admin
from django.urls import path
import journalapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('write/', journalapp.views.write, name = 'write'),
    path('useform/', journalapp.views.useform, name = 'useform'),
    path('detail1/<str:id>/', journalapp.views.detail1, name='detail1'),
    path('update/<str:id>/', journalapp.views.update, name='update'),
    path('delete/<str:id>/', journalapp.views.delete, name='delete'),
] 