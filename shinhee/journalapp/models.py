from django.db import models

# Create your models here.
class JournalUseForm(models.Model):
    title = models.CharField(max_length=30)
    pub_date = models.DateTimeField('data published')
    weather = models.CharField(max_length=20)
    journal = models.TextField()
    image = models.ImageField(upload_to='picture/', blank=True)

    def __int__(self):
        return self.journal