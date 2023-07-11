from django.shortcuts import render
from .models import Product,Contact
from math import ceil

# Create your views here.
from django.http import HttpResponse

def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))

    allProds = []
    catprods = Product.objects.values('category', 'id')
    # print(catprods)
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        # print(prod)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method=="POST":
        print(request)
    name=request.POST.get('Name','')
    email=request.POST.get('Email','')
    phone=request.POST.get('Phone','')
    message=request.POST.get('Message','')
    contact=Contact(name=name,email=email,phone=phone,desc=message)
    contact.save()
    return render(request,'shop/contact.html')

def tracker(request):
    return render(request,'shop/tracker.html')

def search(request):
    return render(request,'shop/search.html')

def prodview(request, myid):
    product = Product.objects.get(id=myid)  # Retrieve the product with the specified ID
    context = {'p': product}  # Create a context dictionary with the product
    return render(request, 'shop/prodview.html', context)


def checkout(request):
    return render(request,'shop/checkout.html')
