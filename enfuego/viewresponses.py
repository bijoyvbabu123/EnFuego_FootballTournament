from . import models
from django.http import JsonResponse


# result for pointtable. directly pass to JsonResponse with safe=False
def point_table_response():
    data = list(models.PointTable.objects.all().values())
    
    # data2 = JsonResponse(data, safe=False)

    # print("-----------------", type(data))
    # print(data)

    # print("-----------------", type(data2))
    # print(data2)

    return data


# results for complete fixtures.
def complete_fixtures_response():
    # data = list(models.Fixtures.objects.all().values())   # working but with "id"
    data = list(models.Fixtures.objects.all().values('matchnumber', 'teama_id', 'teamb_id', 'scorea', 'scoreb', 'date', 'finished'))

    # print("----------------", type(data))
    # print(data)


    return data


# result for goal scorers
def goal_scorers_response():
    data = list(models.Players.objects.filter(goalsscored__gt=0).values('name', 'team_id', 'goalsscored'))
    return data


# guidelines result
def guideline_reponse():
    data = list(models.GuideLines.objects.all().values('rule'))
    return data
    