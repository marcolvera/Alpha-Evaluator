from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('companies/<int:company_id>/', views.company_detail, name='detail'),
]