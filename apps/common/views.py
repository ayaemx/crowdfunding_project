from django.shortcuts import render
from django.http import HttpResponse

def common_home(request):
    return HttpResponse("Common Utilities Home Page")
