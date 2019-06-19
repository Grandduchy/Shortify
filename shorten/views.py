from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def index(request):
    return render(request, "shorten/index.html")


from .models import Url

def url(request, shortedUrl):
    redirectUrl = get_object_or_404(Url, shortenUrl=shortedUrl)
    return HttpResponseRedirect(redirectUrl.url)


# RESTful API for using the database with javascript
# Would be better for it to a new view than this one

def get(request):
    print(request.GET)
    return HttpResponse()


def post(request):
    print("POST REQUEST : ")
    print(request.POST)
    return HttpResponse()


def delete(request):
    pass
