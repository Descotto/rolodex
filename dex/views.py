from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import User, Company



def index(request):
    companies = list(Company.objects.all())
    return render(request, "dex/index.html", { 'companies': companies })
    

   

