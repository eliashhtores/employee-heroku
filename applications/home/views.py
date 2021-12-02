from django.views.generic import (
    TemplateView, 
    ListView, 
    CreateView
)
from .models import Home

from .forms import HomeForm

class HomeView(TemplateView):
    template_name = 'home/home.html'


class HomeListView(ListView):
    template_name = 'home/home_list.html'
    context_object_name = 'numList'
    queryset = ['item1', 'item2', 'item3']


class ListHome(ListView):
    template_name = 'home/home_list_test.html'
    model = Home
    context_object_name = 'homeList'


class CreateHome(CreateView):
    template_name = 'home/add.html'
    model = Home
    form_class = HomeForm
    success_url = '/home/list_test'
