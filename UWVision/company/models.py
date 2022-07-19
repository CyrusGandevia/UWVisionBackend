from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    class Meta:
        verbose_name_plural = 'Companies'

    name = models.CharField(max_length=255)
    description = models.TextField()
    industry = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.name