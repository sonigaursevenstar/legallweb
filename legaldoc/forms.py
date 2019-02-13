from django import forms
from django.contrib.auth.forms import UserCreationForm
from legaldoc.models import Headerfooter,Personnel, User,Param_values
from django.core.exceptions import ValidationError
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Headerfooter
        fields = ('type','content','img')

class SignUpForm(forms.ModelForm):
   first_name = forms.CharField(label='Enter NAME', min_length=4, max_length=150)
   username = forms.CharField(label='Enter NAME', min_length=4, max_length=150)
   email = forms.CharField(label='Enter Email_address', min_length=4, max_length=150)
   Hourly_fee = forms.CharField(label='Enter Hourly_fee', min_length=4, max_length=150)
   Phone_number = forms.CharField(label='Enter Phone_number', min_length=4, max_length=150)
   Calendar_name = forms.CharField(label='Enter Calendar_name', min_length=4, max_length=150)
   password = forms.CharField(label='Enter Password',widget=forms.PasswordInput())
   Password2 = forms.CharField(label='Enter Password2',widget=forms.PasswordInput())
   
   def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = self.cleaned_data.get('password')
        Password2 = self.cleaned_data.get('Password2')
 
        if password and Password2 and password != Password2:
            raise forms.ValidationError("Password and Confirm Password don't match")
          
        return cleaned_data
   class Meta:
        model = User
        fields = ('first_name', 'email','username', 'Hourly_fee', 'Phone_number','Calendar_name', 'password','is_staff')

class Person(forms.ModelForm):
    """class Meta:
        model = Personnel
        fields = ['Email_address', 'Password']"""
"""class FileFieldForm(forms.ModelForm):
    Value = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
	
    Case_NAME = forms.CharField(label='Enter NAME', min_length=4, max_length=150)
    Person_id= forms.CharField(label='Enter Email_address', min_length=4, max_length=150)
    class Meta:
        model = Param_values
        fields = ('Value', 'Parameter_name','Case_NAME', 'Person_id')"""

		

