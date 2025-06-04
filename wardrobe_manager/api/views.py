from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Main(request):
    return HttpResponse("This is a simple http response")