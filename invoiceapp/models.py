from django.db import models
import datetime
# Create your models here.


class Collections(models.Model):

	reference = models.CharField(max_length=25,blank=False,null=False) 
	collection_amount = models.IntegerField(blank=False,null=False,default=0)
	collection_date  = models.DateField(default=datetime.date.today)
	class Meta:
		verbose_name = "collection"
		verbose_name_plural = "collections"


class Invoices(models.Model):
	reference = models.CharField(max_length=25,blank=False,null=False) 
	brand_manager = models.CharField(max_length=250,blank=False,null=False) 
	customer_name = models.CharField(max_length=250,blank=False,null=False) 
	narration = models.CharField(max_length=250,blank=False,null=False) 
	amount = models.IntegerField(blank=False,null=False,default=0)
	invoice_date  = models.DateField(default=datetime.date.today)
	class Meta:
		verbose_name = "invoice"
		verbose_name_plural = "invoices"



