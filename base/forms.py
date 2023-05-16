from django import forms

class ItemSearchForm(forms.Form):
    unique_code = forms.CharField(label='Enter Unique Code')
