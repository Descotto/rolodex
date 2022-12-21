from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('departments/', views.department, name='department'),
    path('signup/', views.signup, name='signup'),
    path('profile/<int:member_id>/', views.profile, name='profile'),
    path('members/', views.members_views, name='members_views'),
    path('company/create/', views.CompanyCreate.as_view(), name='company_create'),
    path('companies/', views.company_views, name='companies_views'),
    path('companies/<int:company_id>', views.company_details, name='companies_views'),
    path('team/<int:company_id>', views.team, name='team'),
    path('member/<int:pk>/update/', views.MemberUpdate.as_view(), name='member_create'),
    path('member/create/', views.MemberCreate.as_view(), name='member_create'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name="logout"),
]