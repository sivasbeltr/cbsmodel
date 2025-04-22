from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TemizlikConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "temizlik"
    verbose_name = _("Temizlik İşleri")
