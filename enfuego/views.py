from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# this view is for the landing page which shows the current point table
def point_table_view(request):
    return HttpResponse("this is point table view")


# this view is for the page that shows the complete fixtures
def complete_fixtures_view(request):
    return HttpResponse("this is fixtures view")


# this view is for the specific team fixtures
def specific_fixtures_view(request):
    return HttpResponse("this is specific team fixtures view")


# this view is for the table of goal scorers 
def goal_scorers_view(request):
    return HttpResponse("this is goal scorers view")


# this view is for the guidelines
def guidelines_view(request):
    return HttpResponse("this is guideline view")

