from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('habit_home', views.list_habits, name="habit_home"),
    path('habit_detail/<int:pk>/', views.habit_detail, name="habit_detail"),
    path("habit/new", views.add_habit, name="add_habit"),
    
    path('record_detail/<int:pk>/', views.record_detail, name="record_detail"),
    path("record/new", views.add_record, name="add_record"),
]
