from django.db import models


class Chore(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField()


class Person(models.Model):
    name = models.CharField(max_length=50)


class Event(models.Model):
    chore = models.ForeignKey(Chore)
    person = models.ForeignKey(Person)
    date = models.DateTimeField('date done')
