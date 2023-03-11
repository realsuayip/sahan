from django.contrib import admin

from sahan.clips.models import Clip


@admin.register(Clip)
class ClipAdmin(admin.ModelAdmin):
    search_fields = ("name", "ident", "keywords")
    list_display = ("name", "ident", "is_active", "created")
    list_editable = ("ident", "is_active")
    ordering = ("-created",)
    list_filter = ("is_active", "created", "modified")
