from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return self.user.username
    

    def calcular_cashback(self, valor_deposito):
        cashback_percentage = 0.15
        cashback = valor_deposito * cashback_percentage
        self.saldo += cashback
        self.save()
        return cashback


class Deposito(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} - {self.valor} reais"
    



