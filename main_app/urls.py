from djando.urls import path
from . import views

urlspattern = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),
]