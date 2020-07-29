from django.contrib import admin
# Register your models here.

from django.contrib import admin
from testmodel.models import Test, Tag


# class ContactAdmin(admin.ModelAdmin):
#     fields = ('name')
#
#
# admin.site.register(Tag, ContactAdmin)
class TagInline(admin.TabularInline):
    model = Tag


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','degree', 'email') # list
    search_fields = ('name',)
    inlines = [TagInline]
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['Advance', {
            'classes': ('collapse',),  # CSS
            'fields': ('degree',),
        }]
    )


admin.site.register(Test, ContactAdmin)
# Register your models here.
# admin.site.register([Tag])
