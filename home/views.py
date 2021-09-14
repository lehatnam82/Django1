from django.shortcuts import render
from django.http import HttpResponse
from blog.models import modelBlog
def index(request):
    listBlog = modelBlog.objects.all()
    return render(request,"home/index.html",{"listBlog":listBlog})
