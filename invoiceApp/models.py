from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from num2words import num2words
from decimal import *
# Create your models here.

payemnt_status = (
			('payment completed','Payment Completed'),
			('payment pending','Payment Pending'),
			('partial payment pending','Partial Payment Pending'),
			('not initiated','Not Initiated'),
	)

invoice_type_options = (
			('interstate','Interstate'),
			('intrastate','Intrastate')
	)

STATUS_CHOICES = (
	('draft', 'Draft'),
	('published', 'Published'),
)

#
class country(models.Model):
	country_name = models.CharField(max_length=256, null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.country_name or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Country Name List'

#
class state(models.Model):
	state_name = models.CharField(max_length=256, null=True, blank=True)
	country_name = models.ForeignKey(country,related_name='countryS', on_delete=models.CASCADE, null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.state_name or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'State Name List'

#
class city(models.Model):
	city_Name = models.CharField(max_length=256, null=True, blank=True)
	state_name = models.ForeignKey(state,related_name='stateC', on_delete=models.CASCADE, null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.city_Name or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'City Name List'

#
class address(models.Model):
	address_line_1 = models.CharField(max_length=256)
	address_line_2 = models.CharField(max_length=256, null=True, blank=True)
	city_name = models.ForeignKey(city,related_name='cityA', on_delete=models.CASCADE,null=True, blank=True)
	pincode = models.BigIntegerField(null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.address_line_1 or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Address List'

class our_bank_details(models.Model):
	account_name = models.CharField(max_length=256)
	account_number =models.BigIntegerField()
	bank_name = models.CharField(max_length=256)
	branch = models.CharField(max_length=256)
	IFSC_code = models.CharField(max_length=50)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.account_name or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Our Bank Details'

#
class Terms_and_conditions(models.Model):
	terms_and_condition = models.TextField()
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.terms_and_condition or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Our Terms And Conditions'


#
class our_office_location(models.Model):
	image = models.ImageField(upload_to='ourOfficeLocation/Image/',null=True, blank=True)
	company_name = models.CharField(max_length=256)
	GST_IN = models.CharField(max_length=256)
	CIN = models.CharField(max_length=256, null=True, blank=True)
	Pan_no = models.CharField(max_length=256, null=True, blank=True)
	address = models.ForeignKey(address, related_name='addressesOOL', on_delete=models.CASCADE)
	email_id = models.EmailField(null=True, blank=True)
	mobile_number = models.BigIntegerField(null=True,blank=True)
	website = models.CharField(max_length=256, null=True, blank=True)
	signature = models.ImageField(upload_to='ourOfficeLocation/signature/',null=True, blank=True)
	bank_details = models.ForeignKey(our_bank_details,related_name='bank_detailsOOL',on_delete=models.SET_NULL,null=True, blank=True)
	terms_and_condition = models.ForeignKey(Terms_and_conditions, related_name='Terms_and_conditionOOL', on_delete=models.SET_NULL, blank=True, null=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.company_name or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Our Office Location'

#
class client_profile(models.Model):
	client_name = models.CharField(max_length=256)
	GST = models.CharField(max_length=256)
	address = models.ForeignKey(address,related_name='addressCP', on_delete=models.CASCADE)
	email_id = models.EmailField(null=True, blank=True)
	mobile_number = models.BigIntegerField(null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.client_name or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Client Profile'


class product_and_services_profile(models.Model):
	title = models.CharField(max_length=256)
	description = models.TextField(null=True, blank=True)
	HSN= models.PositiveIntegerField()
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.title or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Product And Services Profile'

#
class invoice_details(models.Model):
	client = models.ForeignKey(client_profile, related_name='clientID', on_delete=models.CASCADE)
	our_office_info = models.ForeignKey(our_office_location, related_name='our_infoID', on_delete=models.CASCADE)
	invoice_number = models.CharField(max_length=256, unique=True)
	invoice_date = models.DateField()
	due_date = models.DateField(null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=25, choices=payemnt_status, default='not initiated')

	def __str__(self):
		return str(self.invoice_number) or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Invoice Details'

#
class billed_product(models.Model):
	invoice_info = models.ForeignKey(invoice_details, related_name='invoice_infoBP', on_delete=models.CASCADE)
	product_and_service = models.ForeignKey(product_and_services_profile, related_name='product_and_serviceBP', on_delete=models.CASCADE)
	quantity = models.DecimalField(decimal_places=2 , max_digits=20)
	price_per_product = models.DecimalField(decimal_places=4 , max_digits=20)
	amount = models.DecimalField(decimal_places=4 , max_digits=20, null=True, blank=True)
	applicable_GST = models.DecimalField(decimal_places=2, max_digits=4 ,max_length=256)
	applicable_GST_amount = models.DecimalField(decimal_places=4, max_digits=20 ,max_length=256, null=True, blank=True)
	applicable_GST_amount_plus_GST = models.DecimalField(decimal_places=4, max_digits=20 ,max_length=256, null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return str(self.invoice_info) or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Billed Product'

	def save(self):
		if self.quantity:
			self.amount = (self.price_per_product * self.quantity)
		else:
			self.amount = (self.price_per_product)
		if self.applicable_GST:
			self.applicable_GST_amount = (self.amount * (self.applicable_GST / 100))
		if self.applicable_GST_amount:
			self.applicable_GST_amount_plus_GST = self.applicable_GST_amount + self.amount
		super(billed_product, self).save()