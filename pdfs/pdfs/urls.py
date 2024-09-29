# pdfs/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PDFUploadViewSet

router = DefaultRouter()
router.register(r'pdfs', PDFUploadViewSet, basename='pdf')

urlpatterns = [
    path('', include(router.urls)),
]
