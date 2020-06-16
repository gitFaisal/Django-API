from django.shortcuts import render
from rest_framework import viewsets
from .models import VisitorsTable
from .serializers import VisitorSerializer


class VisitView(viewsets.ModelViewSet):
    queryset = VisitorsTable.objects.all()
    serializer_class = VisitorSerializer

# def Index(request):
#     return render(request, 'index.html')
