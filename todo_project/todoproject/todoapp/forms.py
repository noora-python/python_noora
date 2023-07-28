from django import forms

from todoapp.models import Task


class TodoForms(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'priority', 'date']