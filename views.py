

from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.forms import UserChangeForm 
from django.contrib.auth.decorators import login_required
from .models import Property
from .forms import PropertyForm
from buyer.models import VisitBooking


def seller_login(request): # vieww for seller login 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('seller:dashboard')
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'seller/login.html')

def seller_register(request):      # views for non registered seller
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
            return redirect('seller:login')

    return render(request, 'seller/register.html')


def seller_logout(request):
    logout(request)
    return redirect('role_selection') 

@login_required
def seller_dashboard(request):
    properties = Property.objects.filter(seller=request.user)
    property_count = properties.count()

    return render(request, 'seller/dashboard.html', {
        'properties': properties,
        'property_count': property_count,
    })

@login_required
def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            prop = form.save(commit=False)
            prop.seller = request.user
            prop.save()
            return redirect('seller:dashboard')
    else:
        form = PropertyForm()
    return render(request, 'seller/add_property.html', {'form': form})

@login_required
def edit_property(request, property_id):
    property = get_object_or_404(Property, id=property_id, seller=request.user)
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property)
        if form.is_valid():
            form.save()
            return redirect('seller:dashboard')
    else:
        form = PropertyForm(instance=property)
    return render(request, 'seller/edit_property.html', {'form': form, 'property': property})

@login_required
def delete_property(request, property_id):
    property = get_object_or_404(Property, id=property_id, seller=request.user)
    if request.method == 'POST':
        property.delete()
        return redirect('seller:dashboard')
    return render(request, 'seller/delete_property.html', {'property': property})



@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('seller:dashboard')
    else:
        form = UserChangeForm(instance=request.user)

    return render(request, 'seller/edit_profile.html', {'form': form})


@login_required
def view_bookings(request):
    seller_properties = Property.objects.filter(seller=request.user)

    # Get sort key from query params, default to visit_date
    sort_by = request.GET.get('sort', '-visit_date')

    # Validate sort key (to prevent malicious input)
    allowed_sorts = ['visit_date', '-visit_date', 'status', '-status']
    if sort_by not in allowed_sorts:
        sort_by = '-visit_date'

    bookings = VisitBooking.objects.filter(property__in=seller_properties).order_by(sort_by)

    return render(request, 'seller/view_bookings.html', {
        'bookings': bookings,
        'sort_by': sort_by
    })

@login_required
def complete_booking(request, booking_id):
    booking = get_object_or_404(VisitBooking, id=booking_id, property__seller=request.user)
    booking.status = 'completed'
    booking.save()
    messages.success(request, "Booking marked as completed.")
    return redirect('seller:view_bookings')


@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(VisitBooking, id=booking_id)

    # Ensure the booking belongs to this seller
    if booking.property.seller != request.user:
        messages.error(request, "Unauthorized access.")
        return redirect('seller:view_bookings')

    booking.delete()
    messages.success(request, "Booking deleted successfully.")
    return redirect('seller:view_bookings')


from rest_framework import viewsets
from .models import Property
from .serializers import PropertySerializer

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer