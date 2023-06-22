from django.db import models
from django.utils import timezone

# Create your models here.

class Diarynotform(models.Model):
    title = models.CharField(max_length=30)
    pub_date = models.DateTimeField('date published')
    weather = models.CharField(max_length=20)
    body = models.TextField()
    image = models.ImageField(upload_to='photo/', blank=True)

    def __int__(self):
        return self.title
