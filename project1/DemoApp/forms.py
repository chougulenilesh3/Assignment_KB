from .models import UserRegistrationModel
from django import forms

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegistrationModel
        fields = '__all__'

