from django.contrib import admin
from .models import Post, UserConnect
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

admin.site.register(Post)
class StripeConnect(admin.StackedInline):
    model = UserConnect
    can_delete = False
    verbose_name_plural = 'you stripe account'


class UserAdmin(BaseUserAdmin):
    inlines = (StripeConnect, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)