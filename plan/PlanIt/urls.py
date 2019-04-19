from django.conf.urls import url
from . import views
#from PlanIt import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
   url('signup/', views.signup, name='signup'),

     url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', auth_views.auth_logout, name='logout'),
    url('admin/', admin.site.urls),
    #url(r'^signup/$', views.signup),

	path('categories/', views.categories, name='categories'),

    path('arch/', views.arch, name='arch'),
    path('centrepiece/', views.centrepiece, name='centrepiece'),
    path('sculpture/', views.sculpture, name='sculpture'),
    path('stage/', views.stage, name='stage'),
    path('DropsPops/', views.DropsPops, name='DropsPops'),
    path('name/', views.name, name='name'),
    path('lights/', views.lights, name='lights'),
    path('room/', views.room, name='room'),
    path('Car/', views.Car, name='Car'),
    path('backup/', views.backup, name='backup'),

    url('sellerpost/', views.postseller, name='home'),

    url(r'^(?P<post_id>[0-9]+)$/', views.detail, name='detail'),

]

