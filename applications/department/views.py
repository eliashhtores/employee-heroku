from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .models import Department
from .forms import NewDepartmentForm
from applications.person.models import Person
from django.db.models import Q


class DepartmentListAll(ListView):
    template_name = 'department/all.html'
    ordering = ['name']
    paginate_by = 5
    model = Department

    def get_queryset(self):
        keyword = self.request.GET.get('keyword', '')
        return Department.objects.filter(Q(name__icontains=keyword) | Q(short_name__icontains=keyword)).order_by('name')


class DepartmentListByKeyword(ListView):
    template_name = 'department/by_keyword.html'

    def get_queryset(self):
        keyword = self.request.GET.get('keyword')
        if keyword:
            return Department.objects.filter(Q(name__icontains=keyword) | Q(short_name__icontains=keyword))
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


class NewDepartment(FormView):
    template_name = 'department/new_department.html'
    form_class = NewDepartmentForm
    success_url = reverse_lazy('department_app:all')

    def form_valid(self, form):
        department = Department(
            name=form.cleaned_data['name'],
            short_name=form.cleaned_data['short_name']
        )
        department.save()

        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        job_title = form.cleaned_data['job_title']
        Person.objects.create(
            first_name=first_name,
            last_name=last_name,
            job_title=job_title,
            branch='Querétaro',
            department=department,
            email=first_name[0].lower() + '.' + last_name.lower() + '@test.com'
        )
        return super(NewDepartment, self).form_valid(form)
