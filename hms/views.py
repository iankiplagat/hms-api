from django.shortcuts import render
from .models import *
from datetime import datetime,timedelta,date
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
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
    
    
class LoginUser(APIView):
    serializer_class=LoginSerializer
    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)

        # login user
    def post(self, request, format=None):
        serializers=self.serializer_class(data=request.data)
        if serializers.is_valid():
            serializers.save()
            users=serializers.data

            response={
                "data":{
                    "user":dict(users),
                    "status":"Success",
                    "message":"User logged in successfully"
                }
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)    


class SingleDoctorList(APIView):
  def get(self,request, pk, format=None):
    doctor= Doctor.objects.get(pk=pk)
    serializers=DoctorSerializer(doctor)
    return Response(serializers.data)


class DoctorSearchList(APIView):
  def get(self,request,name):
    doctor=Doctor.find_doctor(name)
    serializers=DoctorSerializer(doctor, many=True)
    return Response(serializers.data)


class DoctorList(APIView):
  def get_doctor(self, pk):
    try:
        return Doctor.objects.get(pk=pk)
    except Doctor.DoesNotExist:
        return Http404()

  def get(self,request,format=None):
    doctor= Doctor.objects.all()
    serializers=DoctorSerializer(doctor, many=True)
    return Response(serializers.data)

  def put(self, request, pk, format=None):
    doctor = self.get_doctor(pk)
    serializers = DoctorSerializer(doctor, request.data)
    if serializers.is_valid():
      serializers.save()
      doctor=serializers.data
      response = {
          'data': {
              'doctor': dict(doctor),
              'status': 'success',
              'message': 'Doctor updated successfully',
          }
      }
      return Response(response)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    doctor = self.get_doctor(pk)
    doctor.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class SinglePatientList(APIView):
  def get(self,request, pk, format=None):
    patient= Patient.objects.get(pk=pk)
    serializers=PatientSerializer(patient)
    return Response(serializers.data)


class PatientSearchList(APIView):
  def get(self,request,name):
    patient=Patient.find_patient(name)
    serializers=DoctorSerializer(patient, many=True)
    return Response(serializers.data)


class PatientList(APIView):
  def get_patient(self, pk):
    try:
        return Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return Http404()

  def get(self,request,format=None):
    patient= Patient.objects.all()
    serializers=PatientSerializer(patient, many=True)
    return Response(serializers.data)

  def put(self, request, pk, format=None):
    patient = self.get_patient(pk)
    serializers = PatientSerializer(patient, request.data)
    if serializers.is_valid():
      serializers.save()
      patient=serializers.data
      response = {
          'data': {
              'patient': dict(patient),
              'status': 'success',
              'message': 'Patient updated successfully',
          }
      }
      return Response(response)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    patient = self.get_patient(pk)
    patient.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class SingleAppointmentList(APIView):
  def get(self,request, pk, format=None):
    appointment= Appointment.objects.get(pk=pk)
    serializers=AppointmentSerializer(appointment)
    return Response(serializers.data)


class ApptSearchList(APIView):
  def get(self,request,patientName):
    appointment=Appointment.find_appointment(patientName)
    serializers=AppointmentSerializer(appointment, many=True)
    return Response(serializers.data)


class PatientList(APIView):
  def get_patient(self, pk):
    try:
        return Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return Http404()

  def get(self,request,format=None):
    patient= Patient.objects.all()
    serializers=PatientSerializer(patient, many=True)
    return Response(serializers.data)

  def put(self, request, pk, format=None):
    patient = self.get_patient(pk)
    serializers = PatientSerializer(patient, request.data)
    if serializers.is_valid():
      serializers.save()
      patient=serializers.data
      response = {
          'data': {
              'patient': dict(patient),
              'status': 'success',
              'message': 'Patient updated successfully',
          }
      }
      return Response(response)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    patient = self.get_patient(pk)
    patient.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
