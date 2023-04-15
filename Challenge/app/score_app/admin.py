from django.contrib import admin

# Register your models here.
from .models import Score

# Task 2 Admin Panel
admin.site.register(Score)
