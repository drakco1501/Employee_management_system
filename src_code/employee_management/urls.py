from django.urls import path
from .import views

urlpatterns = [
    path('', views.employees, name='emp_index'),
    path('all_employees/', views.all_employees, name='all_employees'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('employees_alter/', views.employees_alter, name='employees_alter'),
    path('update_employee/<str:pk>', views.update_employee, name='update_employee'),
    path('delete_employee/<int:pk>/', views.delete_employee, name='delete_employee'),
]
