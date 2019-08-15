from django.shortcuts import render, redirect

from recruitment.forms import RecruitForm
from recruitment.models import *
from trials.models import *


def index(request):
    return render(request, 'recruitment/index.html')


def sith(request):
    if request.method == 'GET':
        return get_sith_form(request)
    elif request.method == 'POST':
        sith_id = int(request.POST['sith'])
        request.session['sith_id'] = Sith.objects.get(sith_id).id
        return redirect('requests')


def recruit(request):
    if request.method == 'GET':
        return get_recruit_form(request)
    elif request.method == 'POST':
        r = create_recruit(request)
        request.session['recruit_id'] = r.id
        return redirect('trial', trial_id=1)


def requests(request):
    recruits = {}
    for r in Recruit.objects.all():
        recruits[r] = RecruitAnswer.objects.filter(recruit=r)
    return render(
        request,
        'recruitment/requests.html',
        {
            'recruits': recruits
        }
    )


def get_recruit_form(request):
    return render(
        request,
        'recruitment/recruit.html',
        {
            'planets': Planet.objects.all(),
        }
    )


def get_sith_form(request):
    return render(
        request,
        'recruitment/sith.html',
        {
            'ss': Sith.objects.all()
        }
    )


def create_recruit(request) -> Recruit:
    form = RecruitForm(request.POST)
    return form.save()
