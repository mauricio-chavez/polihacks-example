"""Models for welcome app"""

from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    url = models.URLField()
    last_login = models.DateTimeField(auto_now_add=True)
    joined = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name