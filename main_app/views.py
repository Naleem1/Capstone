from django.shortcuts import render 
from django.views import View 
from django.http import HttpResponse 


# views 
class Home(View):
    def get(self,request):
     return HttpResponse('Home View')
    