from django.views.generic import (
    TemplateView, 
    ListView, 
    CreateView
)
from .models import Home

class HomeView(TemplateView):
    template_name = 'home.html'


class HomeListView(ListView):
    template_name = 'home_list.html'
    context_object_name = 'numList'
    queryset = ['item1', 'item2', 'item3']


class ListHome(ListView):
    template_name = 'home_list_test.html'
    model = Home
    context_object_name = 'homeList'


class CreateHome(CreateView):
    template_name = 'add.html'
    model = Home
    fields = ['title', 'description', 'quantity']
    success_url = '/home_list_test'
