from phones.models import Phone
from django.contrib import admin

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    pass