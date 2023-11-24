from django.shortcuts import render, redirect, HttpResponse
from .models import UserProfile, Deposito
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm
    

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


class MyProfile(LoginRequiredMixin, View):

    template_name = 'core/profile.html'

    @login_required
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def get(self, request):
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        
        return render(request, 'core/profile.html', context)
    
    def post(self,request):
        user_form = UserUpdateForm(
            request.POST, 
            instance=request.user
        )
        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            
            messages.success(request,'Your profile has been updated successfully')
            
            return redirect('core_profile')
        else:
            context = {
                'user_form': user_form,
                'profile_form': profile_form
            }
            messages.error(request,'Error updating you profile')
            
            return render(request, 'core/profile.html', context)
        

def minha_view(request):
    # Recupera o UserProfile associado ao usuário atual
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        # Obtenha o valor do depósito do formulário
        valor_deposito = float(request.POST.get('valor_deposito', 0.0))

        # Atualize o valor do depósito no UserProfile
        user_profile.deposito.valor = valor_deposito
        user_profile.deposito.save()

    # Obtém o valor de cashback
    cashback = user_profile.calcula_cashback

    # Passa o valor de cashback para o contexto
    context = {'cashback': cashback}

    # Renderiza o arquivo HTML com o contexto
    return render(request, 'core/profile.html', context)
