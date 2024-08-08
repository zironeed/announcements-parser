from django.urls import path
from announcement_app.views import AnnouncementListView, AnnouncementDetailView, AnnouncementParseView
from announcement_app.apps import AnnouncementAppConfig


app_name = AnnouncementAppConfig.name


urlpatterns = [
    path('get/', AnnouncementListView.as_view(), name='list_view'),
    path('get/<int:pk>/', AnnouncementDetailView.as_view(), name='detail_view'),
    path('parse/', AnnouncementParseView.as_view(), name='parse_view'),
]