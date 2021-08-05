from django import forms
from django.forms import ModelForm, widgets
from .models import Cliente

class ClienteForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = ('correo','celular','nombre','apellidos','tdocumento','documento','tdatos','direccion')
        widgets={
            "correo":forms.widgets.EmailInput(attrs={"class":"form-control","required":"true"}),
            "celular":forms.widgets.TextInput(attrs={"class":"form-control","required":"true"}),
            "nombre":forms.widgets.TextInput(attrs={"class":"form-control","required":"true"}),
            "apellidos":forms.widgets.TextInput(attrs={"class":"form-control","required":"true"}),
            "tdocumento":forms.widgets.Select(attrs={"class":"form-select"}),
            "documento":forms.widgets.TextInput(attrs={"class":"form-control","required":"true"}),
            "tdatos":forms.widgets.CheckboxInput(attrs={"class":"form-check-input","required":"true"}),
            "direccion":forms.widgets.TextInput(attrs={"class":"form-control","required":"true"}),
        }
