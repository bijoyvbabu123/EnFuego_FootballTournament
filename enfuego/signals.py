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
    print("-------------update function is called-------------")



@receiver(post_save, sender=models.Fixtures)
def update_pointtable_on_saving(sender, **kwargs):
    update_pointtable()

@receiver(post_delete, sender=models.Fixtures)
def update_pointtable_on_delete(sender, **kwargs):
    update_pointtable()
