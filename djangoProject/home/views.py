from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request,"index.html")

def success_page(request):
    print("*" * 10) 
    return HttpResponse("he this is a success page") 