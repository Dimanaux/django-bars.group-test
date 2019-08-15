from django import forms

from .models import *


class RecruitForm(forms.ModelForm):
    class Meta:
        model = Recruit
        fields = ('name', 'age', 'planet', 'email',)
