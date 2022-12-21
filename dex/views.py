from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Member, Company
from .forms import MemberForm, UserForm

from django.contrib.auth.models import AbstractUser, User
# Add LoginForm to this line...
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# ...and add the following line...
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect


class CompanyCreate(CreateView):
  model = Company
  fields = '__all__'
  success_url = '/companies'

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.user = self.request.user
    self.object.save()
    return HttpResponseRedirect('/companies')

class MemberCreate(CreateView):
  model = Member
  fields = '__all__'
  success_url = '/members'

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.user = self.request.user
    self.object.save()
    return HttpResponseRedirect('/members')

class MemberUpdate(UpdateView):
  model = Member
  fields = ['company','first_name','last_name','email','phone','department']

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.save()
    print(self.object.id)
    return HttpResponseRedirect('/profile/' + str(self.object.id))


def index(request):
    companies = list(Company.objects.all())
    return render(request, "companies/index.html", { 'companies': companies })

def members_views(request):
    members = list(Member.objects.all())
    return render(request, "users/members.html", { 'members': members})

def about(request):
    return render(request, "dex/about.html")

def company_views(request):
    comps = Company.objects.all()
    print(comps, 'comps print')
    return render(request, "companies/companies.html", {"comps": comps})

def company_details(request, company_id):
    comp = Company.objects.get(id=company_id)
    return render(request, "companies/show.html", {"comp": comp})

def contact(request):
    return render(request, "companies/contact.html")


def team(request, company_id):
    print('COMPANY ID PRINT ========>>>', company_id)
    team = Member.objects.all()
    return render(request, "companies/team.html", {"team": team})

def department(request):
    return render(request, "companies/department.html")


def profile(request, member_id):
    member = Member.objects.get(id=member_id)

    return render(request, 'users/profile.html', {'member': member})


def login_view(request):
     # if post, then authenticate (user submitted username and password)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/'+u)
                else:
                    print('The account has been disabled.')
            else:
                print('The username and/or password is incorrect.')
    else: # it was a get request so send the emtpy login form
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print('User created', user)
            return HttpResponseRedirect('/member/' + str(user.id) + '/update/')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})