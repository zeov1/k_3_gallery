from django.contrib.auth.models import User
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


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
    thumbnail = ImageSpecField(source='img',
                               processors=[ResizeToFill(200, 200)],
                               format='JPEG',
                               options={'quality': 60})
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f'{self.author} ({self.date} | {self.time.hour}:{self.time.minute}:{self.time.second})'
