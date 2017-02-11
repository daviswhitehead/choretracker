from django import forms

from .models import Chore


class ChoreForm(forms.ModelForm):

    class Meta:
        model = Chore
        fields = ('name', 'value',)
