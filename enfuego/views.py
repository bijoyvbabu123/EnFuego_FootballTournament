from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from . import models

from . import viewresponses

# Create your views here.


# this view is for the landing page which shows the current point table
def point_table_view(request):

    # this is the landing page, check if all teams are there in the teams and pointtable database. Create a function for that purpose in models.py
    models.database_initialization()

    data = viewresponses.point_table_response()
    """This returns an array of objects with keys { team_id, gamesplayed, gameswon, gamesdraw, 
    gameslost, goalsscored, goalsconceded, goaldifference, points }"""

    # return HttpResponse("this is point table view")
    return JsonResponse(data, safe=False)


# this view is for the page that shows the complete fixtures
def complete_fixtures_view(request):

    data = viewresponses.complete_fixtures_response()
    """This returns array of objects with keys {matchnumber, teama_id, teamb_id,
    scorea, scoreb, date, finished}"""

    # return HttpResponse("this is fixtures view")

    return JsonResponse(data, safe=False)


# this view is for the specific team fixtures
def specific_fixtures_view(request):

    t = request.GET.get('team')

    data = viewresponses.specific_fixtures_response(t)
    """This returns array of objects with keys {matchnumber, teama_id, teamb_id,
    scorea, scoreb, date, finished}"""

    # return HttpResponse("this is specific team fixtures view")

    return JsonResponse(data, safe=False)



# this view is for the table of goal scorers 
def goal_scorers_view(request):

    data = viewresponses.goal_scorers_response()
    """returns array of objects with keys {name, team_id, goalsscored}"""

    # return HttpResponse("this is goal scorers view")
    return JsonResponse(data, safe=False)


# this view is for the guidelines
def guidelines_view(request):

    data = viewresponses.guideline_reponse()
    """returns array of objects with keys {rule}"""

    # return HttpResponse("this is guideline view")
    return JsonResponse(data, safe=False)

