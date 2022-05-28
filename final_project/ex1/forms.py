from django import forms
from ex1.models import Signup_Form


class SignupForm(forms.ModelForm):
    class Meta:
        model = Signup_Form
        fields = "__all__"
        widgets = {
            'password': forms.PasswordInput(),
        }