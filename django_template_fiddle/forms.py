from django import forms
from models import Fiddle
from captcha.fields import CaptchaField

class FiddleForm(forms.ModelForm):
    class Meta:
        model = Fiddle
        fields = '__all__'
