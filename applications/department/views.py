from django.views.generic import TemplateView


class DepartmentView(TemplateView):
    template_name = 'department.html'
