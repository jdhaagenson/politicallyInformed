from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Voter

# Register your models here.
admin.site.register(Voter, UserAdmin)