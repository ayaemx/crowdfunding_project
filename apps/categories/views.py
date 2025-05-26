from django.shortcuts import render
from django.http import HttpResponse

def category_list(request):
    return HttpResponse("Category List Page")

# Create your views here.
