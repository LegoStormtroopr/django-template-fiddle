from django import forms
from models import Fiddle

class FiddleForm(forms.ModelForm):
    class Meta:
        model = Fiddle
        fields = '__all__'