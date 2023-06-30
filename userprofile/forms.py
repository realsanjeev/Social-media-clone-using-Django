from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.models import User
from userprofile.models import Profile

class MyLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-control input-field', 'placeholder': 'Username' }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-control input-field', 'placeholder': 'Password' }))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove labels
        self.fields['username'].label = False
        self.fields['password'].label = False

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, 
        widget=forms.TextInput(attrs={
            'class': 'input-control input-field',
            'placeholder': 'First Name'
            }))
    last_name = forms.CharField(max_length=30, 
        widget=forms.TextInput(attrs={
            'class': 'input-control input-field',
            'placeholder': 'Last Name'
            }))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'input-control input-field',
            'placeholder': 'example@mail.com'
            }))
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'input-control input-field',
            'placeholder': '@username'
            }))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'input-control input-field',
            'placeholder': 'Password'
            }),
        help_text="Enter the same password as before, for verification.")
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'input-control input-field',
            'placeholder': 'Confirm Password'
            }))
    
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove labels
        # self.fields['username'].label = False
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"

        # add class for form element
        for field in self.fields.values():
            field.widget.attrs['class']='input-control input-field'
        