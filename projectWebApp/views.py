from django.shortcuts import render, HttpResponse
from services.models import Servicio

# Create your views here.
def home(request):
    return render(request, "projectWebApp/home.html")