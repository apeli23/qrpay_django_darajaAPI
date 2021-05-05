from django import forms
from .models import Product,Transactions

class inputcontact_Form(forms.ModelForm):
    contact = forms.IntegerField(required=True, widget=forms.TextInput(
		attrs={
			'class':'form-control',			 
		}))
     
    class Meta:
	    model = Transactions
	    fields = ('contact',)