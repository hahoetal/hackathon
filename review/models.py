from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Userreview(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'images/')
    title = models.CharField(max_length = 100)
    menu = models.CharField(max_length = 200)
    body = models.TextField()

    def summary(self):
        return self.body[:50]