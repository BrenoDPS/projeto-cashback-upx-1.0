from django.contrib import admin
from .models import (
    UserProfile, 
    Deposito, 
    Profile, 
)


admin.site.register(Deposito)
admin.site.register(Profile)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'display_valor', 'display_cashback')  # Adicione 'cashback' à lista de exibição

    def display_valor(self, obj):
        return obj.deposito.valor

    def display_cashback(self, obj):
        return obj.calcula_cashback

    display_valor.short_description = 'Valor do Depósito'  # Defina um nome mais amigável para a coluna
    display_cashback.short_description = 'Cashback'  # Defina um nome mais amigável para a coluna

''' def get_queryset(self, request):
        return super().get_queryset(request).annotate(cashback=models.ExpressionWrapper(
            models.F('deposito__valor') * 0.15, output_field=models.DecimalField()
        ))

    def display_cashback(self, obj):
        return obj.cashback'''


admin.site.register(UserProfile, UserProfileAdmin)