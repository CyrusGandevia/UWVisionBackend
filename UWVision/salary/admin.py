from django.contrib import admin
from .models import Salary

# Register your models here.
class SalaryAdmin(admin.ModelAdmin):
    search_fields = ['job', 'city', 'country', 'program']
    list_display = [
        'id',
        'job',
        'hourly_wage',
        'monthly_relocation_stipend',
        'monthly_misc_stipends',
        'term_signing_bonus',
        'city',
        'country',
        'year_worked',
        'term_worked',
        'coop_term_number',
        'program',
        'created_at',
        'added_by',
    ]
    list_filter = ['year_worked', 'term_worked', 'coop_term_number', 'program']

admin.site.register(Salary, SalaryAdmin)
