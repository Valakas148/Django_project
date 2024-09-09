from django.shortcuts import render

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from djangochannelsrestframework.permissions import IsAuthenticated

from core.services.jwt_service import JWTService, SocketToken

# Create your views here.

#
# class ActivateUserView(GenericAPIView):
#     permission_classes = (AllowAny,)


class SocketView(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, *args, **kwargs):
        token = JWTService.create_token(self.request.user, SocketToken)
        return Response({'token': str(token)}, status=status.HTTP_200_OK)