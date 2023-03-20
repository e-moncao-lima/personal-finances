from django.urls import path
from . import views


app_name = 'my_finances'


urlpatterns = [
    path('income_list/', views.IncomeListView.as_view(), name='income_list'),
    path('income_create/', views.IncomeCreateView.as_view(), name='income_create'),
]
