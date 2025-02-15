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

RATING_CHOICES = [
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5)
]

# Some fields currently are marked as optional (when blank and null are True) because these features are still pending implementation on frontend
class Review(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    body = models.TextField(blank=True, null=True)
    work_life_balance = models.IntegerField(choices=RATING_CHOICES)
    culture = models.IntegerField(choices=RATING_CHOICES)
    interesting_work = models.IntegerField(choices=RATING_CHOICES)
    overall_rating = models.IntegerField(choices=RATING_CHOICES)
    year_worked = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    term_worked = models.CharField(max_length=6, choices=TERM_CHOICES)
    coop_term_number = models.IntegerField(choices=COOP_NUMBER_CHOICES, blank=True, null=True) # Optional fields
    program = models.CharField(max_length=255, blank=True, null=True) # Optional fields
    created_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.job) + ' | ' + self.added_by.username + ' | ' + str(self.id)

class UpvotedReview(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
