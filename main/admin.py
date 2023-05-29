from django.contrib import admin
from . import models


# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ('name',)


admin.site.register(models.Client, ClientAdmin)


class SiteAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("site_name",)}
    list_display = ('site_name', 'client', 'address', 'note',)
    list_editable = ('address', 'note', 'client')
    search_fields = ('site_name', 'address', 'note',)
    list_filter = ('client',)


admin.site.register(models.Site, SiteAdmin)


class LineItemInline(admin.TabularInline):
    model = models.LineItem
    extra = 1


class WorkOrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_id', 'slug', 'created_by')
    list_display = ('order_id', 'client', 'site', 'title', 'webhook_type', 'status', 'created_at',)
    list_filter = ('status', 'client', 'site', 'created_at',)
    search_fields = ('title', 'scope',)
    inlines = [LineItemInline, ]
    list_editable = ('title', 'slug', 'site', 'client', 'scope', 'status',)

    def get_readonly_fields(self, request, obj=None):
        fields = ['order_id', 'slug', 'created_by']
        if obj:
            fields.append('id')
        return fields

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)


admin.site.register(models.WorkOrder, WorkOrderAdmin)


class WebhookAdmin(admin.ModelAdmin):
    list_filter = ('webhook_type',)
    list_display = ('pk', 'title', 'webhook_type', 'url',)


admin.site.register(models.WebHook, WebhookAdmin)


class PartAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


admin.site.register(models.Part, PartAdmin)


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


admin.site.register(models.Manufacturer, ManufacturerAdmin)
