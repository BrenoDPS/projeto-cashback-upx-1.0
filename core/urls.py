from django.urls import path
from django.conf.urls import include
from .views import home, rotas

urlpatterns = [
    path('', home, name='core_home'),
    path('rotas', rotas, name='core_rotas')
]
