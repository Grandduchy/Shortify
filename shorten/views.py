from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
# Create your views here.

def index(request):
    return render(request, "shorten/index.html")


from .models import Url

def url(request, shortedUrl):
    redirectUrl = get_object_or_404(Url, shortenUrl=shortedUrl)
    return HttpResponseRedirect(redirectUrl.url)


# RESTful API for using the database with javascript
# Would be better for it to a new view than this one

host = "http://127.0.0.1:8000"


from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
import random

def get(request):
    print(request.GET)
    return HttpResponse()

@csrf_exempt
def post(request):

    response = {
        "success" : False,
        "url" : "",
        "message" : "",
    }
    
    if not request.method == "POST":
        response["message"] = "This endpoint only supports POST requests"
        return JsonResponse(response)


    # Correct Format
    postDict = request.POST
    if len(postDict) is not 1 or not "url" in postDict:
        response["message"] = "Invalid format of data; expected one key \'url\'"
        return JsonResponse(response)
    
    # Is valid Url
    try:
        validate = URLValidator()
        validate(postDict["url"])
    except (ValueError, ValidationError) as err:
        response["message"] = "Url validation failure, url does not exist or is not valid"
        return JsonResponse(response)
    
    response["success"] = True

    # Check if the url exists, if so don't create a new one, return the already existing
    existingSet = Url.objects.filter(url=postDict["url"])
    if len(existingSet) is not 0:
        response["url"] = host + "/url/" + existingSet.first().shortenUrl
        return JsonResponse(response)

    # Create a new one
    i = 0;
    for power in range(1,50): # Database can handle numbers up to 10^50
        i = random.randint(1, 10**power)
        numOfI = Url.objects.filter(shortenUrl = i).count()
        if numOfI == 0:
            break
    newUrl = host + "/url/" + str(i)
    urlScheme = Url.objects.create(url=postDict["url"], shortenUrl=i) # do not consider local host to the database!
    response["url"] = newUrl
    print(newUrl)
    return JsonResponse(response)

def delete(request):
    pass
