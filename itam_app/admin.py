from django.contrib import admin
from .models import Asset, Employee, Asset_Type, Os_Type, Product_Type, State_Type, Department

admin.site.register(Asset)
admin.site.register(Employee)
admin.site.register(Asset_Type)
admin.site.register(Os_Type)
admin.site.register(Product_Type)
admin.site.register(State_Type)
admin.site.register(Department)
