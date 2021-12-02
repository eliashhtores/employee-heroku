from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Department


class DepartmentListAll(ListView):
    template_name = 'department/all.html'
    ordering = ['name']
    model = Department

class DepartmentListByKeyword(ListView):
    template_name = 'department/by_keyword.html'

    def get_queryset(self):
        if self.request.GET.get('keyword'):
            return Department.objects.filter(name__icontains=self.request.GET.get('keyword'))
        return

class DepartmentDetail(DetailView):
    template_name = 'department/detail.html'
    model = Department

class DepartmentCreate(CreateView):
    template_name = 'department/create.html'
    model = Department
    fields = ('__all__')
    success_url = reverse_lazy('department_app:all')

class DepartmentUpdate(UpdateView):
    template_name = 'department/update.html'
    model = Department
    fields = ('__all__')
    success_url = reverse_lazy('department_app:all')

class DepartmentDelete(DeleteView):
    template_name = 'department/delete.html'
    model = Department
    success_url = reverse_lazy('department_app:all')
