# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from .models import Comment 
# TagWidget()", widgets

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "content", "tags")  # author is set in the view

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={"rows":3}), label="")

    class Meta:
        model = Comment
        fields = ("content",)



