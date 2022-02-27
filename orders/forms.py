from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'city']
        labels = {'first_name': 'First Name', 'Email': 'Your email', 'phone_number': 'Phone number'}