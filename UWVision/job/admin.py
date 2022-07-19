from django.contrib import admin

from .models import Job, SavedJob

# Register your models here.
class JobAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id', 'company_id', 'name', 'created_at', 'added_by']

class SavedJobAdmin(admin.ModelAdmin):
    search_fields = ['job_id', 'user_id'] #TODO: Is this searchable?
    list_display = ['id', 'job_id', 'user_id']

admin.site.register(Job, JobAdmin)
admin.site.register(SavedJob, SavedJobAdmin)