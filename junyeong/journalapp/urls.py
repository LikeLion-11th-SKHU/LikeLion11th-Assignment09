from django.contrib import admin
from django.urls import path
import journalapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('write/', journalapp.views.write, name='write'),
    path('journal/', journalapp.views.journal, name='journal'),
    path('journal_detail/<int:journal_id>/', journalapp.views.journal_detail, name='journal_detail'),
    path('journal_update/<int:journal_id>/', journalapp.views.journal_update, name='journal_update'),
    path('journal_delete/<int:journal_id>/', journalapp.views.journal_delete, name='journal_delete'),
]
