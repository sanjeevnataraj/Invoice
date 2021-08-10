from django.contrib import admin

# Register your models here.

from .models import Collections,Invoices
# 
# admin.site.register(Collections)
# admin.site.register(Invoices)


@admin.register(Collections)
class CollectionAdmin(admin.ModelAdmin):
    search_fields = ("reference", )

@admin.register(Invoices)
class InvoiceAdmin(admin.ModelAdmin):
    search_fields = ("reference", )