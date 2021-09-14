from django.shortcuts import render
from django.views import View
# Create your views here.
class HomeView(View):
    def get(sefl,request):
        return render(request,'home/index.html')