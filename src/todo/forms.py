from django import forms
from .models import Todo

class TodoAddForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title',)
        
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control', 'id':'floatingInput', 'placeholder':'my_title' }),
            
        }
        
        
class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'completed')
        # exclude = ('created_date')