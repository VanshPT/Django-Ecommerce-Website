from django.shortcuts import render
from .models import Product,Contact,Orders,OrderUpdate
from math import ceil
import json

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
    if request.method=="POST":
        print(request)
        orderid=request.POST.get('orderid','')
        email=request.POST.get('email','')
        try:
            orders=Orders.objects.filter(orderid=orderid,email=email)
            if(len(orders)>0):
                updates=OrderUpdate.objects.filter(orderid=orderid)
                oupdates=[]
                for update in updates :
                    oupdates.append({'text':update.update_desc,'time':update.timestamp})
                    response=json.dumps(oupdates)
                    return HttpResponse(response)
        except:
            pass
    return render(request,'shop/tracker.html')

def search(request):
    return render(request,'shop/search.html')

def prodview(request, myid):
    product = Product.objects.get(id=myid)  # Retrieve the product with the specified ID
    context = {'p': product}  # Create a context dictionary with the product
    return render(request, 'shop/prodview.html', context)


def checkout(request):
    if request.method=="POST":
        print(request)
        itemsjson=request.POST.get('itemsJson','')
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        address=request.POST.get('address','')
        address_line_2=request.POST.get('address_line_2','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zip_code=request.POST.get('zip_code','')
        phone=request.POST.get('phone','')
        print(name)
        orders=Orders(items_json=itemsjson,name=name,email=email,address=address,address_line_2=address_line_2,city=city,state=state,zip_code=zip_code,phone=phone)
        orders.save()
        update=OrderUpdate(order_id=orders.order_id,update_desc="The Order has been placed")
        update.save()
    return render(request,'shop/checkout.html')
