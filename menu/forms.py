from django import forms
#from django.forms.extras.widgets import SelectDateWidget

from .models import Menu, Item, Ingredient

class MenuForm(forms.ModelForm):

    class Meta:
        model = Menu
        fields = ['season', 'items', 'expiration_date']
        exclude = ['created_date',]
        
    def clean(self):
        data = self.cleaned_data
        items = data.get('items')
        
        if not items:
            raise forms.ValidationError(
                'A menu must have at least one item.'
            )
        return data