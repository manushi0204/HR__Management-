from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Performance
from .serializers import PerformanceSerializer

# Create your views here.
@api_view(['POST'])
def create_performance(request):
    serializer = PerformanceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_performance(request):
    performances = Performance.objects.all()
    serializer = PerformanceSerializer(performances, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def performance_detail(request, id):
    performance = get_object_or_404(Performance, id=id)

    if request.method == 'GET':
        serializer = PerformanceSerializer(performance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PerformanceSerializer(performance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        performance.delete()
        return Response(
            {"message": "Performance review deleted"},
            status=status.HTTP_204_NO_CONTENT
        )
