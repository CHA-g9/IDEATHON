from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def start1(request):
    return render(request, 'signin.html')

def start2(request):
    return render(request, 'login.html')

def CAT_HOME(request):
    username = request.POST['username']
    return render(request, 'MAIN.html', {'username' : username})

def signin(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render (request, 'error_signin.html')

            except:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return render(request, 'login.html')
        else:
            return render (request, 'error_signin.html')
    return render(request, 'signin.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            username = request.POST['username']
            return render(request, 'MAIN.html', {'username' : username})

        else:
            return render(request, 'error_login.html')
    
    else:
        return render(request, 'login.html')
