from django.db import models
from applications.department.models import Department

class Person(models.Model):
    QRO = 'querétaro'
    CDMX = 'cdmx'
    CELAYA = 'Celaya'
    BRANCH_CHOICES = (
        (QRO, 'Querétaro'),
        (CDMX, 'CDMX'),
        (CELAYA, 'Celaya'),
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    branch = models.CharField(max_length=10, choices=BRANCH_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    # image = models.ImageField(max_length=100, upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' +  self.last_name
