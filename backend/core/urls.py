
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static




urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/api-auth/', include('API.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
