from django.urls import path
from . import views

app_name = 'department_app'

urlpatterns = [
    path('department/all/', views.DepartmentListAll.as_view(), name='all'),
    path('department/search/', views.DepartmentListByKeyword.as_view()),
    path('department/detail/<pk>', views.DepartmentDetail.as_view(), name='detail'),
    path('department/create/', views.DepartmentCreate.as_view()),
    path('department/update/<pk>', views.DepartmentUpdate.as_view()),
    path('department/delete/<pk>', views.DepartmentDelete.as_view()),
    path('department/new-department/', views.NewDepartment.as_view()),
]
