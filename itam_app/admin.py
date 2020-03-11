from django.contrib import admin
from .models import Asset, Employee, Asset_Type, Os_Type, Product_Type, State_Type, Department
from simple_history.admin import SimpleHistoryAdmin


admin.site.register(Asset, SimpleHistoryAdmin)
admin.site.register(Employee, SimpleHistoryAdmin)
admin.site.register(Asset_Type, SimpleHistoryAdmin)
admin.site.register(Os_Type, SimpleHistoryAdmin)
admin.site.register(Product_Type, SimpleHistoryAdmin)
admin.site.register(State_Type, SimpleHistoryAdmin)
admin.site.register(Department, SimpleHistoryAdmin)


