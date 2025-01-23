from django.forms import ModelForm
from django import forms
from .models import *
class BloggingForm(forms.ModelForm):

    class Meta:
        model=Blogging
        fields='__all__'

class CategoryForm(forms.ModelForm):
    
    class Meta:
        model=Category
        fields='__all__'
        
        


