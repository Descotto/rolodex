from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import User, Company



def index(request):
    companies = list(Company.objects.all())
    return render(request, "companies/index.html", { 'companies': companies })
    

def about(request):
    return render(request, "dex/about.html")


def contact(request):
    return render(request, "companies/contact.html")


def team(request):
    return render(request, "companies/team.html")

def department(request):
    return render(request, "companies/department.html")
