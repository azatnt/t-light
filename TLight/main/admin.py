from django.contrib import admin
from .models import *


admin.site.register(TClient)
admin.site.register(DStatus)
admin.site.register(DGender)
admin.site.register(DType)
admin.site.register(TPhone)
admin.site.register(TMail)
admin.site.register(TSocial)
admin.site.register(TLegalEntity)
class TDepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent', 'client_count')
    def client_count(self, obj):
        return obj.id_dept_cl.count()
admin.site.register(TDepartment, TDepartmentAdmin)
admin.site.register(TLegalEntityDepartment)
admin.site.register(TClientDepartment)
