from django.contrib import admin

# Register your models here.
from Formvalidation.models import IndustryType, Company, Profile, Divisions


class IndustryTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(IndustryType, IndustryTypeAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['designation', 'email', 'phone', 'user']


admin.site.register(Profile, ProfileAdmin)


class DivisionsAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Divisions, DivisionsAdmin)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'divisions', 'get_industrytype', 'user']


admin.site.register(Company, CompanyAdmin)
