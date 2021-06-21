from django import forms
from django.forms import ModelForm, fields,widgets
from .models import Producto, usuario,Contacto

class UsuarioForm(ModelForm):
    class Meta:
        model = usuario
        fields = ['NomCompleto','email','direccion','contraseña']
       
        widgets={
            'nomCompleto': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Nombre Completo',
                    'id':'NomCompleto'
                }
            ),
            'email':forms.EmailInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Correo Electronico',
                    'id':'email'
                }
            ),
            'direccion':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Dirección',
                    'id':'direccion'
                }
            ),
            'contraseña':forms.PasswordInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Contraseña',
                    'id':'contraseña'
                }
            )

            
        }
class ContactoForm(forms.ModelForm):



    class Meta:
        model = Contacto
        fields =["nombre", "correo", "tipo_consulta", "mensaje"]
    

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'   

        widgets = {
        "fecha_fabricacion": forms.SelectDateWidget() 
        } 

