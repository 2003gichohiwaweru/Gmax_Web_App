from django.shortcuts import redirect, render 
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views import View
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
                messages.success(request, f'You have succesfully logged in as {username}')
                return redirect('home')
            else: 
                messages.error(request, f'Unable to Log in')
        else:
            messages.error(request, f'An error occured trying while trying to log in')
    elif request.method == 'GET':
        login_form =AuthenticationForm()
    
    return render(request, 'views/login.html', {'login_form': login_form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('main')

class RegisterView(View):
    def get(self, request):
        register_form = UserCreationForm()
        return render(request, 'views/register.html', {'register_form': register_form})
    

    def post(self, request):
        register_form = UserCreationForm(data=request.POST)
        if register_form.is_valid():
            user = register_form.save()
            user.refresh_from_db()
           
            login(request, user)
            messages.success(
                request, f'User {user.username} is registered succefully')
            return redirect('home')
        else:
            messages.error(request, f'An error occured trying while trying to register in')
            return render(request, 'views/register.html', {'register_form': register_form})