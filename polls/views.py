from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Roshan! You are at the Polls index")