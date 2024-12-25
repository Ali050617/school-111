from django.urls import path
from . import views

app_name = 'teachers'


urlpatterns = [
    path('student_list/', views.teacher_list, name='teacher_list'),
    path('student_create/', views.teacher_create, name='teacher_create'),
    path('student_update/<int:pk>/', views.teacher_update, name='teacher_update'),
    path('student_detail/<int:pk>/', views.teacher_detail, name='teacher_detail'),
    path('students_delete/<int:pk>/', views.teacher_delete, name='teacher_delete')
]