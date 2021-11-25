from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('home_list/', views.HomeListView.as_view(), name='home_list'),
    path('home_list_test/', views.ListHome.as_view(), name='home_list_test'),
    path('add/', views.CreateHome.as_view(), name='add'),
]
