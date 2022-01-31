
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

from .models import Receipe

@api_view(['GET'])
def apiOverview(request):
    api_urls={
        'List':'receipe-list',
        'Detail View':'/receipe-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>',
        'Delete':'/task-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def receipeList(request):
    receipe = Receipe.objects.all().order_by('_id')
    serializer = TaskSerializer(receipe,many=True)
    return Response(serializer)