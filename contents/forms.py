from django import forms
from .models import Category, bloodbank, blooddonors,places
class PostSearchForm(forms.Form):
    q=forms.CharField()
    c=forms.ModelChoiceField(
         queryset=Category.objects.all().order_by('name'))
    l=forms.ModelChoiceField(
         queryset=places.objects.all())  
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['c'].label = ''
        self.fields['c'].required = False
        self.fields['c'].label = 'Category'
        self.fields['l'].required = False
        self.fields['l'].label = 'location_in_bangalore'
        self.fields['q'].label = 'Search For'
        self.fields['q'].widget.attrs.update(
            {'class': 'form-control'})

class bloodbanksearchForm(forms.Form):
     x=forms.ModelChoiceField(
          queryset= bloodbank.objects.all().order_by('pincode')) 
     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['x'].label = 'search by pincode'

class blooddonorsearchForm(forms.Form):
     y=forms.ModelChoiceField(
          queryset= blooddonors.objects.all().order_by('blood_group')) 
     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['y'].label = 'search by blood--group'