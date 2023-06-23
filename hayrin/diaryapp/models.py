from django.db import models

class DiaryNotForm(models.Model):
    title = models.CharField(max_length=30) 
    pub_date = models.DateTimeField('data published')
    weather = models.CharField(max_length=20) 
    content = models.TextField() 
    file = models.FileField(upload_to='phto/', blank=True) 

    def __int__(self):
        return self.title
    
# Create your models here.
