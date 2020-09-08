from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("picks will be here! \n"
                        "pick 1 :\n"
                        "pick 2 :\n")


