import base64
from .models import Image
from rest_framework import serializers
from django.core.files.base import ContentFile




class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,') 
            ext = format.split('/')[-1] 
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super().to_internal_value(data)

    def to_representation(self, value):
        return value.url

class ImageSerializer(serializers.ModelSerializer):
    image = Base64ImageField()
    image_url = serializers.SerializerMethodField()
    class Meta():
        model = Image
        fields = ['id', 'image', 'description', 'image_url']
        
    def get_image_url(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(obj.image.url)
        return obj.image.url
