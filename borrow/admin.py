from django.contrib import admin
from .models import LenderTypes, LenderPreferences, Lenders, LenderProfile

admin.site.register(LenderTypes)
admin.site.register(Lenders)
admin.site.register(LenderPreferences)
admin.site.register(LenderProfile)
