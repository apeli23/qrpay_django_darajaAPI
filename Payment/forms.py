from django import forms 
from .models import Transactions
from django.db import models
from django.db import models


class transactionsForm(forms.ModelForm  ):
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
	# code = forms.ImageField()
	class Meta:
		model = Transactions
		fields = ['contact','amount','code']
