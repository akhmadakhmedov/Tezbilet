from django.contrib import admin
from .models import Blog, Comment

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    list_display_links = ['title']
    search_fields = ['title', 'content']
    list_filter = ['title', 'created_date']

    class Meta:
        model = Blog

admin.site.register(Comment)

