from django.views.generic import ListView
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
