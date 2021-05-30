from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tes/', views.get_data, name='result'),
    path('cari/', views.search, name='search'),
]