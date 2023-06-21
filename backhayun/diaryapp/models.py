from django.db import models

# Create your models here.
class DiaryNotForm(models.Model):
    title = models.CharField(max_length=30)
    pub_date = models.DateTimeField('date published')
    weather = models.CharField(max_length=20)
    content = models.TextField()
    file = models.FileField(upload_to='phto/', blank=True)

    def __int__(self):
        return self.title