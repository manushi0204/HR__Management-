from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Training
from .serializers import TrainingSerializer

@api_view(['POST'])
def create_training(request):
    serializer = TrainingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_trainings(request):
    trainings = Training.objects.all()
    serializer = TrainingSerializer(trainings, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def training_detail(request, id):
    training = get_object_or_404(Training, id=id)

    if request.method == 'GET':
        serializer = TrainingSerializer(training)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TrainingSerializer(training, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        training.delete()
        return Response(
            {"message": "Training deleted"},
            status=status.HTTP_204_NO_CONTENT
        )
