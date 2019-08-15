from django.db import models


class Recruit(models.Model):
    name = models.TextField()
    planet = models.ForeignKey('Planet', on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    email = models.EmailField()


class Sith(models.Model):
    name = models.TextField()
    planet = models.ForeignKey('Planet', on_delete=models.CASCADE)


class Planet(models.Model):
    name = models.TextField()


class ShadowHand(Recruit):
    sith = models.ForeignKey('Sith', on_delete=models.CASCADE)
