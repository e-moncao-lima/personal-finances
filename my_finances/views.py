from django.urls import reverse_lazy, reverse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from .models import Income
from .forms import IncomeForm


# Create your views here.
class IncomeListView(ListView):
    model = Income
    paginate_by = 100
    # template_name = 'my_finances/income_list.html'
    # queryset = Income.objects.all()
    # context_object_name = 'income_list'


class IncomeDetailView(DetailView):
    model = Income


class IncomeCreateView(CreateView):
    model = Income
    form_class = IncomeForm

    def get_success_url(self) -> str:
        messages.success(self.request, 'Income created successfully!')
        return reverse_lazy('my_finances:income_list')


class IncomeUpdateView(UpdateView):
    model = Income
    form_class = IncomeForm
    
    def get_success_url(self) -> str:
        messages.success(self.request, 'Income updated successfully!')
        return reverse('my_finances:income_detail', kwargs={'pk': self.object.pk})


class IncomeDeleteView(DeleteView):
    model = Income
    
    def get_success_url(self) -> str:
        messages.success(self.request, 'Income deleted successfully!')
        return reverse_lazy('my_finances:income_list')
