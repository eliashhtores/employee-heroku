from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView
from django.urls import reverse_lazy
from .models import Person


class PersonListAll(ListView):
    template_name = 'person/all.html'
    paginate_by = 4
    ordering = ['first_name']
    model = Person

class PersonListByDepartment(ListView):
    template_name = 'person/filtered.html'

    def get_queryset(self):
        return Person.objects.filter(department__short_name__icontains=self.kwargs['short_name'])

class PersonListByBranch(ListView):
    template_name = 'person/filtered.html'

    def get_queryset(self):
        return Person.objects.filter(branch__icontains=self.kwargs['branch'])

class PersonListByKeyword(ListView):
    template_name = 'person/by_keyword.html'

    def get_queryset(self):
        return Person.objects.filter(first_name__icontains=self.request.GET.get('keyword', ' '))

class PersonBySkills(ListView):
    template_name = 'person/by_skills.html'
    context_object_name = 'skills'

    def get_queryset(self):
        return Person.objects.get(id=self.kwargs['id']).skills.all()

class PersonDetail(DetailView):
    model = Person
    template_name = 'person/detail.html'
    context_object_name = 'employee'

class SuccessView(TemplateView):
    template_name = 'person/success.html'

class PersonCreate(CreateView):
    template_name = 'person/create.html'
    model = Person
    fields = ('__all__')
    # success_url = '/person-all/'
    success_url = reverse_lazy('person_app:success')

    def form_valid(self, form):
        person = form.save(commit=False)
        person.email = person.first_name[0].lower() + '.' + person.last_name.lower() + '@test.com'
        person.save()
        return super(PersonCreate, self).form_valid(form)

class PersonUpdate(UpdateView):
    template_name = 'person/update.html'
    model = Person
    fields = ('__all__')
    success_url = '/person-all/'
    # success_url = reverse_lazy('person_app:success')
