from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Usuario, Inmueble


class RegistroForm(UserCreationForm):

    nombres = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )

    apellidos = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )

    rut = forms.CharField(
        max_length=12,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )

    direccion = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )

    telefono = forms.CharField(
        max_length=12,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )

    correo_electronico = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control'
        })
    )

    tipo_usuario = forms.ChoiceField(
        choices=Usuario.TIPOS_USUARIO,
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control'
        })

    class Meta:
        model = User
        fields = [
            'username',
            'nombres',
            'apellidos',
            'rut',
            'direccion',
            'telefono',
            'correo_electronico',
            'tipo_usuario',
            'password1',
            'password2',
        ]
        
class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = [
            'nombres',
            'apellidos',
            'rut',
            'direccion',
            'telefono',
            'correo_electronico',
            'tipo_usuario',
        ]

        widgets = {
            'nombres': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'apellidos': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'rut': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'correo_electronico': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
            'tipo_usuario': forms.Select(attrs={
                'class': 'form-select'
            }),
        }

class InmuebleForm(forms.ModelForm):

    class Meta:
        model = Inmueble
        fields = [
            'nombre',
            'descripcion',
            'm2_construidos',
            'm2_totales',
            'estacionamientos',
            'habitaciones',
            'banos',
            'direccion',
            'comuna',
            'tipo_inmueble',
            'precio_mensual',
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'm2_construidos': forms.NumberInput(attrs={'class': 'form-control'}),
            'm2_totales': forms.NumberInput(attrs={'class': 'form-control'}),
            'estacionamientos': forms.NumberInput(attrs={'class': 'form-control'}),
            'habitaciones': forms.NumberInput(attrs={'class': 'form-control'}),
            'banos': forms.NumberInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'comuna': forms.Select(attrs={'class': 'form-select'}),
            'tipo_inmueble': forms.Select(attrs={'class': 'form-select'}),
            'precio_mensual': forms.NumberInput(attrs={'class': 'form-control'}),
        }