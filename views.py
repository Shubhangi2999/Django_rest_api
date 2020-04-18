from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework import status
import csv

from .models import Partner
from .serializers import *

@api_view(['GET', 'POST'])
def partners_list(request):
    if request.method == 'GET':
        data = Partner.objects.all()
        with open('training.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for partner in data:
                writer.writerow([partner.id,partner.f_name,partner.l_name,partner.email,partner.contact,partner.age])
        serializer = PartnerSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PartnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            list = Partner.objects.all()
            with open('training.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                for partner in list:
                    writer.writerow([partner.id, partner.f_name, partner.l_name, partner.email, partner.contact, partner.age])
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def partners_detail(request, pk):
    try:
        partner = Partner.objects.get(pk=pk)
    except Partner.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PartnerSerializer(partner, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        partner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
