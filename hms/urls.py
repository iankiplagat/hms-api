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
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)