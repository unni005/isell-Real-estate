
from django.db import models
from django.contrib.auth.models import User
from seller.models import Property



class VisitBooking(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    visit_date = models.DateField()
    visit_time = models.TimeField(null=True, blank=True)
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')  # ✅
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.buyer.username} - {self.property.title} on {self.visit_date}"



class BuyerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    address = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='buyer_profiles/', blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"Buyer: {self.user.username}"
    

   
