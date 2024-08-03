from .models import Image
from django.contrib import admin
from django.utils.safestring import mark_safe




@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_tag', 'description')
    readonly_fields = ["image_tag"]
    
    def image_tag(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="400" height="300" />')
