# this is the conventional way to use signals in django app
# define all the receiver functions here

# ** override ready() in apps.py
#  def ready(self):
#         import enfuego.signals

# ** in installed_apps in settings.py give complete name like 'appname.apps.AppnameConfig'  # derived from apps.py
#             'enfuego.apps.EnfuegoConfig',


from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from . import models


def update_pointtable():
    # print("-------------update function is called-------------") #####################

    teams = ["CSA", "CSB", "EB", "ECA", "ECB", "EEE", "MECH"]

    # resetting the pointtable
    for i in teams:
            t = models.Teams(team=i)
            t.save()
            p = models.PointTable(
                team=models.Teams.objects.get(team=i), 
                gamesplayed=0,
                gameswon=0,
                gamesdraw=0,
                gameslost=0,
                goalsscored=0,
                goalsconceded=0,
                goaldifference=0,
                points=0
            )
            p.save()

    fixtures = models.Fixtures.objects.filter(finished=True)
    for fixture in fixtures:
        # print(fixture, type(fixture))         # model instance
        # print(fixture.teama.team, type(fixture.teama.team))  # string
        # print(fixture.teamb.team, type(fixture.teamb.team))  # fixture.teamb is Team instance
        # print(fixture.scorea, type(fixture.scorea))   # int 
        # print(fixture.scoreb, type(fixture.scoreb))    # int

        # getting individual team objects
        ta = models.PointTable.objects.get(team=fixture.teama)
        tb = models.PointTable.objects.get(team=fixture.teamb)
        # updating gamesplayed
        ta.gamesplayed = ta.gamesplayed+1
        tb.gamesplayed = tb.gamesplayed+1
        # updating gameswon, gameslost, gamesdraw, points
        if(fixture.scorea > fixture.scoreb):
            ta.gameswon = ta.gameswon+1
            ta.points = ta.points+3
            tb.gameslost = tb.gameslost+1
        elif(fixture.scoreb > fixture.scorea):
            tb.gameswon = tb.gameswon+1
            tb.points = tb.points+3
            ta.gameslost = ta.gameslost+1
        else:
            ta.gamesdraw = ta.gamesdraw+1
            ta.points = ta.points+1
            tb.gamesdraw = tb.gamesdraw+1
            tb.points = tb.points+1
        # updating goalsscored, goalsconceded, goaldifference
        ta.goalsscored = ta.goalsscored+fixture.scorea
        ta.goalsconceded = ta.goalsconceded+fixture.scoreb
        ta.goaldifference = ta.goaldifference+fixture.scorea-fixture.scoreb
        tb.goalsscored = tb.goalsscored+fixture.scoreb
        tb.goalsconceded = tb.goalsconceded+fixture.scorea
        tb.goaldifference = tb.goaldifference+fixture.scoreb-fixture.scorea
        # saving the changes
        ta.save()
        tb.save()




@receiver(post_save, sender=models.Fixtures)
def update_pointtable_on_saving(sender, **kwargs):
    update_pointtable()

@receiver(post_delete, sender=models.Fixtures)
def update_pointtable_on_delete(sender, **kwargs):
    update_pointtable()
