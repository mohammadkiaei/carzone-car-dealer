from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Cars, name='cars'),
    path('<int:id>', views.car_detail, name='car_detail'),
    path('search/', views.search, name='search'),
]