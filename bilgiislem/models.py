import uuid

from django.conf import settings
from django.contrib.gis.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from ortak.models import Mahalle

# Fiber Optik Modelleri


class FiberKabloTip(models.Model):
    """
    Teknik Bilgiler:
    - Kablo Tipi: Fiber Optik Kablo
    - Kablo Çapı: 9/125, 50/125, 62.5/125, 100/140, 200/240, 400/480
    - Kablo Türü: Singlemode, Multimode
    """

    ad = models.CharField(_("Kablo Tipi"), max_length=100, unique=True)
    deger = models.SlugField(
        _("Değer"),
        max_length=50,
        unique=True,
        help_text=_("Sulama tipi için benzersiz bir değer giriniz."),
    )
    aciklama = models.TextField(_("Açıklama"), blank=True, null=True)

    def __str__(self):
        return self.ad

    class Meta:
        verbose_name = _("Fiber Kablo Tipi")
        verbose_name_plural = _("Fiber Kablo Tipleri")
        ordering = ["ad"]
        db_table = '"bilgiislem"."fiber_kablo_tipleri"'


class FiberGuzergahTip(models.Model):
    """
    Teknik Bilgiler:
    - Güzergah Tipi: Yeraltı, Yerüstü, Havai, Boru İçi
    - Güzergah Malzemesi: PVC, HDPE, Çelik, Alüminyum
    """

    ad = models.CharField(_("Güzergah Tipi"), max_length=50, unique=True)
    deger = models.SlugField(
        _("Değer"),
        max_length=50,
        unique=True,
        help_text=_("Güzergah tipi için benzersiz bir değer giriniz."),
    )
    aciklama = models.TextField(_("Açıklama"), blank=True, null=True)

    def __str__(self):
        return self.ad

    class Meta:
        verbose_name = _("Fiber Hat Güzergah Tipi")
        verbose_name_plural = _("Fiber Hat Güzergah Tipleri")
        ordering = ["ad"]
        db_table = '"bilgiislem"."fiber_guzergah_tipleri"'


class FiberHat(models.Model):
    """
    Model representing a fiber optic cable route.
    This model includes information about the fiber cable type,
    """

    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, blank=True, null=True
    )
    fiber_kablo_tipi = models.ForeignKey(
        FiberKabloTip,
        on_delete=models.SET_NULL,
        verbose_name=_("Kablo Tipi"),
        to_field="deger",
        null=True,
        blank=True,
    )
    fiber_hat_guzergah_tipi = models.ForeignKey(
        FiberGuzergahTip,
        on_delete=models.SET_NULL,
        verbose_name=_("Güzergah Tipi"),
        to_field="deger",
        null=True,
        blank=True,
    )
    boru_cap = models.FloatField(_("Koruyucu Boru Çapı (mm)"), blank=True, null=True)
    uzunluk = models.FloatField(_("Hat Uzunluğu (m)"), blank=True, null=True)
    baslangic_noktasi_aciklama = models.CharField(
        _("Başlangıç Noktası"), max_length=255, blank=True, null=True
    )
    bitis_noktasi_aciklama = models.CharField(
        _("Bitiş Noktası"), max_length=255, blank=True, null=True
    )
    geom = models.LineStringField(_("Geometri"), srid=settings.SRID)
    extra_data = models.JSONField(_("Ekstra Veri"), blank=True, null=True)
    created_at = models.DateTimeField(
        _("Oluşturulma Tarihi"),
        auto_now_add=True,
        editable=False,
        blank=True,
        null=True,
    )
    updated_at = models.DateTimeField(
        _("Güncellenme Tarihi"), auto_now=True, editable=False, blank=True, null=True
    )

    def __str__(self):
        return f"Fiber Hat - {self.pk}"

    class Meta:
        verbose_name = _("Fiber Optik Hat")
        verbose_name_plural = _("Fiber Optik Hatlar")
        ordering = ["-created_at"]
        db_table = '"bilgiislem"."fiber_hatlar"'


# Güvenlik Kamerası Modelleri


class KameraMarkaModel(models.Model):
    """
    Model representing a camera brand and model.
    This model includes information about the camera brand,
    model, and a description.
    """

    marka = models.CharField(_("Marka"), max_length=100)
    model = models.CharField(_("Model"), max_length=100)
    deger = models.SlugField(
        _("Değer"),
        max_length=100,
        unique=True,
        help_text=_("Kamera marka/modeli için benzersiz bir değer giriniz."),
    )
    aciklama = models.TextField(_("Açıklama"), blank=True, null=True)

    def __str__(self):
        return f"{self.marka} {self.model}"

    class Meta:
        verbose_name = _("Kamera Marka/Model")
        verbose_name_plural = _("Kamera Marka/Modelleri")
        unique_together = ("marka", "model")
        ordering = ["marka", "model"]
        db_table = '"bilgiislem"."kamera_marka_modelleri"'


class KameraTip(models.Model):
    """
    Model representing a camera type.
    This model includes information about the camera type,
    and a description.
    """

    ad = models.CharField(_("Kamera Tipi"), max_length=50, unique=True)
    deger = models.SlugField(
        _("Değer"),
        max_length=50,
        unique=True,
        help_text=_("Kamera tipi için benzersiz bir değer giriniz."),
    )
    aciklama = models.TextField(_("Açıklama"), blank=True, null=True)

    def __str__(self):
        return self.ad

    class Meta:
        verbose_name = _("Kamera Tipi")
        verbose_name_plural = _("Kamera Tipleri")
        ordering = ["ad"]
        db_table = '"bilgiislem"."kamera_tipleri"'


class KameraCozunurluk(models.Model):
    """
    Model representing a camera resolution.
    This model includes information about the camera resolution,
    and a description.
    """

    ad = models.CharField(_("Çözünürlük"), max_length=50, unique=True)
    deger = models.SlugField(
        _("Değer"),
        max_length=50,
        unique=True,
        help_text=_("Kamera çözünürlüğü için benzersiz bir değer giriniz."),
    )
    aciklama = models.TextField(_("Açıklama"), blank=True, null=True)

    def __str__(self):
        return self.ad

    class Meta:
        verbose_name = _("Kamera Çözünürlüğü")
        verbose_name_plural = _("Kamera Çözünürlükleri")
        ordering = ["ad"]
        db_table = '"bilgiislem"."kamera_cozunurlukleri"'


class GuvenlikKamerasi(models.Model):
    """
    Model representing a security camera.
    This model includes information about the camera's location,
    brand, model, type, resolution, and other technical details.
    """

    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, blank=True, null=True
    )
    ad = models.CharField(_("Kamera Adı/Tanımı"), max_length=150)
    mahalle = models.ForeignKey(
        Mahalle,
        on_delete=models.SET_NULL,
        verbose_name=_("Mahalle"),
        null=True,
        blank=True,
    )
    kamera_marka_model = models.ForeignKey(
        KameraMarkaModel,
        on_delete=models.SET_NULL,
        verbose_name=_("Marka/Model"),
        to_field="deger",
        null=True,
        blank=True,
    )
    kamera_tipi = models.ForeignKey(
        KameraTip,
        on_delete=models.SET_NULL,
        verbose_name=_("Kamera Tipi"),
        to_field="deger",
        null=True,
        blank=True,
    )
    kamera_cozunurluk = models.ForeignKey(
        KameraCozunurluk,
        on_delete=models.SET_NULL,
        verbose_name=_("Çözünürlük"),
        to_field="deger",
        null=True,
        blank=True,
    )
    seri_no = models.CharField(
        _("Seri Numarası"), max_length=100, blank=True, null=True
    )
    ip_adresi = models.GenericIPAddressField(_("IP Adresi"), blank=True, null=True)
    kurulum_tarihi = models.DateField(_("Kurulum Tarihi"), blank=True, null=True)
    gorus_acisi = models.IntegerField(_("Görüş Açısı (Derece)"), blank=True, null=True)
    gece_gorus = models.BooleanField(_("Gece Görüşü Var mı?"), default=False)
    kayit_cihazi_bilgisi = models.CharField(
        _("Kayıt Cihazı Bilgisi"), max_length=150, blank=True, null=True
    )
    aktif_durum = models.BooleanField(_("Aktif mi?"), default=True)
    geom = models.PointField(_("Konum"), srid=settings.SRID)
    extra_data = models.JSONField(_("Ekstra Veri"), blank=True, null=True)
    created_at = models.DateTimeField(
        _("Oluşturulma Tarihi"),
        auto_now_add=True,
        editable=False,
        blank=True,
        null=True,
    )
    updated_at = models.DateTimeField(
        _("Güncellenme Tarihi"), auto_now=True, editable=False, blank=True, null=True
    )

    def __str__(self):
        return self.ad

    class Meta:
        verbose_name = _("Güvenlik Kamerası")
        verbose_name_plural = _("Güvenlik Kameraları")
        ordering = ["mahalle", "ad"]
        db_table = '"bilgiislem"."guvenlik_kameralari"'


# Arıza ve Bakım Modelleri


class ArizaBakimTipChoices(models.TextChoices):
    ARIZA = "ariza", _("Arıza")
    BAKIM = "bakim", _("Periyodik Bakım")
    DEGISHIM = "degisim", _("Değişim/Yenileme")
    KURULUM = "kurulum", _("Yeni Kurulum")


class ArizaBakimDurumChoices(models.TextChoices):
    BILDIRILDI = "bildirildi", _("Bildirildi")
    PLANLANDI = "planlandi", _("Planlandı")
    DEVAM_EDIYOR = "devam_ediyor", _("Devam Ediyor")
    COZULDU = "cozuldu", _("Çözüldü/Tamamlandı")
    ERTELENDI = "ertelendi", _("Ertelendi")
    IPTAL = "iptal", _("İptal Edildi")


class FiberArizaBakim(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, blank=True, null=True
    )
    fiber_hat = models.ForeignKey(
        FiberHat,
        on_delete=models.CASCADE,
        related_name="ariza_bakim_kayitlari",
        verbose_name=_("Fiber Hat"),
    )
    kayit_tipi = models.CharField(
        _("Kayıt Tipi"),
        max_length=20,
        choices=ArizaBakimTipChoices.choices,
        default=ArizaBakimTipChoices.ARIZA,
    )
    durum = models.CharField(
        _("Durum"),
        max_length=20,
        choices=ArizaBakimDurumChoices.choices,
        default=ArizaBakimDurumChoices.BILDIRILDI,
    )
    bildirim_tarihi = models.DateTimeField(
        _("Bildirim/Planlama Tarihi"), default=timezone.now
    )
    baslama_tarihi = models.DateTimeField(_("Başlama Tarihi"), blank=True, null=True)
    bitis_tarihi = models.DateTimeField(
        _("Bitiş/Çözülme Tarihi"), blank=True, null=True
    )
    sorumlu_ekip = models.CharField(
        _("Sorumlu Ekip/Personel"), max_length=150, blank=True, null=True
    )
    aciklama = models.TextField(_("Arıza/Bakım Açıklaması"))
    cozum_aciklamasi = models.TextField(
        _("Çözüm/Yapılan İşlem Açıklaması"), blank=True, null=True
    )
    extra_data = models.JSONField(_("Ekstra Veri"), blank=True, null=True)
    created_at = models.DateTimeField(
        _("Oluşturulma Tarihi"),
        auto_now_add=True,
        editable=False,
        blank=True,
        null=True,
    )
    updated_at = models.DateTimeField(
        _("Güncellenme Tarihi"), auto_now=True, editable=False, blank=True, null=True
    )

    def __str__(self):
        return f"{self.fiber_hat} - {self.get_kayit_tipi_display()} - {self.bildirim_tarihi.strftime('%Y-%m-%d')}"

    class Meta:
        verbose_name = _("Fiber Hat Arıza/Bakım Kaydı")
        verbose_name_plural = _("Fiber Hat Arıza/Bakım Kayıtları")
        ordering = ["-bildirim_tarihi"]
        db_table = '"bilgiislem"."fiber_ariza_bakim"'


class KameraArizaBakim(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, blank=True, null=True
    )
    kamera = models.ForeignKey(
        GuvenlikKamerasi,
        on_delete=models.CASCADE,
        related_name="ariza_bakim_kayitlari",
        verbose_name=_("Güvenlik Kamerası"),
    )
    kayit_tipi = models.CharField(
        _("Kayıt Tipi"),
        max_length=20,
        choices=ArizaBakimTipChoices.choices,
        default=ArizaBakimTipChoices.ARIZA,
    )
    durum = models.CharField(
        _("Durum"),
        max_length=20,
        choices=ArizaBakimDurumChoices.choices,
        default=ArizaBakimDurumChoices.BILDIRILDI,
    )
    bildirim_tarihi = models.DateTimeField(
        _("Bildirim/Planlama Tarihi"), default=timezone.now
    )
    baslama_tarihi = models.DateTimeField(_("Başlama Tarihi"), blank=True, null=True)
    bitis_tarihi = models.DateTimeField(
        _("Bitiş/Çözülme Tarihi"), blank=True, null=True
    )
    sorumlu_ekip = models.CharField(
        _("Sorumlu Ekip/Personel"), max_length=150, blank=True, null=True
    )
    aciklama = models.TextField(_("Arıza/Bakım Açıklaması"))
    cozum_aciklamasi = models.TextField(
        _("Çözüm/Yapılan İşlem Açıklaması"), blank=True, null=True
    )
    extra_data = models.JSONField(_("Ekstra Veri"), blank=True, null=True)
    created_at = models.DateTimeField(
        _("Oluşturulma Tarihi"),
        auto_now_add=True,
        editable=False,
        blank=True,
        null=True,
    )
    updated_at = models.DateTimeField(
        _("Güncellenme Tarihi"), auto_now=True, editable=False, blank=True, null=True
    )

    def __str__(self):
        return f"{self.kamera} - {self.get_kayit_tipi_display()} - {self.bildirim_tarihi.strftime('%Y-%m-%d')}"

    class Meta:
        verbose_name = _("Kamera Arıza/Bakım Kaydı")
        verbose_name_plural = _("Kamera Arıza/Bakım Kayıtları")
        ordering = ["-bildirim_tarihi"]
        db_table = '"bilgiislem"."kamera_ariza_bakim"'
