from django import forms 
from .models import Transactions
from django.db import models
from django.db import models


class inputcontact_Form(forms.ModelForm):
    contact = forms.IntegerField(required=True, widget=forms.TextInput(
		attrs={
			'class':'form-control',			 
		}))
     
    class Meta:
	    model = Transactions
	    fields = ('contact',)

class transactionsForm(forms.Form  ):
	contact = forms.IntegerField( 
		label='phonenumber',
        required=True,
        widget=forms.TextInput(
				attrs={
					'class':'form-control', 
			 
		}))
	amount = forms.IntegerField(required=True,widget=forms.TextInput(
		attrs={
			'class':'form-control',	
			 'value':1, 
		}))
	class Meta:
		model = Transactions
		fields = '__all__'
