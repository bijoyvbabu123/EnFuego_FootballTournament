from django.contrib import admin

from . import models

# Register your models here.


# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['name', 'price', 'available']
# admin.site.register(models.Product, ProductAdmin)


class TeamsAdmin(admin.ModelAdmin):
    list_display = ['team']

class PlayersAdmin(admin.ModelAdmin):
    list_display = ['name', 'team', 'goalsscored']

class FixturesAdmin(admin.ModelAdmin):
    list_display = ['matchnumber', 'teama', 'teamb', 'scorea', 'scoreb', 'date', 'finished']

class PointTableAdmin(admin.ModelAdmin):
    list_display = ['team', 'gamesplayed', 'gameswon', 'gamesdraw', 'gameslost', 'goaldifference', 'points']

class GuideLinesAdmin(admin.ModelAdmin):
    list_display = ['rule']



admin.site.register(models.Teams, TeamsAdmin)
admin.site.register(models.Players, PlayersAdmin)
admin.site.register(models.Fixtures, FixturesAdmin)
admin.site.register(models.PointTable, PointTableAdmin)
admin.site.register(models.GuideLines, GuideLinesAdmin)