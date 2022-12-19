from django.contrib.auth.models import AbstractUser, User
from .models import Member
from django.forms import ModelForm

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ('first_name', 'last_name', 'email', 'phone', 'department', 'address')