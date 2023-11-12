from django.shortcuts import render, redirect, HttpResponse
from .models import UserProfile, Deposito
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


"""
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')
    """

def fazer_deposito(request):
    if request.method == 'POST':
        valor_deposito = float(request.POST.get('valor'))
        user_profile = UserProfile.objects.get(user=request.user)

        # Criar um objeto Deposito
        deposito = Deposito.objects.create(user=request.user, valor=valor_deposito)

        # Calcular e aplicar cashback
        cashback = user_profile.calcular_cashback(valor_deposito)

        return render(request, 'sucesso_deposito.html', {'deposito': deposito, 'cashback': cashback})

    return render(request, 'form_deposito.html')


def home(request):
    return render(request, 'core/index.html')


def rotas(request):
    return render(request, 'core/rotas.html')


def cadastro(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("As senhas não são iguais!!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('core_login')

    return render(request,'core/cadastro.html')


def pagina_de_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('core_home')
        else:
            return HttpResponse ("Nome de usuário ou senha incorretos!!!")

    return render(request,'core/login.html')


def pagina_de_logout(request):
    logout(request)
    return redirect('core_login')