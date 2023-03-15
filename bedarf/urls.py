from django.urls import path
from .views import BedarfListView, BedarfDeleteView, BedarfCreateView, BedarfInlineView

urlpatterns = [
    path("", BedarfListView.as_view(), name="bedarf"),
    path("<int:pk>/delete/", BedarfDeleteView.as_view(), name="bedarf_delete"),
    path("create/", BedarfCreateView.as_view(), name="bedarf_create"),
    path("<int:pk>/details", BedarfInlineView.as_view(), name="bedarf_details"),
]
