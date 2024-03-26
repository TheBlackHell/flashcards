from django.urls import path
from . import views

# URLConfig
urlpatterns = [
    path("", views.main),
    path("edit/", views.edit_flashcardset),
    path("create/", views.create_flashcardset),
    path("create/<str:id>", views.create_flashcards),
    path("create/<str:id>/del", views.delete_flashcardset),
    path("create/<str:id>/flashcards", views.view_flashcards),
    path("create/<str:id>/flashcards/del=<str:del_id>", views.delete_flashcards),

    path("select/<str:id>", views.select_flashcardset),
    path("select/<str:id>/learn/<str:type>", views.learn),
]