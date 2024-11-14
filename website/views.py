from django.shortcuts import render, redirect
from django.contrib.auth import  login, logout, authenticate
from django.contrib import messages
from .forms import SignUpForm
from .models import Record




def home(request):
    
    records = Record.objects.all()
    
    
    
    
    
    
    
    
    # Check to see if loggin in 
    
    
    if request.method == "POST":
        
        username = request.POST['username']
        password = request.POST["password"]
        
        
        
        user = authenticate(username = username, password = password)
        
        if user is not None:
            login(request, user)
            
            messages.success(request,"You have been logged in ! ")
            return redirect("home")
        
        else:
            
            messages.success(request, "Username or Password is not correct ! ")
            return redirect("home")
        
    else :
        
        
        return render(request, 'home.html', {'records': records} )




def logout_user(request):
    
    messages.success(request, "You have been logged out! ")
    logout(request)

    
    return redirect("home")



def register_user(request):
    
    
    if not request.user.is_authenticated:
        if request.method == 'POST' :
            form = SignUpForm(request.POST)
            
            if form.is_valid():
                form.save()
                # Authenticate and login
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                
            
                user = authenticate(username=username, password=password)
                login(request, user)
                messages.success(request, "You Have Successfully Registered! Welcome!")
                return redirect('home')
        else:
            form = SignUpForm()
            return render(request, 'register.html', {'form':form})


        return render(request, 'register.html', {'form':form})
    else:
        return redirect('home')


def costumer_record(request, pk):
    
    
    if request.user.is_authenticated:
        
        
        costumer_record = Record.objects.get(id=pk)
        
        return render(request, 'record.html', {'record':costumer_record})
    
    else :
        
        messages.success(request, "You must be logged in ! ")
        return redirect('home')
        
        
def delete_record(request, pk):
    
    if request.user.is_authenticated:
        
        delete_record = Record.objects.get(id=pk)
    
        delete_record.delete()
    
            
        messages.success(request, "Record Has Been Deleted ")
        return redirect('home')
        
    else :
        
        messages.success(request, "You must be logged in ! ")
        return redirect('home')
        
        

def add_record(request):
    
    return render(request, 'add_record.html', {})