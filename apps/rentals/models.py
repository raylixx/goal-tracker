from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

class Goal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=99)
    description= models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Goal'
        verbose_name_plural = 'Goals'

    def progress_percent(self):
        steps = self.steps.all()
        if not steps.exists():
            return 0
        done_steps = steps.filter(is_done=True).count()
        return int((done_steps / steps.count()) * 100)
    def status(self):
        steps = self.steps.all()
        if not steps.exists():
            return'not_started'
        done_count = steps.filter(is_done=True).count()
        if done_count == 0:
            return 'not_started'
        elif done_count == steps.count():
            return 'done'
        else:
            return 'in_progress'

    def __str__(self):
        return self.title


class Step(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='steps')
    title = models.CharField(max_length=99)
    is_done = models.BooleanField(default=False)
    due_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Step'
        verbose_name_plural = 'Steps'

    def __str__(self):
        return f"{self.title} ({'Done' if self.is_done else 'Pending'})"













