from django.shortcuts import render, redirect
from .models import UserProfile, Deposito


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

