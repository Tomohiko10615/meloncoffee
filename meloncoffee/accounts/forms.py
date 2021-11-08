# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

#from django.core.exceptions import ValidationError

class DateInput(forms.DateInput):
    input_type = 'date'

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'first_name', 'second_name', 'email', 'phone', 'birthday',) # new

        widgets = {
        'username': forms.fields.TextInput(attrs={'placeholder': 'Nombre de usuario'}),
        'first_name': forms.fields.TextInput(attrs={'placeholder': 'Nombre'}),
        'second_name': forms.fields.TextInput(attrs={'placeholder': 'Apellido'}),
        'email': forms.fields.TextInput(attrs={'placeholder': 'Email'}),
        'phone': forms.fields.TextInput(attrs={'placeholder': 'Número telefónico'}),
        'birthday': forms.fields.DateInput(attrs={'placeholder': 'Fecha de nacimiento', 'onblur': "(this.type='text')", 'onfocus': '(this.type="date")'}),
        'password': forms.fields.TextInput(attrs={'placeholder': 'Contraseña'}),
    }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Contraseña'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Confirmar contraseña'})

    """
    def clean(self):
       email = self.cleaned_data.get('email')
       if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("El email ingresado ya sido registrado")
       return self.cleaned_data
    """
    

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'second_name', 'email', 'phone', 'birthday',) # new

        widgets = {
        'username': forms.fields.TextInput(attrs={'placeholder': 'Nombre de usuario'}),
        'first_name': forms.fields.TextInput(attrs={'placeholder': 'Nombre'}),
        'second_name': forms.fields.TextInput(attrs={'placeholder': 'Apellido'}),
        'email': forms.fields.EmailInput(attrs={'placeholder': 'Email'}),
        'phone': forms.fields.TextInput(attrs={'placeholder': 'Número telefónico'}),
        'birthday': forms.fields.DateInput(attrs={'placeholder': 'Fecha de nacimiento', 'onblur': "(this.type='text')", 'onfocus': '(this.type="date")'}),
        'password': forms.fields.TextInput(attrs={'placeholder': 'Contraseña'}),
    }

    """
    def clean(self):
       email = self.cleaned_data.get('email')
       if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("El email ingresado ya sido registrado")
       return self.cleaned_data
    """

"""
class FormContactForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields= ["nombre", "apellido", "email", "password", "phone", "birthday"]
"""