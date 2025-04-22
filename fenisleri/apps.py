from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FenisleriConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "fenisleri"
    verbose_name = _("Fen İşleri")
