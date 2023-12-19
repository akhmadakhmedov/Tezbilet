from django.contrib import admin
from .models import University


@admin.register(University)

class UniversityAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'continent']
    list_display_links = ['name', 'continent', 'country']
    search_fields = ['name', 'continent', 'country', 'body']
    list_filter = ['continent', 'country']
    class Meta:
        model = University
