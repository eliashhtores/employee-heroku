from django.contrib import admin
from .models import Department


admin.site.register(Department)
# class DepartmentAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'description', 'image', 'created_at', 'updated_at')
#     list_display_links = ('id', 'title', 'description', 'image', 'created_at', 'updated_at')
#     list_filter = ('created_at', 'updated_at')
#     search_fields = ('title', 'description')
