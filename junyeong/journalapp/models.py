from django.db import models

# Create your models here.

class Journal(models.Model):
    title = models.CharField(max_length=30)
    pub_date = models.DateTimeField('date published')
    weather = models.CharField(max_length=20)
    body = models.TextField()
    image = models.ImageField(upload_to='photo/', blank=True)

    def __str__(self):
        return self.title
    
