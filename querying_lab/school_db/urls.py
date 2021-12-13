from django.urls import path
from . import views


app_name = 'lab'
urlpatterns = [
    path('', views.index, name="index"),
    path('one/', views.problem_one, name="one"),
    path('two/', views.problem_two, name="two"),
    path('three/', views.problem_three, name="three"),
    path('four/', views.problem_four, name="four"),
    path('five/', views.problem_five, name="five"),
    path('six/', views.problem_six, name="six"),
    path("bonus1/", views.bonus_one, name="bonus1"),
    path("bonus2/", views.bonus_two, name="bonus2"),
    path("bonus3/", views.bonus_three, name="bonus3"),
    path("bonus4/", views.bonus_four, name="bonus4")
]