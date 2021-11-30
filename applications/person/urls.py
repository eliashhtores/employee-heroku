from django.urls import path
from . import views

app_name = 'person_app'

urlpatterns = [
    path('person-all/', views.PersonListAll.as_view()),
    path('person-list-by-department/<short_name>/', views.PersonListByDepartment.as_view()),
    path('person-list-by-branch/<branch>/', views.PersonListByBranch.as_view()),
    path('person-search/', views.PersonListByKeyword.as_view()),
    path('person-by-skill/<id>', views.PersonBySkills.as_view()),
    path('person-detail/<pk>', views.PersonDetail.as_view()),
    path('person-create/', views.PersonCreate.as_view()),
    path('person-success/', views.SuccessView.as_view(), name='success'),
]
