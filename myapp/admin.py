from django.contrib import admin
from .models import Contact, Nine, Eight, Seven


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone']


@admin.register(Nine)
class NineAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone']


@admin.register(Eight)
class EightAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone']


@admin.register(Seven)
class SevenAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone']
