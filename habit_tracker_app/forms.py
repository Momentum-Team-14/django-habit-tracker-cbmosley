from django import forms
from .models import Habit, DailyRecord


class HabitForm(forms.ModelForm):

    class Meta:
        model = Habit
        fields = ('habit_action', 'amount', 'unit')


class DailyRecordForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget(
        empty_label=('Choose Year', 'Choose Month', 'Choose Day')))

    class Meta:
        model = DailyRecord
        fields = ('date', 'daily_amount')
