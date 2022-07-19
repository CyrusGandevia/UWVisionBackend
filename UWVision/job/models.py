from django.db import models
from django.contrib.auth.models import User
from company.models import Company

# Create your models here.
class Job(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.company_id.name + " | " + self.name

class SavedJob(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)