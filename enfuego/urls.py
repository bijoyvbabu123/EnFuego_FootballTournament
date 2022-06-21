from django.urls import path
from . import views


app_name = 'enfuego'

urlpatterns = [
    path('pointtable/', views.point_table_view, name='pointtable'),
    path('completefixtures/', views.complete_fixtures_view, name='completefixtures'),
    path('specificfixtures/', views.specific_fixtures_view, name='specificfixtures'),
    path('goalscorers/', views.goal_scorers_view, name='goalscorers'),
    path('guidelines/', views.guidelines_view, name='guidelines'),
]