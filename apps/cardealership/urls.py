from django.urls import path

from apps.cardealership.views import CarDealershipDetailView, CarDealershipListCreateView

urlpatterns = [
    path('', CarDealershipListCreateView.as_view()),
    path('/<int:pk>', CarDealershipDetailView.as_view()),
]
