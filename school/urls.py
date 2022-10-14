from django.urls import path, include
from . import views

urlpatterns = [
    path('test/', views.test, name='test'),
    path('school/list/', views.school_list, name='school_list'),
    path('school/add/', views.school_add, name='school_add'),
    path('school/detail/<int:school_id>/', views.school_detail, name='school_detail'),
    path('school/edit/<int:school_id>/', views.school_edit, name='school_edit'),
    path('school/delete/<int:school_id>/', views.school_delete, name='school_delete'),

]