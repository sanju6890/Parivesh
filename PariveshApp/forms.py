from django import forms
from django.forms import widgets
from .models import Plantation

class AddPlantForm(forms.ModelForm):
    class Meta:
        model = Plantation
        fields = ('plant_name', 'plant_pic','plant_loc', 'remarks')

        widgets = {
            'plant_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Like Eucalyptus Plant...'}),
            'plant_loc': forms.URLInput(attrs={'class':'form-control','placeholder':'Paste the google map location URL here...'}),
            'planter': forms.TextInput(attrs={'class':'form-control','type':'hidden'}),
            # 'plant_pic': forms.ImageField(attrs={'class':'form-control'}),
            'remarks': forms.Textarea(attrs={'class':'form-control','placeholder':'Write a short & meaningful remark here...'}),
        }