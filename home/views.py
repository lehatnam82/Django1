from django.shortcuts import render
from django.http import HttpResponse
from blog.models import modelBlog
from django.core.paginator import Paginator



def index(request):
    listBlog = modelBlog.objects.all()
    paginator = Paginator(listBlog, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,"home/index.html",{"listBlog":page_obj})
