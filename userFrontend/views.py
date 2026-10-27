from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from mainBackend.models import *
from mainBackend.forms import *

# Create your views here.

def start(request):
    
    return render(request , 'start.html')

def base(request):
    
    return render(request , 'base.html')

def start2(request):
    
    return render(request , 'start2.html')

def userCategory(request):
    
    return render(request , 'userCategory.html')

def basicUsersPage(request):

    properties = Property.objects.filter(verificationStatus=True)
     # Get form inputs
    price = request.POST.get('price')
    category = request.POST.get('category')
    rooms = request.POST.getlist('rooms')

    # Filter by price
    # if price:
    #     properties = properties.filter(PropertyPrice=price)

    # Filter by category
    if category:
        properties = properties.filter(PropertyType=category)

    # Filter by rooms
    # if rooms and 'all' not in rooms:
    #     room_filters = {
    #         'studio': 1,
    #         '2': 2,
    #         '3': 3,
    #         'house': 4,  # assuming 4 represents 
    #     }
    #     room_values = [room_filters[room] for room in rooms if room in room_filters]
    #     properties = properties.filter(number_of_rooms__in=room_values)

    
    return render(request , 'basicUsersPage.html',{'properties':properties})

def basicUsersArea(request):
    properties = Property.objects.filter(verificationStatus=True)
    return render(request, 'basicUsersArea.html', {'properties': properties})

def filter_properties(request):
    category = request.GET.get('category')
    price = request.GET.get('price')
    preference = request.GET.get('preference')
    
    if category and price and preference :
        properties = Property.objects.filter(verificationStatus=True, PropertyType=category,PropertyPrice=price)
    elif category and price:
        properties = Property.objects.filter(verificationStatus=True, PropertyType=category,PropertyPrice=price)
    elif category:
         properties = Property.objects.filter(verificationStatus=True, PropertyType=category)
    elif price:
         properties = Property.objects.filter(verificationStatus=True,PropertyPrice=price)
    else:
        properties = Property.objects.filter(verificationStatus=True)
    
    properties_data = list(properties.values())
    return JsonResponse({'properties': properties_data})

def ownerUsersPage(request):
    
    return render(request , 'ownerUsersPage.html')

def ownerAllProperties(request):
    
    return render(request , 'ownerAllProperties.html')

def ownerNotifications(request):
    
    return render(request , 'ownerNotifications.html')

def ownerProperties(request):
    
    return render(request , 'ownerProperties.html')

def ownerManagementCenter(request):
    
    return render(request , 'ownerManagementCenter.html')

def addProperty(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        files = request.GET.getlist('PropertyOwningFiles')
        form.PropertyOwningFiles = files
        # if form.is_valid():
        form.save()
        PropertyInstance = Property.objects.order_by('-id').first()
        # Création de l'objet PropertyNotification
        notification = PropertyNotification(PropertyId=PropertyInstance)
        notification.save()

        return redirect('addProperty')  
    # else:
    #     form = PropertyForm()
        
        
    return render(request , 'addProperty.html',{'form': form})

def modifyPropertyPage(request):
    # property_instance = get_object_or_404(Property, id=property_id)
    properties = Property.objects.all()

    return render(request,'modifyPropertyPage.html',{'properties':properties})


def modifyProperty(request,property_id):
    property_instance = get_object_or_404(Property, id=property_id)
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property_instance)
        if form.is_valid():
            form.save()  
            return redirect('modifyPropertyPage')  

    else:
        form = PropertyForm(instance=property_instance)
    return render(request, 'modifyProperty.html', {'form': form})


def deleteProperty(request, property_id):
    property_instance = get_object_or_404(Property, id=property_id)
    property_instance.delete()
          
    return redirect('modifyPropertyPage')

def verifyStatutOwner(request):
    
    return render(request , 'verifyStatutOwner.html')

def verifyStatutClient(request):
    
    return render(request , 'verifyStatutClient.html')

def properties(request):
    
    return render(request , 'properties.html')

def propertyViewMore(request):
    
    return render(request , 'propertyViewMore.html')


def notifications(request):
    
    return render(request , 'notifications.html')


def charts(request):
    
    return render(request , 'charts.html')


# Authentification Views

def Registration(request):
    pass

def Login(request):
    pass

def Logout(request):
    pass

def Registration(request):
    pass

def Registration(request):
    pass

def Registration(request):
    pass
