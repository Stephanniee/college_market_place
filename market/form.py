from django import forms
from .models import Product
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

class Form(forms.ModelForm):
    
    title = forms.CharField(max_length=100)

    price = forms.DecimalField(max_digits=10, decimal_places=2)
    
    description = forms.Textarea()
    image = CloudinaryField('image', default='placeholder')

    class Meta:
        model = Product
        fields = ['title', 'price', 'category', 'condition', 'description', 'image']