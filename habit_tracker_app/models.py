from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username

# I want to walk 1000 steps daily


class Habit(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="habits")
    habit_action = models.CharField(max_length=225)
    amount = models.IntegerField(null=True)
    unit = models.CharField(max_length=225)

    def __str__(self):
        return f"I want to {self.habit_action} {self.amount} {self.unit} daily."


class DailyRecord(models.Model):
    habit = models.ForeignKey(
        Habit, on_delete=models.CASCADE, related_name='habit')
    date = models.DateField(null=True)
    past_action = models.CharField(max_length=20)
    amount = models.IntegerField(null=True)
    unit = models.CharField(max_length=10)

    def __str__(self):
        return f"I {self.past_action} {self.amount} {self.unit} on {self.date}"
