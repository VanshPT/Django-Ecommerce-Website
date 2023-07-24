from django.urls import path
from . import views

urlpatterns = [
    path("", views.index,name="BlogIndex"),
    path("blogPost/<int:myid>", views.blogPost,name="BlogPost"),
]