from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import ObtainAuthToken


urlpatterns=[
  # Authentication
  path('register/', views.Registration.as_view(), name="register"),
  path('login/', views.LoginUser.as_view(), name="login"),
  path('authlogin/', ObtainAuthToken.as_view(), name="authlogin"),
  
  # Doctor
  path('doctor/',views.DoctorList.as_view(),name='doctor'),
  path('doctor/<name>',views.DoctorSearchList.as_view(), name='doctor_search'),
  path('doctor/<int:pk>/',views.SingleDoctorList.as_view(),name='single_doctor'),
  path('doctor/update/<int:pk>/',views.DoctorList.as_view(),name='update_doctor_profile'),
  path('doctor/delete/<int:pk>/',views.DoctorList.as_view(),name='delete_doctor'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)