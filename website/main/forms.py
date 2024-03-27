from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main.models import Post, Reply

#Forms to be used in login and posting

class RegisterForm(UserCreationForm) :
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

class PostForm(forms.ModelForm) :
    class Meta:
        model = Post
        fields = ["title", "description"]

class ReplyForm(forms.ModelForm) :
    content = forms.CharField(widget = forms.Textarea(attrs={'name' : 'Reply', 'style' : 'height : 3em; width: 80%; margin-left: 10%', 'autofocus' : 'autofocus'}))
    class Meta :
        model = Reply
        fields = ["content"]
