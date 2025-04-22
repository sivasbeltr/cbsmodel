from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UlasimConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ulasim"
    verbose_name = _("Ulaşım Hizmetleri")
