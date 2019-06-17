from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def index(request):
    return HttpResponse("Shortify home page")


from .models import Url

def url(request, shortedUrl):
    redirectUrl = get_object_or_404(Url, shortenUrl=shortedUrl)
    return HttpResponseRedirect(redirectUrl.url)
