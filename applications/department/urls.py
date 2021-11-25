from django.urls import path


def fromDepartment(self):
    print('Hello from department')

urlpatterns = [
    path('department/', fromDepartment),
]
