from django.shortcuts import render
from django.views import generic

from .forms import CustomUserCreationForm

class SignUp(generic.CreateView):
	form_class = CustomUserCreationForm
	success_url = 'home'
	template_name = 'signup.html'
