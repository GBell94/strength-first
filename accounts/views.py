#from django.shortcuts import render, redirect
#from .forms import RegisterForm

# Create your views here.
#def register(response):
    #if response.method == "POST":
        #form = RegisterForm(response.POST)
        #if form.is_valid():
            #form.save()
            
        #return redirect('/home')  
    #else:   
        #form = RegisterForm()

    #return render(response, "register.html", {"form": form})

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You can now log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})