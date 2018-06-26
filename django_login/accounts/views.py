from django.contrib.auth.forms import UserCreationForm
from django.urls import path
from django.views import generic

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = '' 
    template_name = 'signup.html'

