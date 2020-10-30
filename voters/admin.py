from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Voter

UserAdmin.fieldsets += ('Custom fields set', {'fields': ('party', 'gender')}),

# Register your models here.
admin.site.register(Voter, UserAdmin)