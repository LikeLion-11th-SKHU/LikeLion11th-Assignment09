from django.db import models
from typing import Any

class DiaryNotForm(models.Model):
    title = models.CharField(max_length=30)
    pub_date = models.DateField('data published')
    weather = models.CharField(max_length=20)
    diary = models.TextField()
    image = models.FileField(upload_to ='media/photo/', blank=True)

    def __int__(self):
        return self.diary
    
