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
  
  
class SingleUserList(APIView):
  def get(self,request, pk, format=None):
    user= User.objects.get(pk=pk)
    serializers=RegistrationSerializer(user)
    return Response(serializers.data)    


class UserSearchList(APIView):
  def get(self,request,username):
    user=User.find_user(username)
    serializers=RegistrationSerializer(user, many=True)
    return Response(serializers.data)


class UserList(APIView):
  def get_users(self,pk):
    try:
        return User.objects.get(pk=pk)
    except User.DoesNotExist:
        raise Http404()

  def get(self,request,format=None):
    users=User.objects.all()
    serializers=RegistrationSerializer(users, many=True)
    return Response(serializers.data)

  def put(self, request, pk, format=None):
    user = self.get_users(pk)
    serializers = UserSearchList(user, request.data)
    if serializers.is_valid():
      serializers.save()
      user=serializers.data
      response = {
          'data': {
              'user': dict(user),
              'status': 'success',
              'message': 'User updated successfully',
          }
      }
      return Response(response)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


  def delete(self, request, pk, format=None):
    user = self.get_users(pk)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
    
    
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
  def get_doctor(self, name):
    try:
        return Doctor.objects.get(name=name)
    except Doctor.DoesNotExist:
        return Http404()

  def get(self,request,format=None):
    doctor= Doctor.objects.all()
    serializers=DoctorSerializer(doctor, many=True)
    return Response(serializers.data)

  def put(self, request, name, format=None):
    doctor = self.get_doctor(name)
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
    serializers=PatientSerializer(patient, many=True)
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

  def post(self, request, format=None):
    serializers=PatientSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      patient=serializers.data
      
      response={
        'data':{
          'users':dict(patient),
          'status':'success',
          'message':'Patient created successfully',
        }
      }
      return Response(response, status=status.HTTP_200_OK)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

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


class AppointmentList(APIView):
  def get_appointment(self, pk):
    try:
        return Appointment.objects.get(pk=pk)
    except Appointment.DoesNotExist:
        return Http404()

  def get(self,request,format=None):
    appointment= Appointment.objects.all()
    serializers=AppointmentSerializer(appointment, many=True)
    return Response(serializers.data)

  def put(self, request, pk, format=None):
    appointment = self.get_appointment(pk)
    serializers = AppointmentSerializer(Appointment, request.data)
    if serializers.is_valid():
      serializers.save()
      appointment=serializers.data
      response = {
          'data': {
              'appointment': dict(appointment),
              'status': 'success',
              'message': 'Appointment updated successfully',
          }
      }
      return Response(response)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    appointment = self.get_appointment(pk)
    appointment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
