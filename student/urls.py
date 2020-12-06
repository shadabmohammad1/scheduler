
from django.conf.urls import url, include

from rest_framework_simplejwt import views as jwt_views

from student.views import LoginView

urlpatterns = [
    url(r'^login/', jwt_views.TokenObtainPairView.as_view()),
]
