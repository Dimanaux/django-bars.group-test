from django.shortcuts import render, redirect

from trials.models import *


def trial(request, trial_id: int):
    return render(
        request,
        'trials/trial.html',
        {
            'trial': Trial.objects.get(id=trial_id)
        }
    )


def get_question(request, trial_question: TrialQuestion):
    return render(
        request,
        'trials/question.html',
        {
            'trial': trial_question.trial,
            'question': trial_question
        }
    )


def answer_question(request, trial_question: TrialQuestion):
    RecruitAnswer.objects.create(
        recruit_id=request.session['recruit_id'],
        question=trial_question,
        answer=request.POST['answer'] == 'True'
    )
    if TrialQuestion.objects.last() == trial_question:
        return redirect(
            'complete',
            trial_id=trial_question.trial_id
        )
    else:
        return redirect(
            'question',
            trial_id=trial_question.trial_id,
            question_order=trial_question.order + 1
        )


def question(request, trial_id: int, question_order: int):
    q = TrialQuestion.objects.get(trial_id=trial_id, order=question_order)
    if request.method == 'GET':
        return get_question(request, q)
    elif request.method == 'POST':
        return answer_question(request, q)


def complete(request, trial_id: int):
    return render(
        request,
        'trials/complete.html',
        {
            'trial': Trial.objects.get(id=trial_id)
        }
    )
