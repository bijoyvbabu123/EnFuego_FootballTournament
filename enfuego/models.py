from django.db import models

# Create your models here.


# model for the team
class Teams(models.Model):
    team = models.CharField(max_length=5, verbose_name="Team Name", blank=False, null=False, primary_key=True)

    def __str__(self):
        return str(self.team)


# players name , team , goal scored, (player tag)
class Players(models.Model):
    name = models.CharField(max_length=25, verbose_name="Player Name", blank=False, null=False)
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
    goalsscored = models.PositiveIntegerField(verbose_name="Goals Scored")
    # playertag

    def __str__(self):
        return str(self.team + "-" + self.name)


# model for all fixtures
class Fixtures(models.Model):
    matchnumber = models.PositiveIntegerField(verbose_name="match number")
    teama = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name="teama")
    teamb = models.ForeignKey(Teams, on_delete= models.CASCADE, related_name="teamb")
    scorea = models.PositiveIntegerField(verbose_name="teama score")
    scoreb = models.PositiveIntegerField(verbose_name="teamb score")
    date = models.DateField(verbose_name="match date")
    finished = models.BooleanField()

    def __str__(self):
        return str(self.teama + "vs" + self.teamb)


# pointtable
class PointTable(models.Model):
    team = models.OneToOneField(Teams, on_delete=models.CASCADE, primary_key=True)
    gamesplayed = models.PositiveIntegerField(verbose_name="games played")
    gameswon = models.PositiveIntegerField(verbose_name="games won")
    gamesdraw = models.PositiveIntegerField(verbose_name="games draw")
    gameslost = models.PositiveIntegerField(verbose_name="games lost")
    goaldifference = models.IntegerField(verbose_name="goal difference")
    points = models.PositiveIntegerField(verbose_name="points")

    def __str__(self):
        return str(self.team)


# Guidelines
class GuideLines(models.Model):
    rule = models.TextField(verbose_name='rule')

    def __str__(self):
        return str(self.rule)
