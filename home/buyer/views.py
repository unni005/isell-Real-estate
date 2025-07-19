from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from seller.models import Property
from .models import VisitBooking
from .forms import VisitBookingForm
from django.contrib.auth.decorators import login_required



def buyer_login(request): # vieww for seller login 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('buyer:dashboard')
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'buyer/login.html')

def buyer_logout(request):      # logout functionallity view
    logout(request)
    return redirect('role_selection')

def buyer_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'Passwords do not match')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
        else:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            messages.success(request, 'Account created successfully')
            return redirect('buyer:login')

    return render(request, 'buyer/register.html')



@login_required
def buyer_dashboard(request):
    properties = Property.objects.all()

    property_type = request.GET.get('property_type')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if property_type:
        properties = properties.filter(property_type=property_type)

    if min_price:
        properties = properties.filter(price__gte=min_price)

    if max_price:
        properties = properties.filter(price__lte=max_price)

    return render(request, 'buyer/dashboard.html', {
        'properties': properties,
    })
@login_required
def book_visit(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    if request.method == 'POST':
        form = VisitBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.buyer = request.user
            booking.property = property
            booking.save()
            messages.success(request, 'Visit booked successfully!')
            return redirect('buyer:dashboard')
    else:
        form = VisitBookingForm()

    return render(request, 'buyer/book_visit.html', {'form': form, 'property': property})





# for api 
from rest_framework import viewsets
from .models import VisitBooking
from .serializers import VisitBookingSerializer

class VisitBookingViewSet(viewsets.ModelViewSet):
    queryset = VisitBooking.objects.all()
    serializer_class = VisitBookingSerializer



