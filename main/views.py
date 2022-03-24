from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse
from django.shortcuts import render, redirect


User = get_user_model()


@login_required(login_url='login_attempts')
def user_list(request):
    users = User.objects.select_related('logged_in_user')
    for user in users:
        user.status = 'Online' if hasattr(
            user, 'logged_in_user') else 'Offline'
    return render(request, 'user_list.html', {'users': users})


def login_attempts(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('login_attempts')
        else:
            print(form.errors)
    return render(request, 'login_attempts.html', {'form': form})


@login_required(login_url='login_attempts')
def logout_attempts(request):
    logout(request)
    return redirect('login_attempts')


def register_attempts(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_attempts')
        else:
            print(form.errors)
    return render(request, 'register_attempts.html', {'form': form})
