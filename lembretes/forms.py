from django import forms
from .models import lembrete

class criar_lembrete(forms.ModelForm):
    class Meta:
        model = lembrete
        fields = ['title', 'text']