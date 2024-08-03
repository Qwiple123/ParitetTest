from . import views
from rest_framework.routers import DefaultRouter




router = DefaultRouter()
router.register(r'images', views.ImageViewSet, basename='images')
urlpatterns = router.urls
