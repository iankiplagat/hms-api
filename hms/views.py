from django.shortcuts import render
from .models import *
from datetime import datetime,timedelta,date
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from django.http import response
from .serializers import *

class Registration(APIView):
  serializer_class=RegistrationSerializer

  def post(self, request):
      serializer=self.serializer_class(data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()

      user=serializer.data

      response={
          "data":{
              "user":dict(user),
              "status":"Success",
              "message":"User account created successfully"
          }

      }
      return Response(response, status=status.HTTP_201_CREATED)
