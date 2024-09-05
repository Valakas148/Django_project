from django.urls import path

from apps.employees_dealership.views import DealershipEmployeeDetailView, DealershipEmployeeListCreateView

urlpatterns = [
    path('', DealershipEmployeeListCreateView.as_view()),
    path('/<int:pk>', DealershipEmployeeDetailView.as_view()),
]

