from django import forms

from .models import Todo

class TodoForm(forms.ModelForm):
    tittle = forms.CharField(max_length = 1000, widget=forms.TextInput(attrs = {
        'id' : 'tittleField', 'placeholder' :  'Enter Tittle'
    }))
    class Meta:
        model = Todo
        fields = ['tittle']