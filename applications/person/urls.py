from django.urls import path
from . import views

app_name = 'person_app'

urlpatterns = [
    path('', views.StartView.as_view(), name='start'),
    path('person/all/', views.PersonListAll.as_view(), name='all'),
    path('person/admin/', views.PersonAdmin.as_view(), name='admin'),
    path('person/list-by-department/<id>/',
         views.PersonListByDepartment.as_view(), name='list_by_department'),
    path('person/list-by-branch/<branch>/',
         views.PersonListByBranch.as_view()),
    path('person/search/', views.PersonListByKeyword.as_view()),
    path('person/by-skill/<id>', views.PersonBySkills.as_view()),
    path('person/detail/<pk>', views.PersonDetail.as_view(), name='detail'),
    path('person/create/', views.PersonCreate.as_view(), name='create'),
    path('person/success/', views.SuccessView.as_view(), name='success'),
    path('person/update/<pk>', views.PersonUpdate.as_view(), name='update'),
    path('person/delete/<pk>', views.PersonDelete.as_view(), name='delete'),
]
