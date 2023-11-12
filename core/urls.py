from django.urls import path
from django.conf.urls import include
from .views import (
    home, 
    rotas,
    cadastro, 
    pagina_de_login, 
    pagina_de_logout)

urlpatterns = [
    path('', home, name='core_home'),
    path('rotas/', rotas, name='core_rotas'),
    path('cadastrar/', cadastro, name='core_cadastro'),
    path('login/', pagina_de_login, name='core_login'),
    # path('home/',views.HomePage, name='home'),
    path('logout/', pagina_de_logout, name='core_logout'),
]
