from django.db import models
from user.models import User
from job.models import Job 

import datetime

# Defining constants
YEAR_CHOICES = []
for year in range(2015, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((year, year))

TERM_CHOICES = [
    ('Fall', 'Fall'),
    ('Spring', 'Spring'),
    ('Winter', 'Winter')
]

COOP_NUMBER_CHOICES = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
]

#TODO: Make sure decimal fields are non-negative
# Some fields currently are marked as optional (when blank and null are True) because these features are still pending implementation on frontend
class Salary(models.Model):
    class Meta:
        verbose_name_plural = 'Salaries'

    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    hourly_wage = models.DecimalField(max_digits=5, decimal_places=2) # Max is 999.99
    monthly_relocation_stipend = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True) # Max is 99,999.99
    monthly_misc_stipends = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True) # Max is 9,999.99
    term_signing_bonus = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True) # Max is 99,999.99
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    year_worked = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year, blank=True, null=True)
    term_worked = models.CharField(max_length=6, choices=TERM_CHOICES, blank=True, null=True)
    coop_term_number = models.IntegerField(choices=COOP_NUMBER_CHOICES, blank=True, null=True)
    program = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete = models.CASCADE)
