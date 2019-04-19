from django.contrib.auth import authenticate

from .models import Seller
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from .forms import SellerInfo, SellerSignIn


def info(request):
    if request.method == 'POST':
        form = SellerInfo(request.POST)
        if form.is_valid():
            pass

    else:
        form = SellerInfo()
    return render(request, 'SellerSignUp.html', {'form': form})

def seller_signin(request):
    return render(request,'Sellersignin.html')

def seller_register(request):
    if request.method == 'POST':
        form = SellerInfo(request.POST)
        if form.is_valid():

   #if request.method == 'POST':
    #    if request.POST.get('name') and request.POST.get('cnic'):
#            post = Seller()
            name = form.cleaned_data['name']#request.POST.get('name')
            cnic = form.cleaned_data['cnic']# request.POST.get('cnic')
            phone_number = form.cleaned_data['phone_number'] #request.POST.get('phone_number ')
            email= form.cleaned_data['email']#request.POST.get('email')
            address = form.cleaned_data['address']#request.POST.get('address')
            password = form.cleaned_data['password']#request.POST.get('password')
            confirm_password = form.cleaned_data['confirm_password']#request.POST.get('confirm_password')
            experience = form.cleaned_data['experience']#request.POST.get('experience')
            min_charges =form.cleaned_data['min_charges']# request.POST.get('min_charges')
            max_charges = form.cleaned_data['max_charges']#request.POST.get('max_charges')
            other_detail =form.cleaned_data['other_detail']# request.POST.get('other_detail')
            post= Seller(name=name,cnic=cnic,phone_number=phone_number,email=email,address=address,password=password,confirm_password=confirm_password,experience=experience,min_charges=min_charges,max_charges=max_charges,other_detail=other_detail)
            post.save()

            return HttpResponseRedirect(reverse('home'))
    else:
        form = SellerInfo()
    args = {'form': form}
    return render(request, 'SellerSignUp.html', args)


def seller_login(request):
    if request.method == 'POST':
        form = SellerSignIn(request.POST)
        if form.is_valid():
            email= form.cleaned_data['email']#request.POST.get('email')

            password = form.cleaned_data['password']#request.POST.get('password')#
            signindata=form.save()
            newbiodata = Seller.objects.get(pk=signindata.pk)
            if newbiodata:
                return redirect('home')
           # if Seller.objects.filter(email=request.POST['email'], password=request.POST['password']).exists():
            #    raise forms.ValidationError("Subsystem already existing")
            return HttpResponseRedirect(reverse('home'))
    else:
        form = SellerSignIn()
    args = {'form': form}
    return render(request, 'Sellersignin.html', args)
