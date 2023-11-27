from .models import Socios
from django import forms

class SociosForm(forms.ModelForm):
    ESTADOS = [('activo', 'ACTIVO'), ('inactivo', 'INACTIVO'), ('bloqueado', 'BLOQUEADO')]
    TIPO_SEXO = [('hombre', 'HOMBRE'), ('mujer', 'MUJER'), ('otro', 'OTRO')]

    nombreSocio = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=80,
        required=True,
        label='Nombre del Socio',
    )
    fechaIncorporacion = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}), label='Fecha incorporacion (yyyy-mm-dd)')
    anioNacimiento = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}), label='Año nacimiento (yyyy-mm-dd)')
    telefono = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=20, required=True)
    correoElectronico = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), required=True,label='Correo electronico')
    sexo = forms.CharField(widget=forms.Select(choices=TIPO_SEXO, attrs={'class': 'form-select'}), required=True)
    estado = forms.CharField(widget=forms.Select(choices=ESTADOS, attrs={'class': 'form-select'}), required=True)
    observacion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = Socios
        fields = ['nombreSocio', 'fechaIncorporacion', 'anioNacimiento', 'telefono', 'correoElectronico', 'sexo', 'estado', 'observacion']
    
    def clean(self):
        cleaned_data = super().clean()
        nombre_socio = cleaned_data.get('nombreSocio')

        if len(nombre_socio) >= 80:
            raise forms.ValidationError("El nombre no puede pasar los 80 caracteres")

        return cleaned_data