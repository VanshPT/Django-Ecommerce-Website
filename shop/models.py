from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    produt_name=models.CharField(max_length=30)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
#first we run migrate command, then add table to our models.py file. as soon as we add tables in our models.py, we have to change from appname in installed apps to appname.apps.AppnameConfig(shop.apps.ShopConfig) ,then we have to run python manage.py makemigrations. after that we finally do the migrations by python manage.py migrate. We can see our database made here in models.py by django admin. for acccessing django admin page, we need to create a superuser which could only access django/admin page. for that write pytohn manage.py createsuperuser
#we have to register now our model on admin.py