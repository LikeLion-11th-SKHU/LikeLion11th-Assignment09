from django.db import models

# Create your models here.
class ReviewUseForm(models.Model):
    title = models.CharField(max_length=30)
    pub_date = models.DateTimeField('data published')
    weather = models.CharField(max_length=20)
    content = models.TextField()
    picture = models.ImageField(upload_to='picture/', blank=True)

    def __int__(self):
        return self.title
