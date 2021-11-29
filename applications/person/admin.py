from django.contrib import admin
from .models import Person, Skill


admin.site.register(Skill)


class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'job_title', 'department', 'branch', 'full_name')
    search_fields = ('first_name', 'last_name', 'job_title', 'department__name', 'branch')
    list_filter = ('job_title', 'department', 'branch')
    ordering = ('first_name',)
    filter_horizontal = ('skills',)

    def full_name(self, obj):
        return obj.first_name + ' ' + obj.last_name

admin.site.register(Person, PersonAdmin)
