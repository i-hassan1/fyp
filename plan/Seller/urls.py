from django.conf.urls import url

from Seller import views
from django.urls import path

urlpatterns = [

   url(r'^info/$', views.seller_register ,name='info'),
url(r'^sellersignin/$', views.seller_signin ,name='sellersignin'),
#   path('info/', views.Info, name='info'),

]