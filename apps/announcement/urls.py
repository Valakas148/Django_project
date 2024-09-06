from django.urls import path

from apps.announcement.views import AnnouncementCreateListView, AnnouncementViewUpdateDelete, SeeDetailView, \
    AnnouncementDetailView

urlpatterns = [
    path('', AnnouncementCreateListView.as_view()),
    path('/<int:pk>', AnnouncementViewUpdateDelete.as_view()),
    path('/detail/<int:pk>', AnnouncementDetailView.as_view()),
    path('/my-announcements', SeeDetailView.as_view()),
]
