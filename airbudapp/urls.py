from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cari/', views.search, name='search'),
    path('saran/', views.opinion, name='saran'),
]