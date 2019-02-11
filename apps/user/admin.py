from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _

# from apps.user.forms import CustomUserChangeForm, CustomUserCreationForm
# from apps.user.forms import CustomUserChangeForm, CustomUserCreationForm
from apps.user.models import CustomUser


class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference the removed 'username' field
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('username', 'first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_student', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_student', 'is_staff')}
         ),
    )
    # form = CustomUserChangeForm
    # add_form = CustomUserCreationForm
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['app_name'] = 'user.customuser'
        extra_context['app'] = 'user'
        return super(CustomUserAdmin, self).changelist_view(request, extra_context=extra_context)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Site)
admin.site.unregister(Group)
