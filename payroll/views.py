from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Compensation, Payroll
from .serializers import CompensationSerializer, PayrollSerializer

@api_view(['POST', 'PUT'])
def compensation_create_update(request, employee_id):
    try:
        compensation = Compensation.objects.get(employee_id=employee_id)
    except Compensation.DoesNotExist:
        compensation = None

    if request.method == 'POST':
        serializer = CompensationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        serializer = CompensationSerializer(compensation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_compensation(request, employee_id):
    compensation = get_object_or_404(Compensation, employee_id=employee_id)
    serializer = CompensationSerializer(compensation)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_compensation(request, employee_id):
    compensation = get_object_or_404(Compensation, employee_id=employee_id)
    compensation.delete()
    return Response(
        {"message": "Compensation deleted"},
        status=status.HTTP_204_NO_CONTENT
    )

@api_view(['POST'])
def create_payroll(request):
    serializer = PayrollSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_payrolls(request):
    payrolls = Payroll.objects.all()
    serializer = PayrollSerializer(payrolls, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def payroll_detail(request, id):
    payroll = get_object_or_404(Payroll, id=id)

    if request.method == 'GET':
        serializer = PayrollSerializer(payroll)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PayrollSerializer(payroll, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        payroll.delete()
        return Response(
            {"message": "Payroll deleted"},
            status=status.HTTP_204_NO_CONTENT
        )
