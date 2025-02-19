from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('/')  # Change 'home' to your actual homepage route name
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    return render(request, 'login.html')


#register
def register(request) :

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']

        if(password == confirm_password):
            if User.objects.filter(username=username).exists():
                messages.error(request,f'Account with {username} already exits try another username.')   
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request,f'{email} already exists.')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save();
                messages.success(request,f"Created an account with {username}")
                return redirect('login')
        else:   
            messages.error('password not matched')    
        
        return redirect('/')

        
    else:
        return render(request,'register.html')
    

def logout(request):
    auth.logout(request)
    return redirect('/')
