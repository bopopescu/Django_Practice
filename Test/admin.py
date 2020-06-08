from django.contrib import admin

# Register your models here.
from Test.models import Division, IndustryTypeMaster, IndustryTypeSlave, CompanyInfo, District, Thana


class DivisionAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Division, DivisionAdmin)


class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name', 'division']


admin.site.register(District, DistrictAdmin)


class ThanaAdmin(admin.ModelAdmin):
    list_display = ['name', 'district']


admin.site.register(Thana, ThanaAdmin)


class IndustryTypeMasterAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(IndustryTypeMaster, IndustryTypeMasterAdmin)


class IndustryTypeSlaveAdmin(admin.ModelAdmin):
    list_display = ['name', 'industrytypemaster']


admin.site.register(IndustryTypeSlave, IndustryTypeSlaveAdmin)


class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'country', 'division', 'get_industrytypeslave', 'user']


admin.site.register(CompanyInfo, CompanyInfoAdmin)
