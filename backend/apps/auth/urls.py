from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.auth.views import SocketView

urlpatterns = [
    path('', TokenObtainPairView.as_view()),
    path('/refresh/', TokenRefreshView.as_view()),
    path('/token', SocketView.as_view())
]

