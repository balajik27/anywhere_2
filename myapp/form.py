from django import forms

from .models import Employee

# class Userform(forms.Form):
#     name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Username'}))
#     email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email'}))
#     country = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Country'}))

#     class Meta:
#         model = Employee
#         fields = ('name', 'email','country')
