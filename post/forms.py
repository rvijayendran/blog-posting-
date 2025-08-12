from .models import comments , Post
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class loginForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, max_length=20, required=False)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username","email","password"]
        
    def clean(self):
        cleaned_data =  super().clean()
        password = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm_password")
        
        if password and confirm and password != confirm:
            self.add_error('confirm_password', "Passwords do not match.")
            
            
class Login_pageForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class post_uploadform(ModelForm):
        class Meta:
            model = Post
            fields = ["title","content","image_name"]


class commentsForm(ModelForm):
    
    class Meta:
        model = comments
        fields = ["comments"]
