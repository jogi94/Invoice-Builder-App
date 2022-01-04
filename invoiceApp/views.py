from django.shortcuts import render, HttpResponse , redirect, get_object_or_404,redirect
from django.contrib import messages
from .models import *
from num2words import num2words
from .forms import *
from django.urls import reverse
from django.db.models import Q

# Create your views here.
def billedProductView(request):
	pageFlag = 'billed'
	if request.user.is_superuser:
		try:
			invoiceDetail = invoice_details.objects.all().order_by('invoice_number')
		except:
			return HttpResponse('Server is on maintainance')
	context = {
			'pageFlag':pageFlag,
			'invoiceDetail':invoiceDetail,
	}
	return render(request, 'UI/billed-products.html', context)



#
def billedProductAddEditView(request, id=None):
	if request.user.is_superuser:
		billedProductFormCreate = billedProductForm()
	elif request.user.is_staff:
		billedProductFormCreate = billedProductStuffForm()
	if request.GET.get('action') == 'add':
		pageFlag = 'add'
	elif request.GET.get('action') == 'edit':
		pageFlag = 'edit'
	else:
		pageFlag = 'view'
	if id:
		billedProducts = get_object_or_404(billed_product, id=id)
		print(billedProducts)
	else:
		billedProducts = None
	context = {
		'billedProducts':billedProducts,
		'billedProductFormCreate':billedProductFormCreate,
		'pageFlag':pageFlag,
	}
	return render(request, 'UI/billedProductAddEdit.html', context)


#
def taxInvoiceView(request , id=id):
	invoiceInst = get_object_or_404(invoice_details, id=id)
	billedProducts = billed_product.objects.filter(invoice_info=invoiceInst)
	CGST = 0
	SGST = 0
	IGST = 0
	total_Amount = 0
	grand_total = 0
	for item in billedProducts:
		getCGST = Decimal(0)
		getSGST = Decimal(0)
		getIGST = Decimal(0)
		if (item.invoice_info.our_office_info.address.city_name.state_name == item.invoice_info.client.address.city_name.state_name):	
			if item.applicable_GST_amount:
				getCGST += item.applicable_GST_amount/2
				getSGST += item.applicable_GST_amount/2
				IGST += 0
		elif (item.invoice_info.our_office_info.address.city_name.state_name != item.invoice_info.client.address.city_name.state_name):
			if item.applicable_GST_amount:
				getIGST += item.applicable_GST_amount
				getCGST += 0
				getSGST += 0
		else:
			getCGST += 0
			getSGST += 0
			getIGST += 0
		CGST += getCGST
		SGST += getSGST
		IGST += getIGST
		if item.amount:
			total_Amount += item.amount
		print(item.invoice_info.our_office_info.address.city_name.state_name == item.invoice_info.client.address.city_name.state_name)
	grand_total += (total_Amount+CGST+SGST+IGST)
	grandTotal_inWords = num2words(grand_total)
	print(CGST,SGST,IGST,total_Amount,grand_total)
	context = {
		'invoiceInst': invoiceInst,
		'billedProducts': billedProducts,
		'CGST':CGST,
		'SGST':SGST,
		'IGST':IGST,
		'grand_total':grand_total,
		'grandTotal_inWords':grandTotal_inWords,
			}
	return render(request, 'UI/invoiceDesigning.html', context)

#
def billedProductSubmitView(request, id=None):
	dataID = request.POST.get('dataID')
	parentPK = request.GET.get('invoice')
	if parentPK:
		parentInst = invoice_details.objects.get(pk=parentPK)
	else:
		parentInst = None
	modelInstance = None
	redirectTo = request.POST.get('redirectUrl')
	if dataID:
		modelInstance = get_object_or_404(billed_product, pk=dataID)
	else :
		modelInstance = None
	if request.method == 'POST':
		if request.user.is_superuser:
			submitFormImage = billedProductForm(request.POST, request.FILES, instance=modelInstance)
		elif request.user.is_staff:
			submitFormImage = billedProductStuffForm(request.POST, request.FILES, instance=modelInstance)
		if submitFormImage.is_valid():
			cd = submitFormImage.save(commit=False)
			if request.user.is_authenticated:
				cd.analyst = request.user
			if parentInst:
				cd.invoice_info = parentInst
			cd.save()
			submitFormImage.save_m2m()
			cd.refresh_from_db()
			messages.success(request, 'Product is added Successfully')
		else:
			messages.error(request, 'Wrong Input Data, Please check An Error occurred')
	return redirect(redirectTo)


#
def addressListingView(request):
	pageFlag = 'addresses'
	addressList = address.objects.all().order_by('address_line_1')
	context = {
		'addressList':addressList,
		'pageFlag':pageFlag,
	}
	return render(request, 'UI/addressListing.html', context)

def addressAddEditView(request,id=None):
	form = addEditAddressSubmitForm()
	if request.GET.get('action') == 'add':
		pageFlag = 'add'
	elif request.GET.get('action') == 'edit':
		pageFlag = 'edit'
	else:
		pageFlag = 'view'
	if id:
		addressDetails = get_object_or_404(address, id=id)
	else:
		addressDetails = None
	context = {
		'form':form,
		'addressDetails':addressDetails,
		'pageFlag':pageFlag,
	}
	return render(request, 'UI/addressAddEdit.html', context)

#
def addEditAddressSubmitView(request, id=None):
	dataID = request.POST.get('dataID')
	modelInstance = None
	redirectTo = request.POST.get('redirectUrl')
	if dataID:
		modelInstance = get_object_or_404(address, pk=dataID)
	else :
		modelInstance = None
	if request.method == 'POST':
		submitFormImage = addEditAddressSubmitForm(request.POST, request.FILES, instance=modelInstance)
		if submitFormImage.is_valid():
			cd = submitFormImage.save(commit=False)
			if request.user.is_authenticated:
				cd.analyst = request.user
			cd.save()
			submitFormImage.save_m2m()
			cd.refresh_from_db()
			messages.success(request, 'Address is added Successfully.')
		else:
			messages.error(request, 'Wrong Input Data, Please check An Error occurred')
	return redirect(redirectTo)


def bankListingView(request):
	pageFlag = 'bank'
	bankDetails = our_bank_details.objects.all().order_by('bank_name')
	context = {
		'pageFlag':pageFlag,
		'bankDetails':bankDetails,
	}
	return render(request, 'UI/bankListing.html', context)


#
def bankDetailAddEditView(request,id=None):
	form = ourBankDetailsForm()
	if request.GET.get('action') == 'add':
		pageFlag = 'add'
	elif request.GET.get('action') == 'edit':
		pageFlag = 'edit'
	else:
		pageFlag = 'view'
	if id:
		bankDetails = get_object_or_404(our_bank_details, id=id)
	else:
		bankDetails = None
	context = {
		'form':form,
		'bankDetails':bankDetails,
		'pageFlag':pageFlag,
	}
	return render(request, 'UI/bankDetailsAddEdit.html', context)

#
def ourBankDetailsAddEditSubmitView(request, id=None):
	dataID = request.POST.get('dataID')
	modelInstance = None
	redirectTo = request.POST.get('redirectUrl')
	if dataID:
		modelInstance = get_object_or_404(our_bank_details, pk=dataID)
	else :
		modelInstance = None
	if request.method == 'POST':
		submitFormImage = ourBankDetailsForm(request.POST, request.FILES, instance=modelInstance)
		if submitFormImage.is_valid():
			cd = submitFormImage.save(commit=False)
			if request.user.is_authenticated:
				cd.analyst = request.user
			cd.save()
			submitFormImage.save_m2m()
			cd.refresh_from_db()
			messages.success(request, 'Bank details are added Successfully.')
		else:
			messages.error(request, 'Wrong Input Data, Please check An Error occurred')
	return redirect(redirectTo)

def termsAndConditionView(request):
	pageFlag = 'tc'
	termsAndcondition = Terms_and_conditions.objects.all().order_by('terms_and_condition')
	context = {
		'pageFlag':pageFlag,
		'termsAndcondition':termsAndcondition,
	}
	return render(request, 'UI/termsAndConditionListing.html', context)

def termsAndConditionAddEditView(request,id=None):
	form = termsAndConditionForm()
	if request.GET.get('action') == 'add':
		pageFlag = 'add'
	elif request.GET.get('action') == 'edit':
		pageFlag = 'edit'
	else:
		pageFlag = 'view'
	if id:
		termsAndCondition = get_object_or_404(Terms_and_conditions, id=id)
	else:
		termsAndCondition = None
	context = {
		'form':form,
		'termsAndCondition':termsAndCondition,
		'pageFlag':pageFlag,
	}
	return render(request, 'UI/termsAndConditionAddEdit.html', context)

#
def termsAndConditionAddEditSubmitView(request, id=None):
	dataID = request.POST.get('dataID')
	modelInstance = None
	redirectTo = request.POST.get('redirectUrl')
	if dataID:
		modelInstance = get_object_or_404(Terms_and_conditions, pk=dataID)
	else :
		modelInstance = None
	if request.method == 'POST':
		submitFormImage = termsAndConditionForm(request.POST, request.FILES, instance=modelInstance)
		if submitFormImage.is_valid():
			cd = submitFormImage.save(commit=False)
			if request.user.is_authenticated:
				cd.analyst = request.user
			cd.save()
			submitFormImage.save_m2m()
			cd.refresh_from_db()
			messages.success(request, 'Terms and conditions are added Successfully.')
		else:
			messages.error(request, 'Wrong Input Data, Please check An Error occurred')
	return redirect(redirectTo)

#
def clientListingView(request):
	pageFlag = 'client'
	clients = client_profile.objects.all().order_by('client_name')
	context = {
		'pageFlag':pageFlag,
		'clients':clients,
	}
	return render(request, 'UI/clientsListing.html', context)

def clientAddEditView(request,id=None):
	form = addClientsSubmitForm()
	if request.GET.get('action') == 'add':
		pageFlag = 'add'
	elif request.GET.get('action') == 'edit':
		pageFlag = 'edit'
	else:
		pageFlag = 'view'
	if id:
		clients = get_object_or_404(client_profile, id=id)
	else:
		clients = None
	context = {
		'form':form,
		'clients':clients,
		'pageFlag':pageFlag,
	}
	return render(request, 'UI/clientsAddEdit.html', context)


#
def addClientsSubmitView(request, id=None):
	dataID = request.POST.get('dataID')
	modelInstance = None
	redirectTo = request.POST.get('redirectUrl')
	if dataID:
		modelInstance = get_object_or_404(client_profile, pk=dataID)
	else :
		modelInstance = None
	if request.method == 'POST':
		submitFormImage = addClientsSubmitForm(request.POST, request.FILES, instance=modelInstance)
		if submitFormImage.is_valid():
			cd = submitFormImage.save(commit=False)
			if request.user.is_authenticated:
				cd.analyst = request.user
			cd.save()
			submitFormImage.save_m2m()
			cd.refresh_from_db()
			messages.success(request, 'Client is added Successfully.')
		else:
			messages.error(request, 'Wrong Input Data, Please check An Error occurred')
	return redirect(redirectTo)

#
def officeLocationListingView(request):
	pageFlag = 'office'
	officeLocations = our_office_location.objects.all().order_by('company_name')
	context = {
		'pageFlag':pageFlag,
		'officeLocations':officeLocations,
	}
	return render(request, 'UI/officeLocationListing.html', context)

#
def officeLocationAddEditView(request,id=None):
	form = officeLocationAddEditViewForm()
	if request.GET.get('action') == 'add':
		pageFlag = 'add'
	elif request.GET.get('action') == 'edit':
		pageFlag = 'edit'
	else:
		pageFlag = 'view'
	if id:
		officeLocation = get_object_or_404(our_office_location, id=id)
	else:
		officeLocation = None
	
	context = {
		'officeLocation':officeLocation,
		'pageFlag':pageFlag,
		'form':form,
	}
	return render(request, 'UI/officeLocationAddEdit.html', context)


#
def officeLocationAddEditViewSubmitView(request, id=None):
	dataID = request.POST.get('dataID')
	modelInstance = None
	redirectTo = request.POST.get('redirectUrl')
	if dataID:
		modelInstance = get_object_or_404(our_office_location, pk=dataID)
	else :
		modelInstance = None
	if request.method == 'POST':
		submitFormImage = officeLocationAddEditViewForm(request.POST, request.FILES, instance=modelInstance)
		if submitFormImage.is_valid():
			cd = submitFormImage.save(commit=False)
			if request.user.is_authenticated:
				cd.analyst = request.user
			cd.save()
			submitFormImage.save_m2m()
			cd.refresh_from_db()
			messages.success(request, 'Office location is added Successfully.')
		else:
			messages.error(request, 'Wrong Input Data, Please check An Error occurred')
	return redirect(redirectTo)



#
def productAndServicesListingView(request):
	pageFlag = 'product'
	productAndServices = product_and_services_profile.objects.all().order_by('title')
	context = {
		'pageFlag':pageFlag,
		'productAndServices':productAndServices,
	}
	return render(request, 'UI/productAndServicesListing.html', context)


#
def productAndServicesAddEditView(request,id=None):
	form = productAndServicesProfileForm()
	if request.GET.get('action') == 'add':
		pageFlag = 'add'
	elif request.GET.get('action') == 'edit':
		pageFlag = 'edit'
	else:
		pageFlag = 'view'
	if id:
		productAndService = get_object_or_404(product_and_services_profile, id=id)
	else:
		productAndService = None
	context = {
		'form':form,
		'productAndService':productAndService,
		'pageFlag':pageFlag,
	}
	return render(request, 'UI/productAndServicesAddEdit.html', context)

#
def productAndServicesAddEditSubmitFormView(request, id=None):
	dataID = request.POST.get('dataID')
	modelInstance = None
	redirectTo = request.POST.get('redirectUrl')
	if dataID:
		modelInstance = get_object_or_404(product_and_services_profile, pk=dataID)
	else :
		modelInstance = None
	if request.method == 'POST':
		submitFormImage = productAndServicesProfileForm(request.POST, request.FILES, instance=modelInstance)
		if submitFormImage.is_valid():
			cd = submitFormImage.save(commit=False)
			if request.user.is_authenticated:
				cd.analyst = request.user
			cd.save()
			submitFormImage.save_m2m()
			cd.refresh_from_db()
			messages.success(request, 'Product and services are added Successfully.')
		else:
			messages.error(request, 'Wrong Input Data, Please check An Error occurred')
	return redirect(redirectTo)



#
def invoiceListingView(request):
	pageFlag = 'invoice'
	invoiceDetails = invoice_details.objects.all().order_by('invoice_number')
	invoiceInfo = {}
	for item in invoiceDetails:
		products = billed_product.objects.filter(invoice_info=item)
		invoiceInfo[item] = products
	context = {
		'pageFlag':pageFlag,
		'invoiceInfo':invoiceInfo,
	}
	return render(request, 'UI/invoiceListing.html', context)


#
def invoiceAddEditView(request,id=None):
	form = invoiceAddEditForm()
	if request.GET.get('action') == 'add':
		pageFlag = 'add'
	elif request.GET.get('action') == 'edit':
		pageFlag = 'edit'
	else:
		pageFlag = 'view'
	if id:
		invoiceDetails = get_object_or_404(invoice_details, id=id)
	else:
		invoiceDetails = None

	clientsName = client_profile.objects.all()
	officeLocations = our_office_location.objects.all()
	productAndServices = product_and_services_profile.objects.all()
	context = {
		'form':form,
		'clientsName':clientsName,
		'officeLocations':officeLocations,
		'invoiceDetails':invoiceDetails,
		'pageFlag':pageFlag,
	}
	return render(request, 'UI/invoiceAddEdit.html', context)

#
def invoiceAddEditSubmitView(request):
	if request.method == 'POST':
		# parentElement = request.POST.get('parentID')
		# parentInstance = get_object_or_404(invoice_details, pk=parentElement)
		methodType = request.POST.get('submitType')
		redirectTo = request.POST.get('redirectUrl')
		objInstID = request.POST.get('dataID')
		if methodType == 'new':
			objInst = None
		else:
			objInst = get_object_or_404(invoice_details, pk=objInstID) #Change Model Name
		objForm = invoiceAddEditForm(request.POST, instance=objInst) #Change Form Name
		print(objForm)
		if objForm.is_valid():
			cd = objForm.save(commit=False)
			# cd.invoice_info = parentInstance
			cd.save()
			cd.refresh_from_db()
			messages.success(request, 'Invoice is added Successfully') #Change Msg Accordingly
		else:
			messages.error(request, 'Please check An Error occurred')
		return redirect(redirectTo)
	return HttpResponse('Invalid Entry')

#
def deleteView(request):
	deleteFrom = request.GET.get('model')
	dataID = request.GET.get('dataID')
	redirectTo = request.GET.get('next')
	if deleteFrom == 'address':
		address.objects.get(pk=dataID).delete()
	elif deleteFrom == 'our_office_location':
		our_office_location.objects.get(pk=dataID).delete()
	elif deleteFrom == 'our_bank_details':
		our_bank_details.objects.get(pk=dataID).delete()
	elif deleteFrom == 'Terms_and_conditions':
		Terms_and_conditions.objects.get(pk=dataID).delete()
	elif deleteFrom == 'client_profile':
		client_profile.objects.get(pk=dataID).delete()
	elif deleteFrom == 'product_and_services_profile':
		product_and_services_profile.objects.get(pk=dataID).delete()
	elif deleteFrom == 'invoice_details':
		invoice_details.objects.get(pk=dataID).delete()
	elif deleteFrom == 'billed_product':
		billed_product.objects.get(pk=dataID).delete()
	elif deleteFrom == 'invoice_details':
		invoice_details.objects.get(pk=dataID).delete()
	return redirect(redirectTo)

#
def searchBarView(request):
	query = request.GET.get('searchq')
	redirectTo = request.GET.get('requestFrom')
	searchIn = request.GET.get('model')
	if query:
		if searchIn == 'our_bank_details':
			pageFlag = 'bank'
			searchObjs = our_bank_details.objects.filter(Q(account_name__icontains=query) | Q(account_number__icontains=query) | Q(bank_name__icontains=query) | Q(branch__icontains=query) | Q(IFSC_code__icontains=query)).distinct().order_by('bank_name')
	elif query:
		if searchIn == 'address':
			pageFlag = 'addresses'
			searchObjs = address.objects.filter(Q(address_line_1__icontains=query) | Q(address_line_2__icontains=query) | Q(city_name__icontains=query) | Q(pincode__icontains=query)).distinct().order_by('address_line_1')
	elif query:
		if searchIn == 'our_office_location':
			pageFlag = 'office'
			searchObjs = our_office_location.objects.filter(Q(company_name__icontains=query) | Q(GST_IN__icontains=query) | Q(CIN__icontains=query) | Q(Pan_no__icontains=query) | Q(address__icontains=query) | Q(email_id__icontains=query) | Q(mobile_number__icontains=query) | Q(website__icontains=query) | Q(bank_details__icontains=query)).distinct().order_by('company_name')
	elif query:
		if searchIn == 'client_profile':
			pageFlag = 'client'
			searchObjs = client_profile.objects.filter(Q(client_name__icontains=query) | Q(GST__icontains=query) | Q(address__icontains=query) | Q(email_id__icontains=query) | Q(mobile_number__icontains=query)).distinct().order_by('title')
	elif query:
		if searchIn == 'product_and_services_profile':
			pageFlag = 'product'
			searchObjs = product_and_services_profile.objects.filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(HSN__icontains=query)).distinct().order_by('address_line_1')
	elif query:
		if searchIn == 'invoice_details':
			pageFlag = 'invoice'
			searchObjs = invoice_details.objects.filter(Q(client__icontains=query) | Q(our_office_info__icontains=query) | Q(invoice_number__icontains=query) | Q(invoice_date__icontains=query) | Q(due_date__icontains=query)).distinct().order_by('client')
	elif query:
		if searchIn == 'invoice_details':
			pageFlag = 'billed'
			searchObjs = invoice_details.objects.filter(Q(client__icontains=query) | Q(our_office_info__icontains=query) | Q(invoice_number__icontains=query) | Q(invoice_date__icontains=query) | Q(due_date__icontains=query)).distinct().order_by('client')
	else :
		messages.error(request, 'Enter an Query to Search')
		return redirect('invoiceApp:billedProductUrl')
	context = {
		'pageFlag':pageFlag,
		'searchObjs':searchObjs,
		'query': query,
	}
	return render(request, 'UI/searchList.html', context)