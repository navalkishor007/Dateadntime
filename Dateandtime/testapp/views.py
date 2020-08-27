from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def DateTimeView(request):
    dandt = datetime.now()
    view ="<h1>Date and time is {}</h1>".format(dandt)
    return HttpResponse(view)