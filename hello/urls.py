from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HelloWorldViewSet

router = DefaultRouter()
router.register(r'helloworld', HelloWorldViewSet, basename='helloworld')

urlpatterns = [
    path('api/', include(router.urls)),
]
