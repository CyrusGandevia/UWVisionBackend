from django.db import models
from django.contrib.auth.models import User
from company.models import Company

# Create your models here.
class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.company) + " | " + self.name

class SavedJob(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)