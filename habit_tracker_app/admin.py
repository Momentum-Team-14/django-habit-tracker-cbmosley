from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Habit, DailyRecord
# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["email", "username", ]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Habit)
admin.site.register(DailyRecord)
