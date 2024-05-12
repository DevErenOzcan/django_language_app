from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('forgot_password/', views.forgot_password_page, name='forgot_password'),
]