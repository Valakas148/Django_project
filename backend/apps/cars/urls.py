from django.urls import path

from apps.cars.views import CarBrandCreateListView, CarBrandViewUpdateDelete, CarCreateListView, CarViewUpdateDelete

urlpatterns = [
    path('/brands', CarBrandCreateListView.as_view()),
    path('/brands/<int:pk>', CarBrandViewUpdateDelete.as_view()),
    path('/models', CarCreateListView.as_view()),
    path('/models/<int:pk>', CarViewUpdateDelete.as_view()),
]

