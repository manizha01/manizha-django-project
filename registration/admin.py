from django.contrib import admin

# Register your models here.

from .models import client, dress

@admin.register(client)
class clientAdmin(admin.ModelAdmin):
    list_display = ['first', 'last', 'phone', 'city','country']
    


@admin.register(dress)
class dressAdmin(admin.ModelAdmin):
    pass
    


