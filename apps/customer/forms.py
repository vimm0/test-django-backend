from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from apps.customer.models import Client


class ClientForm(ModelForm):
    domain_url = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'client1'}))
    schema_name = forms.CharField(required=False)
    name = forms.CharField(required=False)

    class Meta:
        model = Client
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        from django.forms.widgets import HiddenInput
        # hide_condition = kwargs.pop('hide_condition', None)
        super(ClientForm, self).__init__(*args, **kwargs)
        # if hide_condition:
        self.fields['schema_name'].widget = HiddenInput()
        self.fields['name'].widget = HiddenInput()
        # or alternately:  del self.fields['fieldname']  to remove it from the form altogether.

    def clean(self):
        form_data = self.cleaned_data
        subdomain = self.cleaned_data['domain_url']
        subdomain_with_domain = subdomain + '.nepexgroup.tk'

        if Client.objects.filter(domain_url=subdomain_with_domain).exists():
            raise ValidationError("Client with this Domain url already exists.")
        # else:
        #     self.schema_name = subdomain
        #     self.name = subdomain
        return form_data
