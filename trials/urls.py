from django.urls import path

from . import views

urlpatterns = [
    path('<int:trial_id>/questions/<int:question_order>', views.question, name='question'),
    path('<int:trial_id>', views.trial, name='trial'),
    path('<int:trial_id>/complete', views.complete, name='complete'),
]
