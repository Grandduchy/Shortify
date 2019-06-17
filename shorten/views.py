from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Shortify home page")

def url(request, shortenUrl):
    return HttpResponse("At url %s" % shortenUrl)
