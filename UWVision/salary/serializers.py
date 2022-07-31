from rest_framework import serializers
from .models import Salary

class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = [
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
            'added_by'
        ]