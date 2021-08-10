from django.shortcuts import render
from .models import Collections,Invoices
from django.db.models import F,Sum
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CollectionForm,AddBillForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def dashboard(request):
	context = {}
	data = Invoices.objects.all().values()

	for row in data:
		collection_data = Collections.objects.filter(reference=row['reference']).aggregate(collection_amount=Sum('collection_amount'))
		if collection_data and collection_data['collection_amount']:
			row['total_amount'] =  collection_data['collection_amount']
			row['balance_amount'] =  row['amount'] - collection_data['collection_amount']
			# row.update(**collection_data[0])
	page = request.GET.get('page', 1)

	paginator = Paginator(data, 20)
	try:
		invoice_data = paginator.page(page)
	except PageNotAnInteger:
		invoice_data = paginator.page(1)
	except EmptyPage:
		invoice_data = paginator.page(paginator.num_pages)
	context['data'] = invoice_data
	return render(request,'dashboard.html',context)

def add_collection(request,pk=None):
	context = {}
	reference = Invoices.objects.filter(id=pk).values('reference','amount')
	if request.method == "POST":
		form = CollectionForm(request.POST or None)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/dashboard")
	form = CollectionForm(initial={'reference':reference[0]['reference']})
	context['form']=form
	return render(request,'add_collection.html',context)	

def manage_bills(request):
	type = request.GET.get('filter_type',None)
	context = {}
	data = Invoices.objects.all().values()
	final_data = []
	if type == "pending":
		for row in data:
			collection_data = Collections.objects.filter(reference=row['reference']).aggregate(collection_amount=Sum('collection_amount'))
			if collection_data and collection_data['collection_amount']:
				row['total_amount'] =  collection_data['collection_amount']
				row['balance_amount'] =  row['amount'] - collection_data['collection_amount']
				if row['balance_amount'] > 0:
					final_data.append(row)
	elif type == "collected":
		for row in data:
			collection_data = Collections.objects.filter(reference=row['reference']).aggregate(collection_amount=Sum('collection_amount'))
			if collection_data and collection_data['collection_amount']:
				row['total_amount'] =  collection_data['collection_amount']
				row['balance_amount'] =  row['amount'] - collection_data['collection_amount']
				if row['balance_amount'] == 0 :
					final_data.append(row)

			# row.update(**collection_data[0])
	page = request.GET.get('page', 1)

	paginator = Paginator(final_data, 20)
	try:
		invoice_data = paginator.page(page)
	except PageNotAnInteger:
		invoice_data = paginator.page(1)
	except EmptyPage:
		invoice_data = paginator.page(paginator.num_pages)
	context['data'] = invoice_data
	context['type'] = type
	return render(request,'manage-invoices.html',context)


def add_bills(request):
	context = {}
	form = AddBillForm(request.POST or None)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect("/dashboard")
	context['form'] = form
	return render(request,'add_bills.html',context)

	