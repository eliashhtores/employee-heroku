from django import forms


class NewDepartmentForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    job_title = forms.CharField(max_length=100)
    name = forms.CharField(max_length=255)
    short_name = forms.CharField(max_length=50)
