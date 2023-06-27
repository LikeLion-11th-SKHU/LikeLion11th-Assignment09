from django.db import models

# Create your models here.

class JournalUseForm(models.Model):
    title = models.CharField(max_length=30)
    pub_date = models.DateTimeField('data published')
    weather = models.CharField(max_length=20)
    content = models.TextField()
    file = models.FileField(upload_to='files/', blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    
    def __str__(self):
        return self.useform