from django.shortcuts import get_object_or_404, redirect, render
from mainBackend.models import *


# Create your views here.

def index(request):
    
    return render(request , 'index.html')

def users(request):
    
    return render(request , 'users.html')

def properties(request):
    
    return render(request , 'properties.html')

def operations(request):
    
    return render(request , 'operations.html')

def officers(request):
    
    return render(request , 'officers.html')

def notifications(request):
    
    return render(request , 'notifications.html')

def propertiesNotification(request):
    notifications = PropertyNotification.objects.all()
    return render(request , 'propertiesNotification.html',{'notifications':notifications})


def statusVerification(request,id):
    notification = get_object_or_404(PropertyNotification,id=id)
    propertyId = notification.PropertyId.id
    property = get_object_or_404(Property,id=propertyId)
    property.verificationStatus = True
    property.save()
    if property.verificationStatus == True:
        notification.delete()
    #     pass
    return redirect('propertiesNotification')
    

def usersNotification(request):
    
    return render(request , 'usersNotification.html')


def charts(request):
    
    return render(request , 'charts.html')



