from django import forms
from django.forms import ModelForm
from .models import Submit
# from django.core.exceptions import ValidationError




class SubmitForm(ModelForm):
	# def clean_town(self):
	# 	data = self.cleaned_data['city']
	# 	listOfStrings = ['Hi' , 'hello', 'at', 'this', 'there', 'from']
	# 	if listOfStrings in data:


	# 		raise ValidationError("Try again")
	# 	return data

	   

	class Meta:

		model=Submit
		fields=['email','name','address1','address2','city']


		widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
			'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
			'address1': forms.TextInput(attrs={'placeholder': 'Address1', 'class': 'form-control'}),
			'address2': forms.TextInput(attrs={'placeholder': 'Address2', 'class': 'form-control'}),
			'city': forms.TextInput(attrs={'placeholder': 'City','class': 'form-control'}),
            # 'description': forms.Textarea(
            #     attrs={'placeholder': 'Enter description here'}),
        }
		