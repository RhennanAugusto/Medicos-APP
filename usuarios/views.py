from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth


def cadastro(request):
    # uso esses if para diferenciar as requisições
    # para printar uma mensagem do python direto no hmtl eu uso {{}}
    if request.method == 'GET':
       return render (request, 'cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username') 
        email = request.POST.get('email') 
        senha = request.POST.get('senha') 
        confirmar_senha = request.POST.get('confirmar_senha') 
        
        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR,"As senhas devem ser iguais") # passar dois parametros para a mensagem de erro
            return redirect ('/usuarios/cadastro')
        if len(senha) < 6:
            messages.add_message(request, constants.ERROR,"A senha deve ter mais de 6 dígitos")
            return redirect ('/usuarios/cadastro')
        
        users = User.objects.filter(username=username)  

        if users.exists():
            messages.add_message(request, constants.ERROR,"Esse usuário já existe.")
            return redirect ('/usuarios/cadastro')

        user = User.objects.create_user(
            username = username,
            email = email,
            password = senha
        )

        
        return redirect('/usuarios/login')

def login(request):
    if request.method=="GET":
       return render(request,'login.html')
        
    elif request.method == "POST":
        username = request.POST.get('username') 
        senha = request.POST.get('senha') 

        user = auth.authenticate(request, username=username, password=senha) # verifica no banco se existe um usuario com nome e senha se existir retorna uma instancia e caso nao exista retorna none
 
        if user:
            auth.login(request, user) # atrelando ip com a requisição
            return redirect('/pacientes/home')
        
        messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos')
        return redirect ('/usuarios/login')

def sair(request): #caso eu queira saber os dados é so colocar request.user.email e vou trocando as informações
    auth.logout(request) 
    return redirect('/usuarios/login')