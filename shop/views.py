from django.shortcuts import render
from .models import Product,Contact,Orders,OrderUpdate
from math import ceil
import json
from django.views.decorators.csrf import csrf_exempt
import razorpay
from django.conf import settings
# from checksumdir import Checksum


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
        orderid = request.POST.get('orderid', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderid, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderid)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')

def search(request):
    return render(request,'shop/search.html')

def prodview(request, myid):
    product = Product.objects.get(id=myid)  # Retrieve the product with the specified ID
    context = {'p': product}  # Create a context dictionary with the product
    return render(request, 'shop/prodview.html', context)


def checkout(request):
    allorders = None
    payment = None
    if request.method=="POST":
        print(request)
        itemsjson=request.POST.get('itemsJson','')
        amount=request.POST.get('amount','')
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        address=request.POST.get('address','')
        address_line_2=request.POST.get('address_line_2','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zip_code=request.POST.get('zip_code','')
        phone=request.POST.get('phone','')
        orders=Orders(items_json=itemsjson,amount=amount,name=name,email=email,address=address,address_line_2=address_line_2,city=city,state=state,zip_code=zip_code,phone=phone)
        #vvvvvvvvvvvvvviiiiiiiiimmmpp  these arguments in Orders class should be in order only otherwise wont be accepted
        orders.save()
        allorders=Orders.objects.filter(razor_pay_order_id=orders.razor_pay_order_id)
        amount = int(float(orders.amount) * 100)
        client=razorpay.Client(auth=('rzp_test_esdA78rxfTZHjI','5cP6r0OXiy5j1ijUT6o3HGJN'))
        data={'amount':amount,'currency':'INR','payment_capture':1}
        payment=client.order.create(data=data)
        update=OrderUpdate(razor_pay_order_id=orders.razor_pay_order_id,update_desc="The Order has been placed")
        update.save()
        
    
    context={'orders':allorders,'payment':payment}
    return render(request, 'shop/checkout.html',context)


def thankyou(request):
    razorpay_payment_id = request.GET.get('razorpay_payment_id')
    razorpay_order_id = request.GET.get('razorpay_order_id')
    razorpay_signature = request.GET.get('razorpay_signature')
    try:
        orders = Orders.objects.get(razor_pay_order_id=razorpay_order_id)
        order = orders.first()
        order.is_paid = True
        order.save()
        context = {
            'razorpay_payment_id': razorpay_payment_id,
            'razorpay_order_id': razorpay_order_id,
            'razorpay_signature': razorpay_signature,
        }
        return render(request, 'shop/thankyou.html', context)
        
    except Orders.DoesNotExist:
        return HttpResponse("Invalid Order ID")