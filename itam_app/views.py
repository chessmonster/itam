from django.urls import reverse_lazy
from vanilla import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import AssetForm, EmployeeForm, Asset_TypeForm, Os_TypeForm, Product_TypeForm, State_TypeForm, DepartmentForm
from .models import Asset, Employee, Asset_Type, Os_Type, Product_Type, State_Type, Department
from django.http import HttpResponse

import barcode
from barcode.writer import ImageWriter

# Asset #
class AssetList(ListView):
    model = Asset
    paginate_by = 50


class AssetCreate(CreateView):
    model = Asset
    form_class = AssetForm
    success_url = reverse_lazy('itam_app:list')


class AssetDetail(DetailView):
    model = Asset


class AssetUpdate(UpdateView):
    model = Asset
    form_class = AssetForm
    success_url = reverse_lazy('itam_app:list')


class AssetDelete(DeleteView):
    model = Asset
    success_url = reverse_lazy('itam_app:list')


# Employee #
class EmployeeList(ListView):
    model = Employee
    paginate_by = 20


class EmployeeCreate(CreateView):
    model = Employee
    form_class = EmployeeForm
    success_url = reverse_lazy('itam_app:employee_list')


class EmployeeDetail(DetailView):
    model = Employee


class EmployeeUpdate(UpdateView):
    model = Employee
    form_class = EmployeeForm
    success_url = reverse_lazy('itam_app:employee_list')


class EmployeeDelete(DeleteView):
    model = Employee
    success_url = reverse_lazy('itam_app:employee_list')


# Asset Type #
class Asset_TypeList(ListView):
    model = Asset_Type
    paginate_by = 20


class Asset_TypeCreate(CreateView):
    model = Asset_Type
    form_class = Asset_TypeForm
    success_url = reverse_lazy('itam_app:asset_type_list')


class Asset_TypeDetail(DetailView):
    model = Asset_Type


class Asset_TypeUpdate(UpdateView):
    model = Asset_Type
    form_class = Asset_TypeForm
    success_url = reverse_lazy('itam_app:asset_type_list')


class Asset_TypeDelete(DeleteView):
    model = Asset_Type
    success_url = reverse_lazy('itam_app:asset_type_list')


# OS Type #
class OS_TypeList(ListView):
    model = Os_Type
    paginate_by = 20


class OS_TypeCreate(CreateView):
    model = Os_Type
    form_class = Os_TypeForm
    success_url = reverse_lazy('itam_app:os_type_list')


class OS_TypeDetail(DetailView):
    model = Os_Type


class OS_TypeUpdate(UpdateView):
    model = Os_Type
    form_class = Os_TypeForm
    success_url = reverse_lazy('itam_app:os_type_list')


class OS_TypeDelete(DeleteView):
    model = Os_Type
    success_url = reverse_lazy('itam_app:os_type_list')


# Product #
class Product_TypeList(ListView):
    model = Product_Type
    paginate_by = 20


class Product_TypeCreate(CreateView):
    model = Product_Type
    form_class = Product_TypeForm
    success_url = reverse_lazy('itam_app:product_type_list')


class Product_TypeDetail(DetailView):
    model = Product_Type


class Product_TypeUpdate(UpdateView):
    model = Product_Type
    form_class = Product_TypeForm
    success_url = reverse_lazy('itam_app:product_type_list')


class Product_TypeDelete(DeleteView):
    model = Product_Type
    success_url = reverse_lazy('itam_app:product_type_list')


# State #
class State_TypeList(ListView):
    model = State_Type
    paginate_by = 20


class State_TypeCreate(CreateView):
    model = State_Type
    form_class = State_TypeForm
    success_url = reverse_lazy('itam_app:state_type_list')


class State_TypeDetail(DetailView):
    model = State_Type


class State_TypeUpdate(UpdateView):
    model = State_Type
    form_class = State_TypeForm
    success_url = reverse_lazy('itam_app:state_type_list')


class State_TypeDelete(DeleteView):
    model = State_Type
    success_url = reverse_lazy('itam_app:state_type_list')



# Department #
class DepartmentList(ListView):
    model = Department
    paginate_by = 20


class DepartmentCreate(CreateView):
    model = Department
    form_class = DepartmentForm
    success_url = reverse_lazy('itam_app:department_list')


class DepartmentDetail(DetailView):
    model = Department


class DepartmentUpdate(UpdateView):
    model = Department
    form_class = DepartmentForm
    success_url = reverse_lazy('itam_app:department_list')


class DepartmentDelete(DeleteView):
    model = Department
    success_url = reverse_lazy('itam_app:department_list')


# barcode generation
def get_barcode(request, serial_number):
    

    ean = barcode.get('ean13', str(serial_number))
    filename = ean.save(serial_number)

    # print(filename)

    # return HttpResponse(str(filename), 'image/gif')
    
    ## return HttpResponse(str(ean), 'image/gif')

    # response = HttpResponse(mimetype='application/force-download')
    # response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name)
    # response['X-Sendfile'] = smart_str('/ean13.svg')
    # return response

    with open(filename, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=' + filename
        response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-16'
        return response