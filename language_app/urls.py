from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_view, name='home'),
    path('add_word/', views.add_word_view, name='add_word'),
    path('quiz/', views.quiz_view, name='quiz'),
]