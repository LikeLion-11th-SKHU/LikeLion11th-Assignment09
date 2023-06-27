
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
import mainapp.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainapp.views.index, name='index'),

    path('',include('diaryapp.urls')),
    path('',include('journalapp.urls')),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)