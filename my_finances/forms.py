from datetime import date
from django import forms
from .models import Income


class DateInput(forms.DateInput):
    input_type = 'date'


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['value', 'date', 'income_type', 'recurrent', 'recurrency_interval',  'recurrency_time', 'comment']

    value = forms.DecimalField()
    date = forms.DateField(widget=DateInput, initial=date.today())
    income_type = forms.ChoiceField(choices=Income.IncomeTypes.choices)
    recurrent = forms.BooleanField(required=False)
    recurrency_interval = forms.ChoiceField(choices=Income.RepetitionInterval.choices, initial=1)
    recurrency_time = forms.IntegerField(initial=0)
    comment = forms.CharField(max_length=255, required=False, widget=forms.Textarea)
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance
