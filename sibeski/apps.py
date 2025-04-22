from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SibeskiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sibeski"
    verbose_name = _("Su ve Kanalizasyon İşleri")
