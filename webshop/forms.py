from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import ProductReview
from django import forms

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={'class': 'form-input', 'placeholder': 'Имя пользователя'}
        ))
    
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-input', 'placeholder': 'Пароль'}
        ))

    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-input', 'placeholder': 'Повторите пароль'}
        ))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={'class': 'form-input', 'placeholder': 'Имя пользователя'}
        ))

    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-input', 'placeholder': 'Пароль'}
        ))


class ReviewForm(forms.ModelForm):
    content = forms.CharField(label='Content',  widget=forms.Textarea(
        attrs={'class': 'review-text', 'maxlength': '2048'}
        ), required=True)
    is_recommend = forms.BooleanField(label='Will you recommend?', initial=True, required=False)

    class Meta:
        model = ProductReview
        fields = ['content', 'is_recommend']