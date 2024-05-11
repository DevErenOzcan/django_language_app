from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='index'),
    path('login/', views.login_page, name='login'),
]