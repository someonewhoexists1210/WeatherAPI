from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import CustomUser


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Password'}),
        help_text="Your password must be at least 8 characters long, contain letters and numbers, and should not be too common."
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Confirm Password'}),
        help_text="Enter the same password as before, for verification."
    )
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'latitude', 'longitude', 'city']
        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
            'city': forms.HiddenInput(),
        }

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
