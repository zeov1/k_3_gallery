from django.contrib import admin

from gallery.models import Comment, Image

# Register your models here.

# admin.site.register(Person)
admin.site.register(Comment)
admin.site.register(Image)
