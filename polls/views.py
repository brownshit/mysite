from django.shortcuts import render

#add part
from django.http import HttpResponse
# Create your views here.

def Index(request):
    #return string type message 
    return HttpResponse("Hello world! You're in the polls index.")