from django.contrib import admin

from .models import *

admin.register(
    Recruit,
    Sith,
    Planet,
    ShadowHand,
)
