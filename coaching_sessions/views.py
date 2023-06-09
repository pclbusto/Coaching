from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail_session(request, session_id):
    return HttpResponse("Detalle de la sesion %s." % session_id)


def results_sessions(request, recurso_id):
    response = "sesiones realizadas a  %s."
    return HttpResponse(response % recurso_id)


def recurso(request, recurso_id):
    return HttpResponse("You're voting on question %s." % recurso_id)