from django.contrib.auth.models import User
from django.db import models


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)

    # date_modified = models.DateField()

    def __str__(self):
        return f'{self.author} ({self.date} {self.time})'


class Image(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images', max_length=255)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    # date_modified = models.DateField()
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f'{self.author} ({self.date} {self.time})'
