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

# Create your models here.
class InterviewQuestion(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    body = models.TextField()
    year_worked = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    term_worked = models.CharField(max_length=6, choices=TERM_CHOICES)
    coop_term_number = models.IntegerField(choices=COOP_NUMBER_CHOICES)
    program = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.job) + ' | ' + self.added_by.username

class UpvotedInterviewQuestion(models.Model):
    interview_question = models.ForeignKey(InterviewQuestion, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)