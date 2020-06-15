from django.http import HttpResponse,JsonResponse,Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Employee,Department,CostCentre


    
def index(request):

    return render(request, 'employees/index.html')


def all(request):
    data={}
    
    try:
        departments = Department.objects.all()
        
        

        
        print(data)       


    except:
        raise Exception

    
    return render(request, 'employees/all.html',  {'departments':departments})


def getCostCentres(department):
    

    return 
    
