from django.db import models


class League(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Team (models.Model):
    location = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=20)
    league = models.ForeignKey(League, null=True, on_delete=models.SET_NULL)

    def display_name(self):
        return "%s %s" % (self.location, self.nickname)

    def __str__(self):
        return self.display_name