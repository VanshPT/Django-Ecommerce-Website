from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    produt_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    image=models.ImageField(upload_to='shop/images',default="")

    def __str__(self):
        return self.produt_name
#first we run migrate command, then add table to our models.py file. as soon as we add tables in our models.py, we have to change from appname in installed apps to appname.apps.AppnameConfig(shop.apps.ShopConfig) ,then we have to run python manage.py makemigrations. after that we finally do the migrations by python manage.py migrate. We can see our database made here in models.py by django admin. for acccessing django admin page, we need to create a superuser which could only access django/admin page. for that write pytohn manage.py createsuperuser
#we have to register now our model on admin.py

#IMPORTANT
#we can upload images here inside images but this is not recommended manner. we use media directory for storing all media items.
#see how to add media files in settings.py file in every website. after doing that stuff, do changes in urls.py of mac, see what changes we have done and do it on every website

#to show product information from database into front end, do following steps