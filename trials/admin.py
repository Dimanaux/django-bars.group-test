from django.contrib import admin

from .models import *

admin.register(
    Trial,
    TrialQuestion,
    RecruitAnswer,
)
