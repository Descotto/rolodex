from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Member, Company

from django.contrib.auth.models import User
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




def index(request):
    companies = list(Company.objects.all())
    return render(request, "companies/index.html", { 'companies': companies })

def members_views(request):
    members = list(Member.objects.all())
    return render(request, "users/members.html", { 'members': members})

def about(request):
    return render(request, "dex/about.html")


def singup(request):
    return render(request, "dex/singup.html")


def contact(request):
    return render(request, "companies/contact.html")


def team(request):
    return render(request, "companies/team.html")

def department(request):
    return render(request, "companies/department.html")


def profile(request, member_id):
    member = Member.objects.get(id=member_id)

    return render(request, 'users/profile.html', {'member': member})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/cats')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})