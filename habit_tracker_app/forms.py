from django import forms
from .models import Habit, DailyRecord


class HabitForm(forms.ModelForm):

    class Meta:
        model = Habit
        fields = ('user', 'habit_action', 'amount', 'unit')


class DailyRecordForm(forms.ModelForm):

    class Meta:
        model = DailyRecord
        fields = ('date', 'daily_amount')
