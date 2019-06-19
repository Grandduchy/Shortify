from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
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

@csrf_exempt
def post(request):
    print(request.POST)
    return HttpResponse("http:///.....")


def delete(request):
    pass
