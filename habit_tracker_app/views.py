from django.shortcuts import render, get_object_or_404, redirect
from .models import CustomUser, Habit, DailyRecord
# Create your views here.


def index(request):
    pass
    return render(request, 'habits/index.html', {})


def list_habits(request):
    habits = Habit.objects.filter(user=request.user)
    return render(request, 'habits/habit_home.html', {"habits": habits})


def habit_detail(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    return render(request, "habits/habit_detail.html", {"habit": habit})


def list_records(request):
    records = DailyRecord.objects.filter(record=Habit.record)
    return render(request, "habits/list_records.html", {"records": records})


def record_detail(request, pk):
    record = get_object_or_404(DailyRecord, pk=pk)
    return render(request, "habits/record_detail.html", {"record": record})

# def create_habit(request):
#     if request.methond == "POST":
#         form = HabitForm(request.POST)
#         if form.is_valid():
#             habit = form.save()
#             return
#             redirec
