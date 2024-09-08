from django import forms
from .models import Search

class UploadFileForm(forms.Form):
    file = forms.FileField(label='Select an Excel file')

class SearchForm(forms.ModelForm):
    pincode = forms.CharField(label='Enter Pincode', max_length=6)

    class Meta:
        model = Search
        fields = ['pincode']
