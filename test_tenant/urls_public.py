from django.urls import path
from django.views.generic import TemplateView


class HomePage(TemplateView):
    """
    Because our needs are so simple, all we have to do is
    assign one value; template_name. The home.html file will be created
    in the next lesson.
    """
    template_name = 'public/home.html'


class PricingPage(TemplateView):
    """
    Because our needs are so simple, all we have to do is
    assign one value; template_name. The home.html file will be created
    in the next lesson.
    """
    template_name = 'public/pricing.html'


urlpatterns = [
    path('', HomePage.as_view()),  # website for customer form fill up, showcase pricing and demo
    path('pricing/', PricingPage.as_view(), name='pricing-model'),
]
