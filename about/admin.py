from django.contrib import admin
from .models import Category, About

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


admin.site.register(Category, CategoryAdmin)

class AboutAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('title','author','published')
    ordering=('author','published','title')
    search_fields=('title',)
    date_hierarchy='published'
    list_filter=('author',)

admin.site.register(About, AboutAdmin)