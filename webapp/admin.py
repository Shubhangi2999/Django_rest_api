from django.contrib import admin
from .models import Partner
# Register your models here.

class PartnerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Partner,PartnerAdmin)