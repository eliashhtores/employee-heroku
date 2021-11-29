from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)
    short_name = models.CharField(max_length=50, blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = ('Departamento')
        # verbose_name_plural = ('Áreas de la empresa')
        ordering = ['name']
        unique_together = ('name', 'short_name')

    def __str__(self):
        return self.name
