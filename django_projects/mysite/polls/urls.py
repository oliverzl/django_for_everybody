from django.urls import path

from . import views

# Django Tutorial 3
app_name = "polls"
urlpatterns = [
    # example: /polls/
    path("", views.index, name="index"),
    # example: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # example: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # example: /polls/vote/2
    path("vote/<int:question_id>", views.vote, name="vote"),
    # danger has GET request
    path("danger", views.danger, name="danger"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
