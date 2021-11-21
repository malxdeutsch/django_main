from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
import json

# Create your views here.
def homepage(request):
    with open('data.json') as f:
        data = json.load(f)
    return render(request,'homepage.html', context ={'people':data})

def about(request):
    numbers: range(1:10)
    return render(request,'about.html')

def today (request):
    return HttpResponse(str(datetime.today()))