from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Habit, DailyRecord
from .forms import HabitForm, DailyRecordForm
# Create your views here.


def index(request):
    pass
    return render(request, 'habits/index.html', {})


@login_required
def list_habits(request):
    habits = Habit.objects.filter(user=request.user)
    return render(request, 'habits/habit_home.html', {"habits": habits})


def habit_detail(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    habit_records = DailyRecord.objects.filter(habit=pk)
    return render(request, "habits/habit_detail.html", {"habit": habit, "habit_records": habit_records})


def add_habit(request):
    if request.method == "POST":
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()

            return redirect("habit_home")
    else:
        form = HabitForm()

    return render(request, "habits/add_habit.html", {"form": form, "text_for_labels": {"habit_action": "example: run, read, walk", "amount": "example"}})


def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == "GET":
        form = HabitForm(instance=habit)
    else:
        form = HabitForm(data=request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect("habit_detail")
        else:
            print(form.errors)

    return render(request, "habits/edit_habit.html", {"form": form, "habit": habit})


def add_record(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == "POST":
        form = DailyRecordForm(data=request.POST)
        if form.is_valid():
            habit_record = form.save(commit=False)
            habit_record.user = request.user
            habit_record.habit = habit
            habit_record.save()

            return redirect("habit_detail", pk=habit.pk)
    else:
        form = DailyRecordForm()

    return render(request, "habits/add_record.html", {"form": form})
# def list_records(request):
#     records = DailyRecord.objects.all()
#     return render(request, "habits/list_records.html", {"records": records})


def record_detail(request, pk):
    record = get_object_or_404(DailyRecord, pk=pk)
    return render(request, "habits/record_detail.html", {"record": record})


# def create_habit(request):
#     if request.methond == "POST":
#         form = HabitForm(request.POST)
#         if form.is_valid():
#             habit = form.save()
#             return redirect('habit_home')
#     else:
#         form = HabitForm()
#     return render(request, '')
