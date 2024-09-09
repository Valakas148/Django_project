from django.urls import path

from apps.announcement.views import (
    AnnouncementCreateListView,
    AnnouncementDetailView,
    AnnouncementViewDelete,
    AnnouncementViewUpdateDelete,
    SeeDetailView,
)

urlpatterns = [
    path('', AnnouncementCreateListView.as_view()),
    path('/<int:pk>', AnnouncementViewUpdateDelete.as_view()),
    path('/detail/<int:pk>', AnnouncementDetailView.as_view()),
    path('/my-announcements', SeeDetailView.as_view()),
    path('/delete/<int:pk>', AnnouncementViewDelete.as_view()),
]
