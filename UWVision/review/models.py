from django.db import models
from django.contrib.auth.models import User
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

RATING_CHOICES = [
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5)
]

# Create your models here.
class Review(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    body = models.TextField()
    work_life_balance = models.IntegerField(choices=RATING_CHOICES)
    culture = models.IntegerField(choices=RATING_CHOICES)
    interesting_work = models.IntegerField(choices=RATING_CHOICES)
    overall_rating = models.IntegerField(choices=RATING_CHOICES)
    year_worked = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    term_worked = models.CharField(max_length=6, choices=TERM_CHOICES)
    coop_term_number = models.IntegerField(choices=COOP_NUMBER_CHOICES)
    program = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.job_id.__str__() + ' | ' + self.added_by.username

class UpvotedReview(models.Model):
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
