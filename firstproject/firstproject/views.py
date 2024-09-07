from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("hello world,you are now at the home page oif the django page contact")
    return render(request,'website/main.html')
