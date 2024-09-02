from django.urls import path

from apps.cars.views import CarCreateListView, CarViewUpdateDelete

urlpatterns = [
    path('', CarCreateListView.as_view()),
    path('/<int:pk>', CarViewUpdateDelete.as_view()),
]

