from django.urls import path
from . import views

urlpatterns =[
    path('', views.base, name='base'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('dashbord', views.dashbord, name='dashbord'),
    path('createrecord', views.createrecord, name='createrecord'),
    path('updaterecord/<int:pk>', views.updaterecord, name='updaterecord'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('viewrecord/<int:pk>', views.viewrecord, name='viewrecord'),
]