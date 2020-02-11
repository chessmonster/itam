from django.forms import ModelForm
from .models import Asset, Employee, Asset_Type, Os_Type, Product_Type, State_Type, Department


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ('name', 'email', 'employee_number')
    

class Asset_TypeForm(ModelForm):
    class Meta:
        model = Asset_Type
        fields = ('name', 'description')
    

class Os_TypeForm(ModelForm):
    class Meta:
        model = Os_Type
        fields = ('name', 'description')


class Product_TypeForm(ModelForm):
    class Meta:
        model = Product_Type
        fields = ('name', 'description')



class State_TypeForm(ModelForm):
    class Meta:
        model = State_Type
        fields = ('name', 'description')
    

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ('name', 'description')
    

class AssetForm(ModelForm):
    class Meta:
        model = Asset
        fields = ('display_name'
        	, 'mac_address'
        	, 'serial_number'
        	, 'date_assigned'
        	, 'employee'
        	, 'asset_type'
        	, 'os_type'
        	, 'product_type'
        	, 'state_type'
        	, 'department')
    