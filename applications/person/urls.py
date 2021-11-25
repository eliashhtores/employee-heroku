from django.urls import path


def fromPerson(self):
    print('Hello from person')

urlpatterns = [
    path('person/', fromPerson),
]
