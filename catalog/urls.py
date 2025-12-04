from django.urls import path
from . import views

urlpatterns = [
    path("", views.NoteList.as_view(), name="note_list"),
    path("details/<int:pk>/", views.NoteDetails.as_view(), name="note_details"),
    path("comment/create", views.create_comment, name="create_comment"),
]
