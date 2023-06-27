from django.contrib import admin
from django.urls import path
import journalapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('write/',journalapp.views.write, name='write'),
    path('useform/',journalapp.views.useform, name= 'useform'),
    path('detail2/<str:id>/',journalapp.views.detail02, name='detail2'),

    #UD
    path('update2/<str:id>/',journalapp.views.update02, name='update2'),
    path('delete2/<str:id>/',journalapp.views.delete02, name='delete2'),
]