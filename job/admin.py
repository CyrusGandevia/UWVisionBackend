from django.contrib import admin
from .models import Job, SavedJob

class JobAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id', 'company', 'name', 'created_at', 'added_by']

class SavedJobAdmin(admin.ModelAdmin):
    list_display = ['id', 'job', 'user']

admin.site.register(Job, JobAdmin)
admin.site.register(SavedJob, SavedJobAdmin)