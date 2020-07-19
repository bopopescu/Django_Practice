from django.contrib import admin

# Register your models here.
from Test.models import Division, IndustryTypeMain, IndustryTypeSubordinate, CompanyInfo, District, Thana


class DivisionAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Division, DivisionAdmin)


class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name', 'division']


admin.site.register(District, DistrictAdmin)


class ThanaAdmin(admin.ModelAdmin):
    list_display = ['name', 'district']


admin.site.register(Thana, ThanaAdmin)


class IndustryTypeMainAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(IndustryTypeMain, IndustryTypeMainAdmin)


class IndustryTypeSubordinateAdmin(admin.ModelAdmin):
    list_display = ['name', 'industrytypemain']


admin.site.register(IndustryTypeSubordinate, IndustryTypeSubordinateAdmin)


class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'country', 'division', 'get_industrytypesubordinate', 'user']


admin.site.register(CompanyInfo, CompanyInfoAdmin)
