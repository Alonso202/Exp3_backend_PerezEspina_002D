from django.urls import path
from .views import index,galeria,login_registro


urlpatterns = [
    path ('', index, name="index"),
    path('galeria',galeria, name="galeria"),
    path('login_registro',login_registro, name="login_registro")
]