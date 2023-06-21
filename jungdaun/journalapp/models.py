from django.db import models

# Create your models here.

class JournalUseForm(models.Model):
    title = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    weather = models.CharField(max_length=30)
    content = models.TextField()
    file = models.FileField(upload_to='files/', blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    
    def __str__(self):
        return self.content