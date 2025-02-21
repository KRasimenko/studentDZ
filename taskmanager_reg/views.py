from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import RegistrationForm
from .models import CustomUser

def choose_role(request):
    return render(request, 'taskmanager_reg/choose_role.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_active = True
            user.save()
            messages.success(request, 'Регистрация успешна! Ожидайте подтверждения администратора.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'taskmanager_reg/register.html', {'form': form})