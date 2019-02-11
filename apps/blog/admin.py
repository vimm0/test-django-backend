from django.conf import settings
from django.contrib import admin

# Register your models here.
from django.contrib.admin import AdminSite
from django.contrib.auth import get_user_model

from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

from apps.customer.models import Client

User = get_user_model()


class MyAdminSite(AdminSite):
    def login(self, request, extra_context=None):
        new_user = False
        user = None
        if request.tenant.domain_url != settings.ORGANIZATION_ADMIN:  # <== here comes nepex group tenant
            # filter tenant users and accept only nepex group user
            # Only Tenant user are show so hard to find nepex group tenant user
            raise Http404()

        username = request.POST.get('username')  # Hack to find user before its last_login set to now.
        if username:
            user = User.objects.filter(username=username).first()
            if user:
                new_user = user.last_login is None

        r = super(MyAdminSite, self).login(request, extra_context)
        if new_user and request.user == user and isinstance(r, HttpResponseRedirect):
            # Successful logins will result in a redirect.
            return HttpResponseRedirect(reverse('admin:password_change'))
        return r


tenant_admin_site = MyAdminSite(name="tenant-admin")

"""
List and register all the Public ModelAdmin, which should be used for monitoring tenant.
Viewed from /nepex/tenant-admin/ 
"""


class ClientAdmin(admin.ModelAdmin):
    pass


tenant_admin_site.register(Client, ClientAdmin)
