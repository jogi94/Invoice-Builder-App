from django.urls import path
from . import views

app_name = 'invoiceApp'

urlpatterns = [
	path('', views.billedProductView, name='billedProductUrl'),
	path('tax-invoice/<id>/', views.taxInvoiceView, name='taxInvoiceUrl'),
	#
	path('address-listing/', views.addressListingView, name='addressListingUrl'),
	path('address-add/', views.addressAddEditView, name='addressAddUrl'),
	path('address-edit/<id>/', views.addressAddEditView, name='addressEditUrl'),
	#
	path('terms-and-condition/', views.termsAndConditionView, name='termsAndConditionUrl'),
	path('terms-and-condition-add/', views.termsAndConditionAddEditView, name='termsAndConditionAddUrl'),
	path('terms-and-condition-edit/<id>/', views.termsAndConditionAddEditView, name='termsAndConditionEditUrl'),
	#
	path('bank-listing/', views.bankListingView, name='bankListingUrl'),
	path('bank-detail-add/', views.bankDetailAddEditView, name='bankDetailAddUrl'),
	path('bank-detail-edit/<id>/', views.bankDetailAddEditView, name='bankDetailEditUrl'),
	#
	path('client-listing/', views.clientListingView, name='clientListingUrl'),
	path('add-client/', views.clientAddEditView, name='clientAddUrl'),
	path('edit-client/<id>/', views.clientAddEditView, name='clientEditUrl'),
	#
	path('office-location-listing/', views.officeLocationListingView, name='officeLocationListingUrl'),
	path('add-office-location/', views.officeLocationAddEditView, name='officeLocationsAddUrl'),
	path('edit-office-location/<id>', views.officeLocationAddEditView, name='officeLocationsEditUrl'),
	#
	path('product-and-services-listing/', views.productAndServicesListingView, name='productAndServicesListingUrl'),
	path('add-product-and-services/', views.productAndServicesAddEditView, name='addProductAndServicesUrl'),
	path('edit-View-Product-And-Services/<id>/', views.productAndServicesAddEditView, name='editViewProductAndServicesUrl'),
	#
	path('invoice-listing/', views.invoiceListingView, name='invoiceListingUrl'),
	path('invoice-add/', views.invoiceAddEditView, name='invoiceAddUrl'),
	path('invoice-edit/<id>/', views.invoiceAddEditView, name='invoiceEditUrl'),
	#
	path('billed-product-add/', views.billedProductAddEditView, name='billedProductAddUrl'),
	path('billed-product-edit/<id>/', views.billedProductAddEditView, name='billedProductEditUrl'),
	#submit url
	path('add-edit-address-submit/', views.addEditAddressSubmitView, name='addEditAddressSubmitUrl'),
	path('terms-and-condition-add-edit-submit/', views.termsAndConditionAddEditSubmitView, name='termsAndConditionAddEditSubmitUrl'),
	path('our-bank-details-add-edit-submit/', views.ourBankDetailsAddEditSubmitView, name='ourBankDetailsAddEditSubmitUrl'),
	path('add-clients-submit/', views.addClientsSubmitView, name='addClientsSubmitUrl'),
	path('office-location-add-edit-view-submit/', views.officeLocationAddEditViewSubmitView, name='officeLocationAddEditViewSubmitUrl'),
	path('product-and-services-add-edit-submit-Form/', views.productAndServicesAddEditSubmitFormView, name='productAndServicesAddEditSubmitFormUrl'),
	path('invoice-add-edit-submit/', views.invoiceAddEditSubmitView, name='invoiceAddEditSubmitUrl'),
	path('billed-product-submit/', views.billedProductSubmitView, name='billedProductSubmitUrl'),
	#delete
	path('delete-item/', views.deleteView, name='deleteUrl'),
	path('search/', views.searchBarView, name='searchBarUrl'),
]