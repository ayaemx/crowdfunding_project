from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Homepage")

# Create your views here.
