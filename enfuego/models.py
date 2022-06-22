from django.db import models


def database_initialization():

    teams = ["CSA", "CSB", "EB", "ECA", "ECB", "EEE", "MECH"]

    if not Teams.objects.all():

        for i in teams:
            t = Teams(team=i)
            t.save()
            p = PointTable(
                team=Teams.objects.get(team=i), 
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

# Create your models here.


# model for the team
class Teams(models.Model):
    class Meta:
        ordering = ['team']        # this is for setting the default ordering for the rows of the relation

    team = models.CharField(max_length=5, verbose_name="Team Name", blank=False, null=False, primary_key=True)

    def __str__(self):
        return str(self.team)


# players name , team , goal scored, (player tag)
class Players(models.Model):
    class Meta:
        ordering = ['-goalsscored']
    
    name = models.CharField(max_length=25, verbose_name="Player Name", blank=False, null=False)
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
    goalsscored = models.PositiveIntegerField(verbose_name="Goals Scored")
    # playertag

    def __str__(self):
        return str(self.team + "-" + self.name)


# model for all fixtures
class Fixtures(models.Model):
    class Meta:
        ordering = ['matchnumber']

    matchnumber = models.PositiveIntegerField(verbose_name="match number")
    teama = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name="teama")
    teamb = models.ForeignKey(Teams, on_delete= models.CASCADE, related_name="teamb")
    scorea = models.PositiveIntegerField(verbose_name="teama score", blank=True, null=True)
    scoreb = models.PositiveIntegerField(verbose_name="teamb score", blank=True, null=True)
    date = models.DateField(verbose_name="match date")
    finished = models.BooleanField()

    def __str__(self):
        return str(str(self.teama) + "vs" + str(self.teamb))


# pointtable
class PointTable(models.Model):
    class Meta:
        ordering = ['-points', '-goaldifference', '-goalsscored']
    team = models.OneToOneField(Teams, on_delete=models.CASCADE, primary_key=True)
    gamesplayed = models.PositiveIntegerField(verbose_name="games played")
    gameswon = models.PositiveIntegerField(verbose_name="games won")
    gamesdraw = models.PositiveIntegerField(verbose_name="games draw")
    gameslost = models.PositiveIntegerField(verbose_name="games lost")
    goalsscored = models.PositiveIntegerField(verbose_name="goals scored")
    goalsconceded = models.PositiveIntegerField(verbose_name="goals conceded")
    goaldifference = models.IntegerField(verbose_name="goal difference")
    points = models.PositiveIntegerField(verbose_name="points")

    def __str__(self):
        return str(self.team)


# Guidelines
class GuideLines(models.Model):
    rule = models.TextField(verbose_name='rule')

    def __str__(self):
        return str(self.rule)
