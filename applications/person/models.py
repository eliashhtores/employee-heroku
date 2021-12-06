from django.db import models
from applications.department.models import Department
from ckeditor.fields import RichTextField


class Skill(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = ('Habilidad')
        verbose_name_plural = ('Habilidades')

    def __str__(self):
        return self.name


class Person(models.Model):
    BRANCH_CHOICES = (
        ('Querétaro', 'Querétaro'),
        ('CDMX', 'CDMX'),
        ('Celaya', 'Celaya'),
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    branch = models.CharField(max_length=10, choices=BRANCH_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill)
    email = models.EmailField(max_length=254, blank=True)
    resume = RichTextField(default='', null=True, blank=True)
    # image = models.ImageField(max_length=100, upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ('Persona')

    def __str__(self):
        return self.first_name + ' ' + self.last_name
