from django.contrib import admin
from .models import Company

class CompanyAdmin(admin.ModelAdmin):
    search_fields = ['name', 'description', 'industry']
    list_display = ['id', 'name', 'description', 'industry', 'logo', 'created_at', 'added_by']
    list_filter = ['industry']
    
admin.site.register(Company, CompanyAdmin)