from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Leave
from .serializers import LeaveSerializer

@api_view(['POST'])
def create_leave(request):
    serializer=LeaveSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_leaves(request):
    leaves = Leave.objects.all()
    serializer = LeaveSerializer(leaves, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
def leave_detail(request, id):
    leave = get_object_or_404(Leave, id=id)

    if request.method == 'GET':
        serializer = LeaveSerializer(leave)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LeaveSerializer(leave, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        leave.delete()
        return Response(
            {"message": "Leave deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
