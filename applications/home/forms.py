from django import forms
from .models import Home

class HomeForm(forms.ModelForm):

    class Meta:
        model = Home
        fields = ('__all__')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add your title'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')

        if quantity < 0:
            raise forms.ValidationError("Quantity must be greater than 0")
        return quantity
