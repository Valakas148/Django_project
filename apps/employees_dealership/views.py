from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.employees_dealership.models import DealershipEmployee
from apps.employees_dealership.serializer import DealershipEmployeeSerializer


# Create your views here.


class DealershipEmployeeListCreateView(ListCreateAPIView):
    queryset = DealershipEmployee.objects.all()
    serializer_class = DealershipEmployeeSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save()


class DealershipEmployeeDetailView(RetrieveUpdateDestroyAPIView):
    queryset = DealershipEmployee.objects.all()
    serializer_class = DealershipEmployeeSerializer
    permission_classes = [IsAuthenticated, ]

