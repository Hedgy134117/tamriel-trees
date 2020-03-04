from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)
            return redirect('')
    else:
        form = AuthenticationForm()
    return render(request, 'authentication/login.html', {'form': form})

def logoutView(request):
    logout(request)
    return redirect('')

def signupView(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            # log the user in
            login(request, user)
            return redirect('')
    else:
        form = UserCreationForm()
    return render(request, 'authentication/signup.html', {'form': form})