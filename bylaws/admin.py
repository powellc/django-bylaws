from django.contrib import admin
from bylaws.models import *

class BylawsAdmin(admin.ModelAdmin):
    search_fields = ('content','title',)

    fieldsets = (
        (None, {'fields': ('title', 'slug', 'content', 'status', 'sites',)}),
        ('Advaneced', {
            'fields': ('markup', 'rendered_content',),
            'classes': ('collapse',)
        }),
    )

admin.site.register(Bylaws, BylawsAdmin)
admin.site.register(UserSignature)
