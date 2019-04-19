from .models import Post


from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm

from PlanIt.forms import Signup_form

from django.urls import reverse_lazy
from django.views import generic
from django.conf.urls import url


from PlanIt import views
from django.contrib import admin

def backup(request):
	return render(request, "backup.html", {})
def categories(request):
    return render(request, "C:/Users/huma/PycharmProjects/MyProject/templates/categories.html", {})

def arch(request):
	return render(request, "arch.html", {})

def centrepiece(request):
	return render(request, "centrepiece.html", {})

def sculpture(request):
	return render(request, "sculpture.html", {})

def stage(request):
	return render(request, "stage.html", {})

def DropsPops(request):
	return render(request, "DropsPops.html", {})

def name(request):
	return render(request, "name.html", {})

def lights(request):
	return render(request, "lights.html", {})

def room(request):
	return render(request, "room.html", {})

def Car(request):
	return render(request, "Car.html", {})
# Create your views here.
class HomePageView(TemplateView):
    template_name = "index.html"


# def  index(request):
#   return render(request, "index.html")
class AboutPageView(TemplateView):
    template_name = "about.html"




#class SignUp(generic.CreateView):
 #   form_class = UserCreationForm
    #success_url = reverse_lazy('login')
  #  template_name = "signup.html"



#class login():

 #   success_url = reverse_lazy('login')
#    template_name = 'login.html'

def login_view(request):
    if request.method=='POST':
        form =AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/signup.html', {'form': form})

#Post and images

def postseller(request):
    return HttpResponse("<h2>fuydvfybf</h2>")
  #  all_post =Post.objects.all()
   # html=''
    #for posts in all_post:
     #   url= '/sellerpost/' + str(posts.id)+'/'
      #  html+='<a href="'+url+'">' + posts.post_text + '</a><br>'
    #return HttpResponse(html)

def detail(request, post_id):

    return HttpResponse("<h2>this " + str(post_id)+"</h2>")