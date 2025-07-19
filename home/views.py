
from django.shortcuts import render, redirect

def role_selection(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        if role == 'buyer':
            return redirect('buyer:login')  # named URL pattern
        elif role == 'seller':
            return redirect('seller:login')
    return render(request, 'home/role_selection.html')
