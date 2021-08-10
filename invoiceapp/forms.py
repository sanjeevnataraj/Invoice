from django import forms
from .models import Collections,Invoices


class CollectionForm(forms.ModelForm):
	class Meta:
		model = Collections
		fields = "__all__"

	def __init__(self, *args, **kwargs):
		super(CollectionForm, self).__init__(*args, **kwargs)
		self.fields['reference'] = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))


class AddBillForm(forms.ModelForm):
	class Meta:
		model = Invoices
		fields = "__all__"
