from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
# ex: /polls/5/
    path("<int:session_id>/", views.detail_session, name="detail"),
    # ex: /polls/5/results/
    path("<int:recurso_id>/results/", views.results_sessions, name="results"),
    # ex: /polls/5/vote/
    path("<int:recurso_id>/recurso/", views.recurso, name="recurso")
]