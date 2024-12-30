from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import TransitData,VehicleForm
from .models import TransitAgency
from django.shortcuts import get_object_or_404, render
# from .models import Products
# from .forms import student_details
# from django.views.generic import ListView,DetailView
# from django.views.generic.edit import UpdateView
# from django.urls import reverse_lazy

def tharun(request):
    return render(request,'add_details.html')

def add_transit_agency(request):
    if request.method == 'POST':
        form = TransitData(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('/')  # Redirect to a success page or another view
    else:
        form = TransitData()  
    

    return render(request, 'add_details.html', {'form': form})

def display_transit_agencies(request):
    role = request.session.get('role', None)
    if request.method == "POST":
        selected_vehicle = request.POST.get('selected_option')  # Get the selected value
    if selected_vehicle == "customer":
        transit_agencies = TransitAgency.objects.all()
        context={
            'transit_agencies' : transit_agencies,
            'role' : role,
            }
        return render(request, 'listoftransit.html', context)
    # if role=="admin":
    #     return render(request, 'listoftransit.html', {'transit_agencies': transit_agencies})
    # if role=="user":
    #     return render(request, 'transitlist.html', {'transit_agencies': transit_agencies})
    # return render(request, 'listoftransit.html', context)
      # Render page_a.html if "a" is selected
    elif selected_vehicle == "vehicletypes":
        transit_agencies = TransitAgency.objects.all()
        context={
            'transit_agencies' : transit_agencies,
            'role' : role,
            }
        return render(request, 'vehiclepage.html', context)
    # if role=="admin":
    #     return render(request, 'listoftransit.html', {'transit_agencies': transit_agencies})
    # if role=="user":
    #     return render(request, 'transitlist.html', {'transit_agencies': transit_agencies})
    

def login_page(request):
    return render(request,'loginform.html')

#login code
ADMIN_CREDENTIALS = {"username": "admin", "password": "admin123"}
USER_CREDENTIALS = {"username": "user", "password": "user123"}
role=""
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        if username == ADMIN_CREDENTIALS["username"] and password == ADMIN_CREDENTIALS["password"]:
            request.session['role'] = 'admin'
            role="admin"
            return redirect('/se/')
        elif username == USER_CREDENTIALS["username"] and password == USER_CREDENTIALS["password"]:
            request.session['role'] = 'user'
            role="user"
            return redirect('/se/')
        else:
            return render(request, 'loginform.html', {'error': 'Invalid credentials'})
    
    return render(request, 'loginform.html')

def dashboard(request):
    role = request.session.get('role', None)
    if role == 'admin':
        return redirect('/get/') # Admin-specific dashboard
    elif role == 'user':
        return render(request, 'transitlist.html')  # User-specific dashboard
    else:
        return redirect('login') 
    
    #sewebtool home page

def sehome(request):
    return render(request,'sehome.html')
#list
def listoftranist(request):
    return render(request,'listoftransit.html')

#detailview
# from django.views.generic.detail import DetailView

# class TransitAgencyDetailView(DetailView):
#     model = TransitAgency
#     template_name = 'singlevehicle_detail.html'
#     context_object_name = 'transit_agency'


def transit_agency_detail(request, pk):
    transit_agency = get_object_or_404(TransitAgency, pk=pk)
    role = request.session.get('role', None)
    return render(request, 'singlevehicle_detail.html', {'transit_agency': transit_agency, 'role': role})

def add_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')  # Redirect to another view after saving
    else:
        form = VehicleForm()

    return render(request, 'add_vehicle.html', {'form': form})


    
