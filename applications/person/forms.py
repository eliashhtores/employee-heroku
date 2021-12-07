from django import forms
from .models import Person


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = '__all__'
        widgets = {
            # 'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'skills': forms.CheckboxSelectMultiple(),
        }
