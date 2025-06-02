from django.conf import settings
from django.contrib.gis import admin
from django.utils.translation import gettext_lazy as _

from .models import (
    FiberArizaBakim,
    FiberGuzergahTip,
    FiberHat,
    FiberKabloTip,
    GuvenlikKamerasi,
    KameraArizaBakim,
    KameraCozunurluk,
    KameraMarkaModel,
    KameraTip,
)


# Fiber Optik Tip Modelleri
@admin.register(FiberKabloTip)
class FiberKabloTipAdmin(admin.ModelAdmin):
    list_display = ("ad", "aciklama")
    search_fields = ("ad",)
    prepopulated_fields = {"deger": ("ad",)}


@admin.register(FiberGuzergahTip)
class FiberGuzergahTipAdmin(admin.ModelAdmin):
    list_display = ("ad", "aciklama")
    search_fields = ("ad",)
    prepopulated_fields = {"deger": ("ad",)}


# Fiber Optik Ana Model
@admin.register(FiberHat)
class FiberHatAdmin(admin.GISModelAdmin):
    list_display = (
        "id",
        "fiber_kablo_tipi",
        "fiber_hat_guzergah_tipi",
        "uzunluk",
        "created_at",
    )
    search_fields = ("baslangic_noktasi_aciklama", "bitis_noktasi_aciklama")
    list_filter = ("fiber_kablo_tipi", "fiber_hat_guzergah_tipi")
    readonly_fields = (
        "uuid",
        "created_at",
        "updated_at",
        "uzunluk",
    )  # Uzunluk otomatik hesaplanabilir veya trigger ile
    gis_widget_kwargs = {
        "attrs": {
            "default_zoom": settings.DEFAULT_MAP_ZOOM,
            "default_lat": settings.DEFAULT_MAP_LATITUDE,
            "default_lon": settings.DEFAULT_MAP_LONGITUDE,
        },
    }
    fieldsets = (
        (
            _("Temel Bilgiler"),
            {"fields": ("fiber_kablo_tipi", "fiber_hat_guzergah_tipi", "boru_cap")},
        ),
        (
            _("Güzergah Bilgileri"),
            {
                "fields": (
                    "baslangic_noktasi_aciklama",
                    "bitis_noktasi_aciklama",
                    "geom",
                    "uzunluk",
                )
            },
        ),
        (_("Ekstra Veri ve Meta"), {"fields": ("extra_data",)}),
        (
            _("Tarihçe"),
            {"fields": ("uuid", "created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )


# Güvenlik Kamerası Tip Modelleri
@admin.register(KameraMarkaModel)
class KameraMarkaModelAdmin(admin.ModelAdmin):
    list_display = ("marka", "model", "aciklama")
    search_fields = ("marka", "model")
    prepopulated_fields = {"deger": ("marka", "model")}


@admin.register(KameraTip)
class KameraTipAdmin(admin.ModelAdmin):
    list_display = ("ad", "aciklama")
    search_fields = ("ad",)
    prepopulated_fields = {"deger": ("ad",)}


@admin.register(KameraCozunurluk)
class KameraCozunurlukAdmin(admin.ModelAdmin):
    list_display = ("ad", "aciklama")
    search_fields = ("ad",)
    prepopulated_fields = {"deger": ("ad",)}


# Güvenlik Kamerası Ana Model
@admin.register(GuvenlikKamerasi)
class GuvenlikKamerasiAdmin(admin.GISModelAdmin):
    list_display = (
        "ad",
        "mahalle",
        "kamera_marka_model",
        "kamera_tipi",
        "ip_adresi",
        "aktif_durum",
    )
    search_fields = ("ad", "mahalle__ad", "seri_no", "ip_adresi")
    list_filter = (
        "mahalle__ilce",
        "mahalle",
        "kamera_tipi",
        "kamera_marka_model",
        "aktif_durum",
        "gece_gorus",
    )
    readonly_fields = ("uuid", "created_at", "updated_at")
    gis_widget_kwargs = {
        "attrs": {
            "default_zoom": settings.DEFAULT_MAP_ZOOM,
            "default_lat": settings.DEFAULT_MAP_LATITUDE,
            "default_lon": settings.DEFAULT_MAP_LONGITUDE,
        },
    }
    fieldsets = (
        (_("Temel Bilgiler"), {"fields": ("ad", "mahalle", "aktif_durum")}),
        (
            _("Teknik Özellikler"),
            {
                "fields": (
                    "kamera_marka_model",
                    "kamera_tipi",
                    "kamera_cozunurluk",
                    "seri_no",
                    "ip_adresi",
                    "gorus_acisi",
                    "gece_gorus",
                )
            },
        ),
        (_("Kurulum ve Kayıt"), {"fields": ("kurulum_tarihi", "kayit_cihazi_bilgisi")}),
        (_("Konum"), {"fields": ("geom",)}),
        (_("Ekstra Veri ve Meta"), {"fields": ("extra_data",)}),
        (
            _("Tarihçe"),
            {"fields": ("uuid", "created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )


# Arıza ve Bakım Modelleri
@admin.register(FiberArizaBakim)
class FiberArizaBakimAdmin(admin.ModelAdmin):
    list_display = (
        "fiber_hat",
        "kayit_tipi",
        "durum",
        "bildirim_tarihi",
        "sorumlu_ekip",
    )
    search_fields = ("fiber_hat__id", "aciklama", "cozum_aciklamasi", "sorumlu_ekip")
    list_filter = ("kayit_tipi", "durum", "sorumlu_ekip", "bildirim_tarihi")
    readonly_fields = ("uuid", "created_at", "updated_at")
    raw_id_fields = ("fiber_hat",)  # ForeignKey için arama/seçim kolaylığı
    fieldsets = (
        (_("İlişkili Hat ve Kayıt Tipi"), {"fields": ("fiber_hat", "kayit_tipi")}),
        (
            _("Durum ve Zamanlama"),
            {"fields": ("durum", "bildirim_tarihi", "baslama_tarihi", "bitis_tarihi")},
        ),
        (
            _("Detaylar ve Çözüm"),
            {"fields": ("sorumlu_ekip", "aciklama", "cozum_aciklamasi")},
        ),
        (_("Ekstra Veri ve Meta"), {"fields": ("extra_data",)}),
        (
            _("Tarihçe"),
            {"fields": ("uuid", "created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )


@admin.register(KameraArizaBakim)
class KameraArizaBakimAdmin(admin.ModelAdmin):
    list_display = ("kamera", "kayit_tipi", "durum", "bildirim_tarihi", "sorumlu_ekip")
    search_fields = (
        "kamera__ad",
        "kamera__seri_no",
        "aciklama",
        "cozum_aciklamasi",
        "sorumlu_ekip",
    )
    list_filter = (
        "kayit_tipi",
        "durum",
        "sorumlu_ekip",
        "bildirim_tarihi",
        "kamera__mahalle",
    )
    readonly_fields = ("uuid", "created_at", "updated_at")
    raw_id_fields = ("kamera",)  # ForeignKey için arama/seçim kolaylığı
    fieldsets = (
        (_("İlişkili Kamera ve Kayıt Tipi"), {"fields": ("kamera", "kayit_tipi")}),
        (
            _("Durum ve Zamanlama"),
            {"fields": ("durum", "bildirim_tarihi", "baslama_tarihi", "bitis_tarihi")},
        ),
        (
            _("Detaylar ve Çözüm"),
            {"fields": ("sorumlu_ekip", "aciklama", "cozum_aciklamasi")},
        ),
        (_("Ekstra Veri ve Meta"), {"fields": ("extra_data",)}),
        (
            _("Tarihçe"),
            {"fields": ("uuid", "created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )
