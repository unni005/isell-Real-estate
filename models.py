
from django.db import models
from django.contrib.auth.models import User

PROPERTY_TYPE_CHOICES = (
    ('flat', 'Flat'),
    ('house', 'House'),
    ('land', 'Land'),
    ('villa', 'Villa'),
    ('apartment', 'Apartment'),
)


class Property(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES, default='flat')
    price = models.DecimalField(max_digits=12, decimal_places=2)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='property_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
class SellerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    address = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='seller_profiles/', blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"Seller: {self.user.username}"