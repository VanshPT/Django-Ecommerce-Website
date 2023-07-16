from django.urls import path
from . import views

urlpatterns = [
    path("", views.index,name="ShopIndex"),
    path("about/", views.about,name="AboutUs"),
    path("contact/", views.contact,name="ContactUs"),
    path("tracker/", views.tracker,name="TrackingStatus"),
    path("search/", views.search,name="Search"),
    path("prodview/<int:myid>", views.prodview,name="Prodview"),
    path("checkout/", views.checkout,name="Checkout")
    
]