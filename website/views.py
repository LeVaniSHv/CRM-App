from django.shortcuts import render, redirect
from django.contrib.auth import  login, logout, authenticate
from django.contrib import messages





def home(request):
    
    # Check to see if loggin in 
    
    
    if request.method == "POST":
        
        username = request.POST['username']
        password = request.POST["password"]
        
        
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request, user)
            
            messages.success(request,"You have been logged in ! ")
            return redirect("home")
        
        else:
            
            messages.success(request, "Username or Password is not correct ! ")
            return redirect("home")
        
    else :
        
        
        return render(request, 'home.html', )




def login_user(request):
    
    pass


def logout_user(request):
    
    messages.success(request, "You have been logged out! ")
    logout(request)
    
    return redirect("home")