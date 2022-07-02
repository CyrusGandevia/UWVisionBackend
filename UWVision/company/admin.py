from django.contrib import admin
from .models import Company

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = [field.name for field in Company._meta.get_fields()]

admin.site.register(Company, CompanyAdmin)