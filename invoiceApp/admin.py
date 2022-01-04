from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django_summernote.admin import SummernoteModelAdmin
from .models import *



#
def approvePost(modeladmin, request, queryset):
	for post in queryset:
		post.status = 'Published'
		post.save()
approvePost.short_description = 'Approve Selected'

#
def draftPost(modeladmin, request, queryset):
	for post in queryset:
		post.status = 'Draft'
		post.save()
draftPost.short_description = 'Draft Selected'


#
@admin.register(country)
class countryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	list_display = ('country_name', 'publish', 'status', )
	list_filter = ('status', )

	actions = [approvePost, draftPost,]
	def save_model(self, request, obj, form, change):
		obj.analyst = request.user
		super().save_model(request, obj, form, change)

#
@admin.register(state)
class stateAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	list_display = ('state_name', 'country_name', 'publish', 'status', )
	list_filter = ('status', )

	actions = [approvePost, draftPost,]
	def save_model(self, request, obj, form, change):
		obj.analyst = request.user
		super().save_model(request, obj, form, change)

#
@admin.register(city)
class cityAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	list_display = ('city_Name', 'state_name', 'publish', 'status', )
	list_filter = ('status', )

	actions = [approvePost, draftPost,]
	def save_model(self, request, obj, form, change):
		obj.analyst = request.user
		super().save_model(request, obj, form, change)

#
@admin.register(address)
class addressAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	list_display = ('address_line_1', 'address_line_2', 'city_name', 'pincode', 'publish', 'status', )
	list_filter = ('status', )

	actions = [approvePost, draftPost,]
	def save_model(self, request, obj, form, change):
		obj.analyst = request.user
		super().save_model(request, obj, form, change)

#
@admin.register(Terms_and_conditions)
class Terms_and_conditionsAdmin(ImportExportModelAdmin, SummernoteModelAdmin, admin.ModelAdmin):
	summernote_fields = ('terms_and_condition',)
	list_display = ('terms_and_condition', 'publish', 'status', )
	list_filter = ('status', )

	actions = [approvePost, draftPost,]
	def save_model(self, request, obj, form, change):
		obj.analyst = request.user
		super().save_model(request, obj, form, change)

#
@admin.register(our_bank_details)
class our_bank_detailsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	list_display = ('account_name', 'account_number', 'bank_name', 'branch', 'IFSC_code', 'publish', 'status', )
	list_filter = ('status', )

	actions = [approvePost, draftPost,]
	def save_model(self, request, obj, form, change):
		obj.analyst = request.user
		super().save_model(request, obj, form, change)

#
@admin.register(our_office_location)
class our_office_locationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	list_display = ('company_name', 'mobile_number', 'GST_IN', 'publish', 'status', )
	list_filter = ('status', )
	# search_fields = ['name']

	actions = [approvePost, draftPost,]
	def save_model(self, request, obj, form, change):
		obj.analyst = request.user
		super().save_model(request, obj, form, change)

#
@admin.register(client_profile)
class client_profileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	list_display = ('client_name', 'mobile_number', 'GST', 'publish', 'status', )
	list_filter = ('status', )
	# search_fields = ['name']

	actions = [approvePost, draftPost,]
	def save_model(self, request, obj, form, change):
		obj.analyst = request.user
		super().save_model(request, obj, form, change)



#
@admin.register(product_and_services_profile)
class product_and_services_profileAdmin(ImportExportModelAdmin, SummernoteModelAdmin, admin.ModelAdmin):
	summernote_fields = ('description',)
	list_display = ('title','description', 'HSN', 'publish', 'status', )
	list_filter = ('status', )
	search_fields = ['title', 'description',]

	actions = [approvePost, draftPost,]
	def save_model(self, request, obj, form, change):
		obj.analyst = request.user
		super().save_model(request, obj, form, change)


#
class billedAdmin(admin.StackedInline):
	model = billed_product

#
@admin.register(invoice_details)
class invoice_detailsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	list_display = ('invoice_number', 'invoice_date', 'client', 'publish', 'status', )
	list_filter = ('status', )
	inlines = [billedAdmin]

	actions = [approvePost, draftPost,]
	def save_model(self, request, obj, form, change):
		obj.analyst = request.user
		super().save_model(request, obj, form, change)

#
@admin.register(billed_product)
class billed_productAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	pass
	# list_display = ('product_and_service', 'amount', 'publish', 'status', )
	# list_filter = ('status', )
	# # search_fields = ['name']

	# actions = [approvePost, draftPost,]
	# def save_model(self, request, obj, form, change):
	# 	obj.analyst = request.user
	# 	super().save_model(request, obj, form, change)

















