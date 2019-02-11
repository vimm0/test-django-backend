from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import path
from django.views.generic import TemplateView

# from apps.blog.admin import tenant_admin_site
from apps.customer.forms import ClientForm


class HomePage(TemplateView):
    """
    Because our needs are so simple, all we have to do is
    assign one value; template_name. The home.html file will be created
    in the next lesson.
    """
    template_name = 'public/home.html'


class PricingPage(TemplateView):
    template_name = 'public/pricing.html'


class ThanksPage(TemplateView):
    template_name = 'public/thanks.html'


def client_registration_page(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ClientForm(request.POST)
        # check whether it's valid:

        if form.is_valid():
            # process the data in form.cleaned_data as required
            client = form.save(commit=False)
            # import ipdb
            # ipdb.set_trace()
            client.name = client.domain_url
            client.schema_name = client.domain_url
            client.domain_url = client.domain_url + '.nepexgroup.tk'
            client.save()  # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ClientForm()

    return render(request, 'public/client_form.html', {'form': form})


urlpatterns = [
    path('', HomePage.as_view()),  # website for customer form fill up, showcase pricing and demo
    path('pricing/', PricingPage.as_view(), name='pricing-model'),
    path('client-registration/', client_registration_page, name='client-registration'),
    path('thanks/', ThanksPage.as_view(), name='thanks'),

]
