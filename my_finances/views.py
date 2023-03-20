from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Income


# Create your views here.
class IncomeListView(ListView):
    model = Income
    paginate_by = 100


class IncomeCreateView(CreateView):
    model = Income
    fields = ['value', 'date', 'income_type', 'recurrent', 'recurrency_interval', 'recurrency_time']
    success_url = reverse_lazy('my_finances.income_list')
