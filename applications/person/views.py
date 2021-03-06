from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Person
from .forms import PersonForm
from django.db.models import Q


class PersonListAll(ListView):
    template_name = 'person/all.html'
    paginate_by = 10
    model = Person

    def get_queryset(self):
        keyword = self.request.GET.get('keyword', '')
        return Person.objects.filter(Q(first_name__icontains=keyword) | Q(last_name__icontains=keyword)).order_by('first_name')


class PersonAdmin(ListView):
    template_name = 'person/admin.html'
    paginate_by = 10
    model = Person

    def get_queryset(self):
        keyword = self.request.GET.get('keyword', '')
        return Person.objects.filter(Q(first_name__icontains=keyword) | Q(last_name__icontains=keyword)).order_by('first_name')


class PersonListByDepartment(ListView):
    template_name = 'person/filtered.html'

    def get_queryset(self):
        return Person.objects.filter(department__id=self.kwargs['id']).order_by('first_name')


class PersonListByBranch(ListView):
    template_name = 'person/filtered.html'

    def get_queryset(self):
        return Person.objects.filter(branch__icontains=self.kwargs['branch'])


class PersonListByKeyword(ListView):
    template_name = 'person/by_keyword.html'

    def get_queryset(self):
        keyword = self.request.GET.get('keyword')
        print(keyword)
        if keyword:
            return Person.objects.filter(Q(first_name__icontains=keyword) | Q(last_name__icontains=keyword))
        return


class PersonBySkills(ListView):
    template_name = 'person/by_skills.html'
    context_object_name = 'skills'

    def get_queryset(self):
        return Person.objects.get(id=self.kwargs['id']).skills.all()


class PersonDetail(DetailView):
    model = Person
    template_name = 'person/detail.html'


class SuccessView(TemplateView):
    template_name = 'person/success.html'


class PersonCreate(CreateView):
    template_name = 'person/create.html'
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('person_app:all')

    def form_valid(self, form):
        person = form.save(commit=False)
        person.email = person.first_name[0].lower(
        ) + '.' + person.last_name.lower() + '@test.com'
        person.save()
        return super(PersonCreate, self).form_valid(form)


class PersonUpdate(UpdateView):
    template_name = 'person/update.html'
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('person_app:admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        # print(request.POST)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        return super().form_valid(form)


class PersonDelete(DeleteView):
    model = Person
    template_name = 'person/delete.html'
    success_url = reverse_lazy('person_app:admin')


class StartView(TemplateView):
    template_name = 'start.html'
