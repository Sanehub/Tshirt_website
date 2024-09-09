from django.contrib import admin
from .models import TShirt


@admin.register(TShirt)
class TShirtAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)