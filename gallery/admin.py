from django.contrib import admin
from django.utils.safestring import mark_safe

from gallery.models import Comment, Image

# Register your models here.

# admin.site.register(Person)
admin.site.register(Comment)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.img.url}" style="max-height: 200px;">')
