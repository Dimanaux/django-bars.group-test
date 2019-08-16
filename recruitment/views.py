from django.core.mail import send_mail
from django.shortcuts import render, redirect

from recruitment.forms import RecruitForm
from recruitment.models import *
from sith_order.settings import *
from trials.models import *


def index(request):
    return render(request, 'recruitment/index.html')


def sith(request):
    if request.method == 'GET':
        return get_sith_form(request)
    elif request.method == 'POST':
        sith_id = int(request.POST['sith_id'])
        request.session['sith_id'] = sith_id
        return redirect('requests')


def recruit(request):
    if request.method == 'GET':
        return get_recruit_form(request)
    elif request.method == 'POST':
        r = create_recruit(request)
        request.session['recruit_id'] = r.id
        return redirect('trial', trial_id=1)


def requests(request):
    recruits_with_answers = {}
    for r in Recruit.objects.filter(shadow_handed=False):
        recruits_with_answers[r] = RecruitAnswer.objects.filter(recruit=r)

    sith_shadow_hands = {}
    for s in Sith.objects.all():
        sith_shadow_hands[s] = ShadowHand.objects.filter(sith=s).count()

    return render(
        request,
        'recruitment/requests.html',
        {
            'recruits': recruits_with_answers,
            'questions': TrialQuestion.objects.all(),
            'sith_shadow_hands': sith_shadow_hands,
            'major_siths': [s for s, h in sith_shadow_hands.items() if h > 1]
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


def shadow_hand(request):
    if request.method == 'POST':
        make_shadow_hand(
            Recruit.objects.get(id=request.POST['recruit_id']),
            Sith.objects.get(id=request.session['sith_id'])
        )
    return redirect('requests')


def notify_shadow_hand(sh: ShadowHand):
    send_mail(
        'Вербовка Ситхов',
        '{}, вы стали Рукой Теней. Ваш мастер - {}'.format(sh.name, sh.sith.name),
        EMAIL_HOST_USER,
        [sh.email],
        fail_silently=True
    )


def make_shadow_hand(r: Recruit, s: Sith) -> ShadowHand:
    if ShadowHand.objects.filter(sith=s).count() >= 3:
        raise Exception("One sith's shadow hands quantity should not exceed 3")
    sh = ShadowHand.objects.create(
        name=r.name,
        age=r.age,
        planet_id=r.planet_id,
        email=r.email,
        sith=s,
        shadow_handed=True
    )
    r.delete()
    notify_shadow_hand(sh)
    return sh
