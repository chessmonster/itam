from django.conf.urls import url
from django.urls import path
from . import views

app_name='itam_app'

urlpatterns = [
    url(r'^$', views.AssetList.as_view(), name='list'),
    url(r'^new/$', views.AssetCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.AssetDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.AssetUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.AssetDelete.as_view(), name='delete'),

    path('get_barcode/<int:serial_number>/', views.get_barcode, name='get_barcode')    

    # url(r'^$', views.EmployeeList.as_view(), name='employee_list'),
    # url(r'^new_employee/$', views.EmployeeCreate.as_view(), name='employee_create'),
    # url(r'^(?P<pk>\d+)/$', views.EmployeeDetail.as_view(), name='employee_detail'),
    # url(r'^(?P<pk>\d+)/update/$', views.EmployeeUpdate.as_view(), name='employee_update'),
    # url(r'^(?P<pk>\d+)/delete/$', views.EmployeeDelete.as_view(), name='employee_delete'),

    # url(r'^$', views.Asset_TypeList.as_view(), name='asset_type_list'),
    # url(r'^new/$', views.Asset_TypeCreate.as_view(), name='asset_type_create'),
    # url(r'^(?P<pk>\d+)/$', views.Asset_TypeDetail.as_view(), name='asset_type_detail'),
    # url(r'^(?P<pk>\d+)/update/$', views.Asset_TypeUpdate.as_view(), name='asset_type_update'),
    # url(r'^(?P<pk>\d+)/delete/$', views.Asset_TypeDelete.as_view(), name='asset_type_delete'),

    # url(r'^$', views.OS_TypeList.as_view(), name='os_type_list'),
    # url(r'^new/$', views.OS_TypeCreate.as_view(), name='os_type_create'),
    # url(r'^(?P<pk>\d+)/$', views.OS_TypeDetail.as_view(), name='os_type_detail'),
    # url(r'^(?P<pk>\d+)/update/$', views.OS_TypeUpdate.as_view(), name='os_type_update'),
    # url(r'^(?P<pk>\d+)/delete/$', views.OS_TypeDelete.as_view(), name='os_type_delete'),

    # url(r'^$', views.Product_TypeList.as_view(), name='product_type_list'),
    # url(r'^new/$', views.Product_TypeCreate.as_view(), name='product_type_create'),
    # url(r'^(?P<pk>\d+)/$', views.Product_TypeDetail.as_view(), name='product_type_detail'),
    # url(r'^(?P<pk>\d+)/update/$', views.Product_TypeUpdate.as_view(), name='product_type_update'),
    # url(r'^(?P<pk>\d+)/delete/$', views.Product_TypeDelete.as_view(), name='product_type_delete'),

    # url(r'^$', views.State_TypeList.as_view(), name='state_type_list'),
    # url(r'^new/$', views.State_TypeCreate.as_view(), name='state_type_create'),
    # url(r'^(?P<pk>\d+)/$', views.State_TypeDetail.as_view(), name='state_type_detail'),
    # url(r'^(?P<pk>\d+)/update/$', views.State_TypeUpdate.as_view(), name='state_type_update'),
    # url(r'^(?P<pk>\d+)/delete/$', views.State_TypeDelete.as_view(), name='state_type_delete'),

    # url(r'^$', views.DepartmentList.as_view(), name='department_list'),
    # url(r'^new/$', views.DepartmentCreate.as_view(), name='department_create'),
    # url(r'^(?P<pk>\d+)/$', views.DepartmentDetail.as_view(), name='department_detail'),
    # url(r'^(?P<pk>\d+)/update/$', views.DepartmentUpdate.as_view(), name='department_update'),
    # url(r'^(?P<pk>\d+)/delete/$', views.DepartmentDelete.as_view(), name='department_delete'),
]
