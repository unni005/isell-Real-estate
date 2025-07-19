from django import forms
from .models import VisitBooking


class VisitBookingForm(forms.ModelForm):
    class Meta:
        model = VisitBooking
        fields = ['visit_date', 'visit_time', 'contact_number', 'email', 'message']
        widgets = {
            'visit_date': forms.DateInput(attrs={'type': 'date'}),
            'visit_time': forms.TimeInput(attrs={'type': 'time'}),
            'message': forms.Textarea(attrs={'rows': 3}),
            'contact_number': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
        }


        