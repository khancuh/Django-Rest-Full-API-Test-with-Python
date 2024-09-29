from django.shortcuts import render

# Create your views here.
# pdfs/views.py
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .models import PDFUpload
from .serializers import PDFUploadSerializer

class PDFUploadViewSet(viewsets.ModelViewSet):
    queryset = PDFUpload.objects.all()
    serializer_class = PDFUploadSerializer
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
