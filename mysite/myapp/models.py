from django.db import models

# Create your models here.


class League(models.Model):
    number = models.IntegerField(max_length=32)

    def __str__(self):
        return self.number


class Year(models.Model):
    number = models.IntegerField(max_length=32)

    def __str__(self):
        return self.number


class Team(models.Model):
    string = models.CharField(max_length=32)

    def __str__(self):
        return self.string


class Participation(models.Model):
    number = models.IntegerField(max_length=32)

    def __str__(self):
        return self.number


class Person(models.Model):
    string = models.CharField(max_length=32)

    def __str__(self):
        return self.string


class Song(models.Model):
    string = models.CharField(max_length=32)

    def __str__(self):
        return self.string


class Parent(models.Model):
    league = models.ForeignKey(
        League, on_delete=models.SET_NULL, null=True, related_name='related_League')
    year = models.ForeignKey(
        Year, on_delete=models.SET_NULL, null=True, related_name='related_year')
    team = models.ForeignKey(
        Team, on_delete=models.SET_NULL, null=True, related_name='related_Team')
    participation = models.ForeignKey(
        Participation, on_delete=models.SET_NULL, null=True, related_name='related_Participation')
    person = models.ManyToManyField(
        Person, related_name='related_Person')
    song = models.ForeignKey(
        Song, on_delete=models.SET_NULL, null=True, related_name='related_Song')

    def __str__(self):
        return self.song
