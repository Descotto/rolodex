from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('team/', views.team, name='team'),
    path('departments/', views.department, name='department'),
    path('singup/', views.singup, name='singup'),
    path('profile/<int:member_id>/', views.profile, name='profile'),
    path('members/', views.members_views, name='members_views'),
    path('company/create/', views.CompanyCreate.as_view(), name='company_create'),
    path('member/create/', views.MemberCreate.as_view(), name='member_create'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.signup, name='signup'),
]