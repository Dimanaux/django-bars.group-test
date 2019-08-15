from django.db import models


class Trial(models.Model):
    title = models.TextField()

    def __str__(self):
        return 'Испытание {0}: {1}'.format(str(self.id), self.title)


class TrialQuestion(models.Model):
    order = models.PositiveIntegerField(unique=True)
    question = models.TextField()
    trial = models.ForeignKey('Trial', on_delete=models.CASCADE)

    def __str__(self):
        return 'Вопрос #{}. исп.{}'.format(self.order, self.trial_id)

    class Meta:
        ordering = ('order',)


class RecruitAnswer(models.Model):
    recruit = models.ForeignKey('recruitment.Recruit', on_delete=models.CASCADE)
    question = models.ForeignKey('TrialQuestion', on_delete=models.CASCADE)
    answer = models.BooleanField()

    class Meta:
        ordering = ('question__order',)
        unique_together = ('recruit', 'question')
