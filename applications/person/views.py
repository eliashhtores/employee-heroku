from django.views.generic import TemplateView


class PersonView(TemplateView):
    template_name = 'person.html'
