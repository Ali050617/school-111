from django.urls import path
from . import views

app_name = 'subjects'


urlpatterns = [
    path('student_list/', views.subject_list, name='subject_list'),
    path('student_create/', views.subject_create, name='subject_create'),
    path('student_update/<int:pk>/', views.subject_update, name='subject_update'),
    path('student_detail/<int:pk>/', views.subject_detail, name='subject_detail'),
    path('students_delete/<int:pk>/', views.subject_delete, name='subject_delete')
]