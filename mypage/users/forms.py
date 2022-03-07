
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Profile


class SignUpForm(UserCreationForm):
    
    first_name = forms.CharField(label="Nombre",max_length=100,required=True)
    last_name = forms.CharField(label="Apellido",max_length=100, required=False)
    email = forms.EmailField(label="Correo Electronico",required=True)

    class Meta:
        model = User
        help_texts = {
            'username': None,
        }
        
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None