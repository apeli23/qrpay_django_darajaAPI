from django import forms 
from django.db import models
from .models import Transactions

 
 
class transactionsForm(forms.ModelForm  ):
	# contact field form
	contact = forms.IntegerField( 
		label='Enter phonenumber :',
        required=True,
        widget=forms.TextInput(
				attrs={
					'class':'form-control',	
					'placeholder':'254...',			 
				}
			)
		)
	# amountfield form.Default value set to 1. This passes 1 as the default amount received 
	# in cosideration of the research purpose of this project. 
	amount = forms.IntegerField(required=True,widget=forms.HiddenInput(
		attrs={
			'class':'form-control',	
			 'value':1, 
		}))
		# code field form
	code = forms.ImageField(required=False,widget=forms.HiddenInput())

	# instanciate Transactions model class
	class Meta:
		model = Transactions
		fields = '__all__'
 