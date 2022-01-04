from django import forms
from .models import *

#
class DateInput(forms.DateInput):
	input_type = 'date'

#
class addEditAddressSubmitForm(forms.ModelForm):
	class Meta:
		model = address
		fields = ('address_line_1','address_line_2','city_name', 'pincode',)


#
class ourBankDetailsForm(forms.ModelForm):
	class Meta:
		model = our_bank_details
		fields = ('account_name','account_number','bank_name','branch','IFSC_code',)

#
class termsAndConditionForm(forms.ModelForm):
	class Meta:
		model = Terms_and_conditions
		fields = ('terms_and_condition',)



#
class addClientsSubmitForm(forms.ModelForm):
	class Meta:
		model = client_profile
		fields = ('client_name','GST','address','email_id','mobile_number',)


#
class officeLocationAddEditViewForm(forms.ModelForm):
	class Meta:
		model = our_office_location
		fields = ('company_name','GST_IN','CIN','Pan_no','address','email_id','mobile_number','website','bank_details','terms_and_condition',)


#
class productAndServicesProfileForm(forms.ModelForm):
	class Meta:
		model = product_and_services_profile
		fields = ('title','description','HSN',)

#
class invoiceAddEditForm(forms.ModelForm):
	class Meta:
		model = invoice_details
		exclude = ('publish','created','updated',)
		widgets = {
			'invoice_date': DateInput(),
			'due_date': DateInput(),
			}

#
class billedProductForm(forms.ModelForm):
	quantity = forms.IntegerField(widget=forms.NumberInput)
	class Meta:
		model = billed_product
		fields = ('product_and_service','quantity','price_per_product','applicable_GST',)

#
class billedProductStuffForm(forms.ModelForm):
	quantity = forms.IntegerField(widget=forms.NumberInput)
	class Meta:
		model = billed_product
		fields = ('product_and_service','quantity','applicable_GST',)