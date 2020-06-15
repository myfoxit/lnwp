from django.contrib import admin
from .models import Employee,CostCentre,Customer,Department,Contract,ContractType,Customer,ServiceType
# Register your models here.


class ModelInline(admin.TabularInline):
    model = CostCentre

class ModelInlineDepartments(admin.TabularInline):
    model = Department

class ModelInlineDepartmentsEmployee(admin.TabularInline):
    model = Employee.departments.through
    extra=0

class ModelInlineDepartmentsCustomer(admin.TabularInline):
    model = Customer.departments.through
    extra=0

class ModelInlineCostcentresEmployee(admin.TabularInline):
    model = Employee.costcentres.through
    extra=0

class ModelInlineCostcentresCustomer(admin.TabularInline):
    model = Customer.costcentres.through
    extra=0

class ModelInlineServiceTypeCustomer(admin.TabularInline):
    model = Customer.servicetypes.through
    extra=0




class DepartmentAdmin(admin.ModelAdmin):
    model = Department
    inlines = [
        ModelInline,
        ModelInlineDepartmentsEmployee,ModelInlineDepartmentsCustomer]

class CostCentreAdmin(admin.ModelAdmin):
    model = CostCentre
    inlines = [
        
        ModelInlineCostcentresEmployee,ModelInlineCostcentresCustomer
        ]

class ServiceTypeAdmin(admin.ModelAdmin):
    model = ServiceType
    inlines = [
        
        ModelInlineServiceTypeCustomer,
        ]




admin.site.register(Employee)
admin.site.register(CostCentre,CostCentreAdmin)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(Customer)
admin.site.register(Contract)
admin.site.register(ServiceType,ServiceTypeAdmin)
admin.site.register(ContractType)