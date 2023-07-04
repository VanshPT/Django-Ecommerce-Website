from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'shop/index.html')
def about(request):
    return HttpResponse("page")
def contact(request):
    return HttpResponse("page")
def tracker(request):
    return HttpResponse("Page")
def search(request):
    return HttpResponse("page")
def prodview(request):
    return HttpResponse("page")
def checkout(request):
    return HttpResponse("page")




# Create your views here.
