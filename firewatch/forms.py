from django import forms
from .models import ImageUpload

class PreviewImage(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = '__all__'