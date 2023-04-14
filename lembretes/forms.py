from django import forms

class criar_lembrete(forms.Form):
    titulo = forms.CharField(max_length=100)
    texto = forms.CharField(widget=forms.Textarea)