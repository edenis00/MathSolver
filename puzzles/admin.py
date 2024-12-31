from django.contrib import admin
from .models import MathProblem

# Register your models here.
admin.site.register(MathProblem)

class MathProblemAdmin(admin.ModelAdmin):
    list_display = ['question', 'solution', 'user', 'created_at']
    search_fields = ['question', 'solution']