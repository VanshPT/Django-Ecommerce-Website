from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost

def index(request):
    Blogs=BlogPost.objects.values('post_id','title','head0','chead01','thumbnail','pub_date')#we write this query if we want only post id of our blogs and nothing else from database
    BlogDict={'blog':Blogs}
    # print(Blogs)
    return render(request,'blog/index.html',BlogDict)
def blogPost(request,myid):
    BlogById=BlogPost.objects.get(post_id=myid) #used to retrieve a full specified tuple instead of retreiving all elements of database like .values
    params={'blog':BlogById}
    return render(request,'blog/blogPost.html',params)
