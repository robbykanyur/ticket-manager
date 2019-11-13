from django.db import models
import math

class League(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=20)

    def __str__(self):
        return self.abbreviation


class Team (models.Model):
    location = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=20)
    league = models.ForeignKey(League, null=True, on_delete=models.SET_NULL, 
                               related_name="team")
    championship_odds = models.IntegerField(default=0)

    def display_name(self):
        return ("%s %s" % (self.location, self.nickname))

    def __str__(self):
        return self.display_name()


class Game (models.Model):
    team = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL)
    opponent = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL, 
                                 related_name="+")
    date = models.DateTimeField(null=True)

    def date_only(self):
        return self.date.strftime("%x")

    def time_only(self):
        return self.date.strftime("%X")

    def game_quality(self):
        return self.team.championship_odds * self.opponent.championship_odds

    def __str__(self):
        formatted_date = self.date.strftime("%x")
        return ("%s at %s on %s" % (self.opponent, self.team, formatted_date))
