from django.contrib import admin
from django.urls import path
import journalapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('write/', journalapp.views.write, name = 'write'),
    path('useform/', journalapp.views.useform, name = 'useform'),
    path('detail2/<int:id>/', journalapp.views.detail2, name = 'detail2'),
    path('update/<int:id>/', journalapp.views.update, name = 'update'),
    path('delete/<int:id>/', journalapp.views.delete, name = 'delete'),
]