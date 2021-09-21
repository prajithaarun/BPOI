from django.shortcuts import render,HttpResponse
from django.conf import settings

def hr(request):
    return HttpResponse("Welcome To my hr Page")
def delete(request):
    return HttpResponse("Welcome to my delete page")



