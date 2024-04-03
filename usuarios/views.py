from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth
from django.urls import reverse
from .forms import LoginForm,CadastroForm


def cadastro(request):
    if request.method == 'GET':
        form = CadastroForm()
        return render(request, 'registration/cadastro.html', {'form': form})
    elif request.method =='POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['password']
            confirmar_senha = form.cleaned_data['confirm_password']

        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'Senha e confirmar senha diferentes')
            return redirect('/usuarios/cadastro')
        
        user = User.objects.filter(username=username)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'Usuário já existente')
            return redirect('/usuarios/cadastro')
        
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=confirmar_senha
            )
            return redirect('/usuarios/login')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno no servidor')
            return redirect('/usuarios/cadastro')
    return render(request, 'registration/cadastro.html', {'form': form})
    
def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            senha = form.cleaned_data['password']
            
            if '@' in username:
                user = auth.authenticate(request, email=username, password=senha)
            else:
                user = auth.authenticate(request, username=username, password=senha)

            if user:
                auth.login(request, user)
                messages.success(request, 'Logado!')
                return redirect(reverse('novo_flashcard'))
            else:
                messages.error(request, 'Username ou senha inválidos')
                return redirect(reverse('login'))
   

def logout(request):
    if request.method == "GET":
        auth.logout(request)
        return redirect('/usuarios/login')
    

