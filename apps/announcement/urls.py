from django.urls import path

from apps.announcement.views import AnnouncementCreateListView, AnnouncementViewUpdateDelete

urlpatterns = [
    path('', AnnouncementCreateListView.as_view()),
    path('/<int:pk>', AnnouncementViewUpdateDelete.as_view())
]