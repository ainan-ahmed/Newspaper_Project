from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import get_user_model
import readtime
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 150)
    
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='images/',blank=True)
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]
    
    def pub(self ):
        return self.date.strftime('%b %e %Y')
    def year(self):
        return self.date.strftime('%Y')
    def month(self):
        return self.date.strftime('%b')
    def day(self):
        return self.date.strftime('%d')
    def countWords(self):
        return readtime.of_text(self.body)
    def get_absolute_url(self):
        return reverse('article:details',kwargs={'pk':self.id})