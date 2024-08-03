from rest_framework import viewsets
from .models import Image
from .serializer import ImageSerializer



class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()

    