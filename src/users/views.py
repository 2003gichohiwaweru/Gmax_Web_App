from django.shortcuts import redirect, render 
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.
#Th login view 


def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            print(user)
            if  user is not None:
                login(request, user)
                messages.success(request, 'You have succesfully logged in as {username}. ')
                return redirect('home')
            else: 
                messages.error(request, f'Unable to Log in')
        else:
            messages.error(request, f'An error occured trying while trying to log in')
    elif request.method == 'GET':
        login_form =AuthenticationForm()
    
    return render(request, 'views/login.html', {'login_form': login_form})



def register_view(request):
    return render(request, 'views/register.html')