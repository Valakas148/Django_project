from django.urls import path

from apps.cardealership.views import CarDealershipListCreateView, CarDealershipDetailView

urlpatterns = [
    path('', CarDealershipListCreateView.as_view()),
    path('/<int:pk>', CarDealershipDetailView.as_view()),
]
