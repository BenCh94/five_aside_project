from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.
class Player(models.Model):
    user_id = models.ForeignKey('accounts.User', related_name='players')
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    # need to create images folder and settings to upload files, could use aws image hosting.
    image = models.ImageField(upload_to='images', blank=True, null=True)
    date_added = models.DateTimeField(default=timezone.now)
    games_played = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)

    def add(self):
        self.save()