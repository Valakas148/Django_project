from django.shortcuts import render

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from djangochannelsrestframework.permissions import IsAuthenticated

# Create your views here.

#
# class ActivateUserView(GenericAPIView):
#     permission_classes = (AllowAny,)
