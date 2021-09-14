from django.shortcuts import render
from django.http import HttpResponse
from .models import modelBlog
def blog(request,slug):
    data = modelBlog.objects.all()
    for i in range(len(data)):
        if(data[i].slug==slug):
            if(i==len(data)-1):
                next = None
            else:
                next = data[i+1].slug
            if(i==0):
                previous = None
            else:
                previous = data[i-1].slug
    

    blog_show = modelBlog.objects.get(slug=slug)
    print(type(next),type(previous))
    return render(request,"blog/blog.html",{"blog_show":blog_show,"next":next,"previous":previous})