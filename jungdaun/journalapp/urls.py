from django.contrib import admin
from django.urls import path
import journalapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('write/', journalapp.views.write, name = 'write'),
    path('useform/', journalapp.views.useform, name = 'useform'),
    path('detail1/<str:id>/', journalapp.views.detail1, name='detail1'),
    path('update1/<str:id>/', journalapp.views.update1, name='update1'),
    path('delete1/<str:id>/', journalapp.views.delete1, name='delete1'),
] 