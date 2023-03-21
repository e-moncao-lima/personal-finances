from django import forms
from .models import Income


class DateInput(forms.DateInput):
    input_type = 'date'


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['value', 'date', 'income_type', 'recurrent', 'recurrency_interval', 'recurrency_time']
        widgets = {'date': DateInput()}
