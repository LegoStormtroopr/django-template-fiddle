from django import forms
from django_template_fiddle.models import Fiddle
#from captcha.fields import CaptchaField

class FiddleForm(forms.ModelForm):
    class Meta:
        model = Fiddle
        fields = '__all__'
