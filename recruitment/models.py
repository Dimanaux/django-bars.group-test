from django.db import models


class Recruit(models.Model):
    name = models.TextField()
    planet = models.ForeignKey('Planet', on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    shadow_handed = models.BooleanField(default=False)

    def __str__(self):
        return 'Рекрут ' + self.name


class Sith(models.Model):
    name = models.TextField()
    planet = models.ForeignKey('Planet', on_delete=models.CASCADE)

    def __str__(self):
        return 'Ситх ' + self.name


class Planet(models.Model):
    name = models.TextField()

    def __str__(self):
        return 'Планета ' + self.name


class ShadowHand(Recruit):
    sith = models.ForeignKey('Sith', on_delete=models.CASCADE)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.shadow_handed = True

    def __str__(self):
        return 'Рука Теней ' + self.name
