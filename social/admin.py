from django.contrib import admin
from .models import Link
# Register your models here.

class LinkAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


# Register your models here.
admin.site.register(Link,LinkAdmin)