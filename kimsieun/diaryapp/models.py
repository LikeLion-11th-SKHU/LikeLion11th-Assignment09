from django.db import models

# Create your models here.
class DiaryNotForm(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    weather = models.CharField(max_length=20)
    pub_date = models.DateTimeField('data published')
    image = models.ImageField(upload_to='phto/', blank=True)
    
    def __int__(self):
        return self.content
    