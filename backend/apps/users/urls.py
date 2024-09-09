from django.urls import path

from apps.users.views import (
    UserBlockView,
    UserListCreateView,
    UserRetrieveView,
    UserToAdminView,
    UserToManagerView,
    UserUnBlockView,
    UserUpdateDestroyView,
)

urlpatterns = [
    path('', UserListCreateView.as_view()),
    path('/<int:pk>', UserRetrieveView.as_view()),
    path('/updel/<int:pk>', UserUpdateDestroyView.as_view()),
    path('/<int:pk>/block', UserBlockView.as_view()),
    path('/<int:pk>/unblock', UserUnBlockView.as_view()),
    path('/<int:pk>/admins', UserToAdminView.as_view()),
    path('/<int:pk>/managers', UserToManagerView.as_view())
]

