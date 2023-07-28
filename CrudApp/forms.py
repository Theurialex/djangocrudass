from django import forms
from CrudApp.models import Students


class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['firstname', 'lastname', 'email']
