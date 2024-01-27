from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Customer,Employee
from django.forms import PasswordInput,TextInput




#Customer Registration Form
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

#Customer Form For Customer Details in customer table in database
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['phone','address','name']
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address' : forms.TextInput(attrs={'class': 'form-control'}),
        }

#Login Form for login page
class LoginForm(AuthenticationForm):    
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))



#Employee creation form for admin
class EmployeeForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {            
            'username': forms.TextInput(attrs={'class': 'form-control'}),            
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),            
        }

    def save(self, commit=True):
        user = super(EmployeeForm, self).save(commit=False)
        user.is_staff = True
        if commit:
            user.save()
        return user
    
#Employee Details Form For Employee Details in employee table in database
class EmployeeDetailsForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name','email','phone','address']
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control'}),
        }
