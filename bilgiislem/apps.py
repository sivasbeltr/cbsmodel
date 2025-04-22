from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BilgiislemConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "bilgiislem"
    verbose_name = _("Bilgi İşlem")
