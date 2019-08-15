from django.urls import path

urlpatterns = [
    path('trials/:id', id),
    path('trials/:id/questions', id),
    path('trials/:id/questions/:id', id)
]
