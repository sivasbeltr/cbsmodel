from django.contrib.gis import admin
from django.utils.translation import gettext_lazy as _

from .models import (
    AboneEndeks,
    DonatiTip,
    ElektrikHat,
    ElektrikHatTip,
    ElektrikKabloTip,
    Habitat,
    HabitatTip,
    KanalBoruTip,
    KanalHat,
    KaplamaTip,
    OyunAlan,
    OyunGrupTip,
    Park,
    ParkAbone,
    ParkBina,
    ParkBinaKullanimTip,
    ParkDonati,
    ParkOyunGrup,
    ParkTip,
    SporAlan,
    SporAlanTip,
    SulamaBoruTip,
    SulamaHat,
    SulamaKaynak,
    SulamaNokta,
    SulamaNoktaTip,
    SulamaTip,
    YesilAlan,
)


# Simple Type Models
@admin.register(SulamaTip)
class SulamaTipAdmin(admin.ModelAdmin):
    list_display = ("ad", "aciklama")
    search_fields = ("ad",)


@admin.register(SulamaKaynak)
class SulamaKaynakAdmin(admin.ModelAdmin):
    list_display = ("ad", "aciklama")
    search_fields = ("ad",)


@admin.register(ParkTip)
class ParkTipAdmin(admin.ModelAdmin):
    list_display = ("ad", "aciklama")
    search_fields = ("ad",)


@admin.register(KaplamaTip)
class KaplamaTipAdmin(admin.ModelAdmin):
    list_display = ("ad", "aciklama")
    search_fields = ("ad",)


@admin.register(SporAlanTip)
class SporAlanTipAdmin(admin.ModelAdmin):
    list_display = ("ad", "aciklama")
    search_fields = ("ad",)


@admin.register(ParkBinaKullanimTip)
class ParkBinaKullanimTipAdmin(admin.ModelAdmin):
    list_display = ("ad", "aciklama")
    search_fields = ("ad",)


@admin.register(DonatiTip)
class DonatiTipAdmin(admin.ModelAdmin):
    list_display = ("ad", "aciklama")
    search_fields = ("ad",)


@admin.register(OyunGrupTip)
class OyunGrupTipAdmin(admin.ModelAdmin):
    list_display = ("ad", "aciklama")
    search_fields = ("ad",)


@admin.register(SulamaBoruTip)
class SulamaBoruTipAdmin(admin.ModelAdmin):
    list_display = ("ad", "aciklama")
    search_fields = ("ad",)


@admin.register(SulamaNoktaTip)
class SulamaNoktaTipAdmin(admin.ModelAdmin):
    list_display = ("ad", "aciklama")
    search_fields = ("ad",)


@admin.register(KanalBoruTip)
class KanalBoruTipAdmin(admin.ModelAdmin):
    list_display = ("ad", "aciklama")
    search_fields = ("ad",)


@admin.register(ElektrikKabloTip)
class ElektrikKabloTipAdmin(admin.ModelAdmin):
    list_display = ("ad", "aciklama")
    search_fields = ("ad",)


@admin.register(ElektrikHatTip)
class ElektrikHatTipAdmin(admin.ModelAdmin):
    list_display = ("ad", "aciklama")
    search_fields = ("ad",)


@admin.register(HabitatTip)
class HabitatTipAdmin(admin.ModelAdmin):
    list_display = ("ad", "aciklama")
    search_fields = ("ad",)


# Main Park Model
@admin.register(Park)
class ParkAdmin(admin.GISModelAdmin):
    list_display = ("ad", "mahalle", "park_tipi", "alan", "yapim_tarihi")
    search_fields = ("ad", "mahalle__ad", "mahalle__ilce__ad")
    list_filter = (
        "mahalle__ilce__il",
        "mahalle__ilce",
        "mahalle",
        "park_tipi",
        "sulama_tipi",
        "sulama_kaynagi",
    )
    readonly_fields = ("uuid", "created_at", "updated_at")
    gis_widget_kwargs = {
        "attrs": {
            "default_zoom": 14,
        },
    }

    fieldsets = (
        (_("Temel Bilgiler"), {"fields": ("ad", "mahalle", "ada", "park_tipi")}),
        (
            _("Yapım ve Karar Bilgileri"),
            {
                "fields": (
                    "yapim_tarihi",
                    "yapan_firma",
                    "ekap_no",
                    "meclis_tarih",
                    "meclis_no",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            _("Sulama Bilgileri"),
            {"fields": ("sulama_tipi", "sulama_kaynagi"), "classes": ("collapse",)},
        ),
        (_("Geometri ve Ölçümler"), {"fields": ("geom", "alan", "cevre")}),
        (
            _("Ekstra Veri ve Meta"),
            {"fields": ("extra_data", "osm_id"), "classes": ("collapse",)},
        ),
        (
            _("Tarihçe"),
            {"fields": ("uuid", "created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )


# Park Related Models
class AboneEndeksInline(admin.TabularInline):
    model = AboneEndeks
    extra = 1
    readonly_fields = ("created_at", "updated_at")
    fields = ("endeks_tarihi", "endeks_degeri", "created_at", "updated_at")


@admin.register(ParkAbone)
class ParkAboneAdmin(admin.GISModelAdmin):
    list_display = ("park", "abone_tipi", "abone_no", "abone_tarihi")
    search_fields = ("park__ad", "abone_no")
    list_filter = ("abone_tipi", "park__mahalle")
    readonly_fields = ("uuid", "created_at", "updated_at")
    inlines = [AboneEndeksInline]
    gis_widget_kwargs = {
        "attrs": {
            "default_zoom": 16,
        },
    }

    fieldsets = (
        (
            _("Temel Bilgiler"),
            {"fields": ("park", "abone_tipi", "abone_no", "abone_tarihi")},
        ),
        (_("Konum"), {"fields": ("geom",)}),
        (
            _("Ekstra Veri ve Meta"),
            {"fields": ("extra_data", "osm_id"), "classes": ("collapse",)},
        ),
        (
            _("Tarihçe"),
            {"fields": ("uuid", "created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )


@admin.register(YesilAlan)
class YesilAlanAdmin(admin.GISModelAdmin):
    list_display = ("park", "alan", "cevre")
    search_fields = ("park__ad",)
    list_filter = ("park__mahalle",)
    readonly_fields = ("uuid", "created_at", "updated_at")
    gis_widget_kwargs = {
        "attrs": {
            "default_zoom": 15,
        },
    }
    fieldsets = (
        (_("Temel Bilgiler"), {"fields": ("park",)}),
        (_("Geometri ve Ölçümler"), {"fields": ("geom", "alan", "cevre")}),
        (
            _("Ekstra Veri ve Meta"),
            {"fields": ("extra_data", "osm_id"), "classes": ("collapse",)},
        ),
        (
            _("Tarihçe"),
            {"fields": ("uuid", "created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )


@admin.register(SporAlan)
class SporAlanAdmin(admin.GISModelAdmin):
    list_display = ("park", "spor_alan_tipi", "spor_alan_kaplama_tipi", "alan")
    search_fields = ("park__ad", "spor_alan_tipi__ad")
    list_filter = ("park__mahalle", "spor_alan_tipi", "spor_alan_kaplama_tipi")
    readonly_fields = ("uuid", "created_at", "updated_at")
    gis_widget_kwargs = {
        "attrs": {
            "default_zoom": 15,
        },
    }
    fieldsets = (
        (
            _("Temel Bilgiler"),
            {"fields": ("park", "spor_alan_tipi", "spor_alan_kaplama_tipi")},
        ),
        (_("Geometri ve Ölçümler"), {"fields": ("geom", "alan", "cevre")}),
        (
            _("Ekstra Veri ve Meta"),
            {"fields": ("extra_data", "osm_id"), "classes": ("collapse",)},
        ),
        (
            _("Tarihçe"),
            {"fields": ("uuid", "created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )


@admin.register(OyunAlan)
class OyunAlanAdmin(admin.GISModelAdmin):
    list_display = ("park", "oyun_alan_kaplama_tipi", "alan")
    search_fields = ("park__ad",)
    list_filter = ("park__mahalle", "oyun_alan_kaplama_tipi")
    readonly_fields = ("uuid", "created_at", "updated_at")
    gis_widget_kwargs = {
        "attrs": {
            "default_zoom": 15,
        },
    }
    fieldsets = (
        (_("Temel Bilgiler"), {"fields": ("park", "oyun_alan_kaplama_tipi")}),
        (_("Geometri ve Ölçümler"), {"fields": ("geom", "alan", "cevre")}),
        (
            _("Ekstra Veri ve Meta"),
            {"fields": ("extra_data", "osm_id"), "classes": ("collapse",)},
        ),
        (
            _("Tarihçe"),
            {"fields": ("uuid", "created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )


@admin.register(ParkBina)
class ParkBinaAdmin(admin.GISModelAdmin):
    list_display = ("ad", "park", "bina_kullanim_tipi", "alan")
    search_fields = ("ad", "park__ad", "bina_kullanim_tipi__ad")
    list_filter = ("park__mahalle", "bina_kullanim_tipi")
    readonly_fields = ("uuid", "created_at", "updated_at")
    gis_widget_kwargs = {
        "attrs": {
            "default_zoom": 15,
        },
    }
    fieldsets = (
        (_("Temel Bilgiler"), {"fields": ("park", "ad", "bina_kullanim_tipi")}),
        (_("Geometri ve Ölçümler"), {"fields": ("geom", "alan", "cevre")}),
        (
            _("Ekstra Veri ve Meta"),
            {"fields": ("extra_data", "osm_id"), "classes": ("collapse",)},
        ),
        (
            _("Tarihçe"),
            {"fields": ("uuid", "created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )


@admin.register(ParkDonati)
class ParkDonatiAdmin(admin.GISModelAdmin):
    list_display = ("park", "donati_tipi")
    search_fields = ("park__ad", "donati_tipi__ad")
    list_filter = ("park__mahalle", "donati_tipi")
    readonly_fields = ("uuid", "created_at", "updated_at")
    gis_widget_kwargs = {
        "attrs": {
            "default_zoom": 16,
        },
    }
    fieldsets = (
        (_("Temel Bilgiler"), {"fields": ("park", "donati_tipi")}),
        (_("Konum"), {"fields": ("geom",)}),
        (
            _("Ekstra Veri ve Meta"),
            {"fields": ("extra_data", "osm_id"), "classes": ("collapse",)},
        ),
        (
            _("Tarihçe"),
            {"fields": ("uuid", "created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )


@admin.register(ParkOyunGrup)
class ParkOyunGrupAdmin(admin.GISModelAdmin):
    list_display = ("ad", "park", "oyun_grup_tipi", "sayi")
    search_fields = ("ad", "park__ad", "oyun_grup_tipi__ad")
    list_filter = ("park__mahalle", "oyun_grup_tipi")
    readonly_fields = ("uuid", "created_at", "updated_at")
    gis_widget_kwargs = {
        "attrs": {
            "default_zoom": 16,
        },
    }
    fieldsets = (
        (_("Temel Bilgiler"), {"fields": ("park", "ad", "oyun_grup_tipi", "sayi")}),
        (_("Konum"), {"fields": ("geom",)}),
        (
            _("Ekstra Veri ve Meta"),
            {"fields": ("extra_data", "osm_id"), "classes": ("collapse",)},
        ),
        (
            _("Tarihçe"),
            {"fields": ("uuid", "created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )


@admin.register(SulamaHat)
class SulamaHatAdmin(admin.GISModelAdmin):
    list_display = ("park", "sulama_boru_tipi", "boru_cap", "uzunluk")
    search_fields = ("park__ad", "sulama_boru_tipi__ad")
    list_filter = ("park__mahalle", "sulama_boru_tipi")
    readonly_fields = ("uuid", "created_at", "updated_at")
    gis_widget_kwargs = {
        "attrs": {
            "default_zoom": 15,
        },
    }
    fieldsets = (
        (_("Temel Bilgiler"), {"fields": ("park", "sulama_boru_tipi", "boru_cap")}),
        (_("Geometri ve Ölçümler"), {"fields": ("geom", "uzunluk")}),
        (
            _("Ekstra Veri ve Meta"),
            {"fields": ("extra_data", "osm_id"), "classes": ("collapse",)},
        ),
        (
            _("Tarihçe"),
            {"fields": ("uuid", "created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )


@admin.register(SulamaNokta)
class SulamaNoktaAdmin(admin.GISModelAdmin):
    list_display = ("park", "sulama_nokta_tipi")
    search_fields = ("park__ad", "sulama_nokta_tipi__ad")
    list_filter = ("park__mahalle", "sulama_nokta_tipi")
    readonly_fields = ("uuid", "created_at", "updated_at")
    gis_widget_kwargs = {
        "attrs": {
            "default_zoom": 16,
        },
    }
    fieldsets = (
        (_("Temel Bilgiler"), {"fields": ("park", "sulama_nokta_tipi")}),
        (_("Konum"), {"fields": ("geom",)}),
        (
            _("Ekstra Veri ve Meta"),
            {"fields": ("extra_data", "osm_id"), "classes": ("collapse",)},
        ),
        (
            _("Tarihçe"),
            {"fields": ("uuid", "created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )


@admin.register(KanalHat)
class KanalHatAdmin(admin.GISModelAdmin):
    list_display = ("park", "kanal_boru_tipi", "boru_cap", "uzunluk")
    search_fields = ("park__ad", "kanal_boru_tipi__ad")
    list_filter = ("park__mahalle", "kanal_boru_tipi")
    readonly_fields = ("uuid", "created_at", "updated_at")
    gis_widget_kwargs = {
        "attrs": {
            "default_zoom": 15,
        },
    }
    fieldsets = (
        (_("Temel Bilgiler"), {"fields": ("park", "kanal_boru_tipi", "boru_cap")}),
        (_("Geometri ve Ölçümler"), {"fields": ("geom", "uzunluk")}),
        (
            _("Ekstra Veri ve Meta"),
            {"fields": ("extra_data", "osm_id"), "classes": ("collapse",)},
        ),
        (
            _("Tarihçe"),
            {"fields": ("uuid", "created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )


@admin.register(ElektrikHat)
class ElektrikHatAdmin(admin.GISModelAdmin):
    list_display = (
        "park",
        "elektrik_kablo_tipi",
        "elektrik_hat_tipi",
        "gerilim",
        "uzunluk",
    )
    search_fields = ("park__ad", "elektrik_kablo_tipi__ad", "elektrik_hat_tipi__ad")
    list_filter = ("park__mahalle", "elektrik_kablo_tipi", "elektrik_hat_tipi")
    readonly_fields = ("uuid", "created_at", "updated_at")
    gis_widget_kwargs = {
        "attrs": {
            "default_zoom": 15,
        },
    }
    fieldsets = (
        (
            _("Temel Bilgiler"),
            {
                "fields": (
                    "park",
                    "elektrik_kablo_tipi",
                    "elektrik_hat_tipi",
                    "boru_cap",
                    "gerilim",
                )
            },
        ),
        (_("Geometri ve Ölçümler"), {"fields": ("geom", "uzunluk")}),
        (
            _("Ekstra Veri ve Meta"),
            {"fields": ("extra_data", "osm_id"), "classes": ("collapse",)},
        ),
        (
            _("Tarihçe"),
            {"fields": ("uuid", "created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )


@admin.register(Habitat)
class HabitatAdmin(admin.GISModelAdmin):
    list_display = ("ad", "park", "habitat_tipi", "dikim_tarihi", "firma")
    search_fields = ("ad", "park__ad", "habitat_tipi__ad", "firma")
    list_filter = ("park__mahalle", "habitat_tipi", "dikim_tarihi")
    readonly_fields = ("uuid", "created_at", "updated_at")
    gis_widget_kwargs = {
        "attrs": {
            "default_zoom": 16,
        },
    }
    fieldsets = (
        (_("Temel Bilgiler"), {"fields": ("park", "ad", "habitat_tipi")}),
        (_("Detay Bilgiler"), {"fields": ("dikim_tarihi", "firma")}),
        (_("Konum"), {"fields": ("geom",)}),
        (
            _("Ekstra Veri ve Meta"),
            {"fields": ("extra_data", "osm_id"), "classes": ("collapse",)},
        ),
        (
            _("Tarihçe"),
            {"fields": ("uuid", "created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )
