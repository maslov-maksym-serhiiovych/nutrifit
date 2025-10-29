from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    readonly_fields = ('date_joined', 'last_login')
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = UserAdmin.add_fieldsets

    def get_inline_instances(self, request, obj=None):
        if obj is None:
            return []
        else:
            return super().get_inline_instances(request, obj)


admin.site.register(CustomUser, CustomUserAdmin)
