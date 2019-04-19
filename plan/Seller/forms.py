from django import forms
from Seller.models import Seller
class SellerInfo(forms.Form):

    name = forms.CharField(max_length=100)
    cnic = forms.IntegerField(required=True)
    phone_number = forms.IntegerField(required=True)
    email = forms.EmailField(max_length=70,required=True)
    password = forms.CharField(max_length=32,required=True, widget=forms.PasswordInput)

    confirm_password = forms.CharField(max_length=32 ,required=True,widget=forms.PasswordInput)
    address = forms.CharField(max_length=100 , required=True)
    experience = forms.Field()
    min_charges = forms.IntegerField()
    max_charges = forms.IntegerField()
    # profile_pic = models.ImageField()
    other_detail = forms.Field()


    def clean(self):
        cleaned_data = super(SellerInfo, self).clean()
        name = cleaned_data.get('name')
        cnic = cleaned_data.get('cnic')
        phone_number= cleaned_data.get('phone_number')
        email = cleaned_data.get('email')
        password=cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        address = cleaned_data.get('address')
        experience = cleaned_data.get('experience')
        min_charges = cleaned_data.get('min_charges')
        max_charges = cleaned_data.get('max_charges')
        other_detail = cleaned_data.get('other_detail')
        if not name and not email and not experience:
            raise forms.ValidationError('You have to write something!')



class SellerSignIn(forms.Form):


    email = forms.EmailField(max_length=70,required=True)
    password = forms.CharField(max_length=32,required=True, widget=forms.PasswordInput)



    def clean(self):
        cleaned_data = super(SellerInfo, self).clean()

        email = cleaned_data.get('email')
        password=cleaned_data.get('password')

        if not password and not email :
            raise forms.ValidationError('You have to write something!')