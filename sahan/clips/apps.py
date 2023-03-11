from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ClipsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sahan.clips"
    verbose_name = _("Clips")
