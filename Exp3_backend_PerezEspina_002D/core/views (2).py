from django.shortcuts import render,redirect
from .models import usuario
from .forms import UsuarioForm
# Create your views here.
def index(request):
    return render(request,'index.html')
def galeria(request):
    return render(request,'Galeria.html')

def login_registro(request):
    if request.method=='POST': 
        usuario_form = UsuarioForm(request.POST)
        if usuario_form.is_valid():
            usuario_form.save()    #save() reemplaza al insert
            return redirect('index')
    else: 
        usuario_form=UsuarioForm()
    return render(request, 'core/login_registro.html', 
    {'usuario_form':usuario_form})




 


