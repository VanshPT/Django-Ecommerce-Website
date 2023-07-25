from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    produt_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=1000000000)
    pub_date=models.DateField()
    image=models.ImageField(upload_to='shop/images',default="")

    def __str__(self):
        return self.produt_name
class Contact(models.Model):
    contact_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=70,default="")
    phone=models.CharField(max_length=30,default="")
    desc=models.CharField(max_length=10000,default="")

    def __str__(self):
        return self.name
class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=100000)
    amount=models.CharField(max_length=100,default="")
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50,default="")
    address=models.CharField(max_length=100,default="")
    address_line_2=models.CharField(max_length=500,default="")
    city=models.CharField(max_length=50,default="")
    state=models.CharField(max_length=50,default="")
    zip_code=models.CharField(max_length=30,default="")
    phone=models.CharField(max_length=40,default="")

    def __str__(self):
        return self.name
class OrderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default="")
    update_desc=models.CharField(max_length=5000)
    timestamp=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.update_desc[0:7]+"..."
#first we run migrate command, then add table to our models.py file. as soon as we add tables in our models.py, we have to change from appname in installed apps to appname.apps.AppnameConfig(shop.apps.ShopConfig) ,then we have to run python manage.py makemigrations. after that we finally do the migrations by python manage.py migrate. We can see our database made here in models.py by django admin. for acccessing django admin page, we need to create a superuser which could only access django/admin page. for that write pytohn manage.py createsuperuser
#we have to register now our model on admin.py

#IMPORTANT
#we can upload images here inside images but this is not recommended manner. we use media directory for storing all media items.
#see how to add media files in settings.py file in every website. after doing that stuff, do changes in urls.py of mac, see what changes we have done and do it on every website

#to show product information from database into front end, do following steps

# we define mac/templates in DIRS in settings file only if we add templates in our project directory. we dont need to add that while making templates of app.

# we push the updates of a particular order in django admin by adding one order update of same order_id.