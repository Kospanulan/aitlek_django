from django import forms

from blog.models import Post


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'text']

