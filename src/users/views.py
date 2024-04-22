from django.shortcuts import render 
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
#Th login view 


def login_view(request):
    login_form = AuthenticationForm()
    return render(request, 'views/login.html', {'login_form': login_form})