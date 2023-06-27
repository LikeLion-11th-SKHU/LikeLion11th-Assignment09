from django.contrib import admin
from django.urls import path
import journalapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('write/', journalapp.views.write, name = 'write'),
    path('journal/', journalapp.views.journal, name = 'journal'),
    path('detail2/<int:id>', journalapp.views.detail2, name = 'detail2'),
    path('update2/<int:id>', journalapp.views.update2, name = 'update2'),
    path('delete2/<int:id>', journalapp.views.delete2, name = 'delete2'),
    
]