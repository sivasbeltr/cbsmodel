# Generated by Django 5.2.1 on 2025-06-02 06:23

import django.contrib.gis.db.models.fields
import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ortak', '0003_alter_ada_uuid_alter_il_uuid_alter_ilce_uuid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FiberGuzergahTip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=50, unique=True, verbose_name='Güzergah Tipi')),
                ('deger', models.SlugField(help_text='Güzergah tipi için benzersiz bir değer giriniz.', unique=True, verbose_name='Değer')),
                ('aciklama', models.TextField(blank=True, null=True, verbose_name='Açıklama')),
            ],
            options={
                'verbose_name': 'Fiber Hat Güzergah Tipi',
                'verbose_name_plural': 'Fiber Hat Güzergah Tipleri',
                'db_table': '"bilgiislem"."fiber_guzergah_tipleri"',
                'ordering': ['ad'],
            },
        ),
        migrations.CreateModel(
            name='FiberKabloTip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=100, unique=True, verbose_name='Kablo Tipi')),
                ('deger', models.SlugField(help_text='Sulama tipi için benzersiz bir değer giriniz.', unique=True, verbose_name='Değer')),
                ('aciklama', models.TextField(blank=True, null=True, verbose_name='Açıklama')),
            ],
            options={
                'verbose_name': 'Fiber Kablo Tipi',
                'verbose_name_plural': 'Fiber Kablo Tipleri',
                'db_table': '"bilgiislem"."fiber_kablo_tipleri"',
                'ordering': ['ad'],
            },
        ),
        migrations.CreateModel(
            name='KameraCozunurluk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=50, unique=True, verbose_name='Çözünürlük')),
                ('deger', models.SlugField(help_text='Kamera çözünürlüğü için benzersiz bir değer giriniz.', unique=True, verbose_name='Değer')),
                ('aciklama', models.TextField(blank=True, null=True, verbose_name='Açıklama')),
            ],
            options={
                'verbose_name': 'Kamera Çözünürlüğü',
                'verbose_name_plural': 'Kamera Çözünürlükleri',
                'db_table': '"bilgiislem"."kamera_cozunurlukleri"',
                'ordering': ['ad'],
            },
        ),
        migrations.CreateModel(
            name='KameraTip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=50, unique=True, verbose_name='Kamera Tipi')),
                ('deger', models.SlugField(help_text='Kamera tipi için benzersiz bir değer giriniz.', unique=True, verbose_name='Değer')),
                ('aciklama', models.TextField(blank=True, null=True, verbose_name='Açıklama')),
            ],
            options={
                'verbose_name': 'Kamera Tipi',
                'verbose_name_plural': 'Kamera Tipleri',
                'db_table': '"bilgiislem"."kamera_tipleri"',
                'ordering': ['ad'],
            },
        ),
        migrations.CreateModel(
            name='FiberHat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True, unique=True)),
                ('boru_cap', models.FloatField(blank=True, null=True, verbose_name='Koruyucu Boru Çapı (mm)')),
                ('uzunluk', models.FloatField(blank=True, null=True, verbose_name='Hat Uzunluğu (m)')),
                ('baslangic_noktasi_aciklama', models.CharField(blank=True, max_length=255, null=True, verbose_name='Başlangıç Noktası')),
                ('bitis_noktasi_aciklama', models.CharField(blank=True, max_length=255, null=True, verbose_name='Bitiş Noktası')),
                ('geom', django.contrib.gis.db.models.fields.LineStringField(srid=5256, verbose_name='Geometri')),
                ('extra_data', models.JSONField(blank=True, null=True, verbose_name='Ekstra Veri')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Güncellenme Tarihi')),
                ('fiber_hat_guzergah_tipi', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bilgiislem.fiberguzergahtip', to_field='deger', verbose_name='Güzergah Tipi')),
                ('fiber_kablo_tipi', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bilgiislem.fiberkablotip', to_field='deger', verbose_name='Kablo Tipi')),
            ],
            options={
                'verbose_name': 'Fiber Optik Hat',
                'verbose_name_plural': 'Fiber Optik Hatlar',
                'db_table': '"bilgiislem"."fiber_hatlar"',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='FiberArizaBakim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True, unique=True)),
                ('kayit_tipi', models.CharField(choices=[('ariza', 'Arıza'), ('bakim', 'Periyodik Bakım'), ('degisim', 'Değişim/Yenileme'), ('kurulum', 'Yeni Kurulum')], default='ariza', max_length=20, verbose_name='Kayıt Tipi')),
                ('durum', models.CharField(choices=[('bildirildi', 'Bildirildi'), ('planlandi', 'Planlandı'), ('devam_ediyor', 'Devam Ediyor'), ('cozuldu', 'Çözüldü/Tamamlandı'), ('ertelendi', 'Ertelendi'), ('iptal', 'İptal Edildi')], default='bildirildi', max_length=20, verbose_name='Durum')),
                ('bildirim_tarihi', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Bildirim/Planlama Tarihi')),
                ('baslama_tarihi', models.DateTimeField(blank=True, null=True, verbose_name='Başlama Tarihi')),
                ('bitis_tarihi', models.DateTimeField(blank=True, null=True, verbose_name='Bitiş/Çözülme Tarihi')),
                ('sorumlu_ekip', models.CharField(blank=True, max_length=150, null=True, verbose_name='Sorumlu Ekip/Personel')),
                ('aciklama', models.TextField(verbose_name='Arıza/Bakım Açıklaması')),
                ('cozum_aciklamasi', models.TextField(blank=True, null=True, verbose_name='Çözüm/Yapılan İşlem Açıklaması')),
                ('extra_data', models.JSONField(blank=True, null=True, verbose_name='Ekstra Veri')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Güncellenme Tarihi')),
                ('fiber_hat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ariza_bakim_kayitlari', to='bilgiislem.fiberhat', verbose_name='Fiber Hat')),
            ],
            options={
                'verbose_name': 'Fiber Hat Arıza/Bakım Kaydı',
                'verbose_name_plural': 'Fiber Hat Arıza/Bakım Kayıtları',
                'db_table': '"bilgiislem"."fiber_ariza_bakim"',
                'ordering': ['-bildirim_tarihi'],
            },
        ),
        migrations.CreateModel(
            name='GuvenlikKamerasi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True, unique=True)),
                ('ad', models.CharField(max_length=150, verbose_name='Kamera Adı/Tanımı')),
                ('seri_no', models.CharField(blank=True, max_length=100, null=True, verbose_name='Seri Numarası')),
                ('ip_adresi', models.GenericIPAddressField(blank=True, null=True, verbose_name='IP Adresi')),
                ('kurulum_tarihi', models.DateField(blank=True, null=True, verbose_name='Kurulum Tarihi')),
                ('gorus_acisi', models.IntegerField(blank=True, null=True, verbose_name='Görüş Açısı (Derece)')),
                ('gece_gorus', models.BooleanField(default=False, verbose_name='Gece Görüşü Var mı?')),
                ('kayit_cihazi_bilgisi', models.CharField(blank=True, max_length=150, null=True, verbose_name='Kayıt Cihazı Bilgisi')),
                ('aktif_durum', models.BooleanField(default=True, verbose_name='Aktif mi?')),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=5256, verbose_name='Konum')),
                ('extra_data', models.JSONField(blank=True, null=True, verbose_name='Ekstra Veri')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Güncellenme Tarihi')),
                ('mahalle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ortak.mahalle', verbose_name='Mahalle')),
                ('kamera_cozunurluk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bilgiislem.kameracozunurluk', to_field='deger', verbose_name='Çözünürlük')),
            ],
            options={
                'verbose_name': 'Güvenlik Kamerası',
                'verbose_name_plural': 'Güvenlik Kameraları',
                'db_table': '"bilgiislem"."guvenlik_kameralari"',
                'ordering': ['mahalle', 'ad'],
            },
        ),
        migrations.CreateModel(
            name='KameraArizaBakim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True, unique=True)),
                ('kayit_tipi', models.CharField(choices=[('ariza', 'Arıza'), ('bakim', 'Periyodik Bakım'), ('degisim', 'Değişim/Yenileme'), ('kurulum', 'Yeni Kurulum')], default='ariza', max_length=20, verbose_name='Kayıt Tipi')),
                ('durum', models.CharField(choices=[('bildirildi', 'Bildirildi'), ('planlandi', 'Planlandı'), ('devam_ediyor', 'Devam Ediyor'), ('cozuldu', 'Çözüldü/Tamamlandı'), ('ertelendi', 'Ertelendi'), ('iptal', 'İptal Edildi')], default='bildirildi', max_length=20, verbose_name='Durum')),
                ('bildirim_tarihi', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Bildirim/Planlama Tarihi')),
                ('baslama_tarihi', models.DateTimeField(blank=True, null=True, verbose_name='Başlama Tarihi')),
                ('bitis_tarihi', models.DateTimeField(blank=True, null=True, verbose_name='Bitiş/Çözülme Tarihi')),
                ('sorumlu_ekip', models.CharField(blank=True, max_length=150, null=True, verbose_name='Sorumlu Ekip/Personel')),
                ('aciklama', models.TextField(verbose_name='Arıza/Bakım Açıklaması')),
                ('cozum_aciklamasi', models.TextField(blank=True, null=True, verbose_name='Çözüm/Yapılan İşlem Açıklaması')),
                ('extra_data', models.JSONField(blank=True, null=True, verbose_name='Ekstra Veri')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Güncellenme Tarihi')),
                ('kamera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ariza_bakim_kayitlari', to='bilgiislem.guvenlikkamerasi', verbose_name='Güvenlik Kamerası')),
            ],
            options={
                'verbose_name': 'Kamera Arıza/Bakım Kaydı',
                'verbose_name_plural': 'Kamera Arıza/Bakım Kayıtları',
                'db_table': '"bilgiislem"."kamera_ariza_bakim"',
                'ordering': ['-bildirim_tarihi'],
            },
        ),
        migrations.CreateModel(
            name='KameraMarkaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marka', models.CharField(max_length=100, verbose_name='Marka')),
                ('model', models.CharField(max_length=100, verbose_name='Model')),
                ('deger', models.SlugField(help_text='Kamera marka/modeli için benzersiz bir değer giriniz.', max_length=100, unique=True, verbose_name='Değer')),
                ('aciklama', models.TextField(blank=True, null=True, verbose_name='Açıklama')),
            ],
            options={
                'verbose_name': 'Kamera Marka/Model',
                'verbose_name_plural': 'Kamera Marka/Modelleri',
                'db_table': '"bilgiislem"."kamera_marka_modelleri"',
                'ordering': ['marka', 'model'],
                'unique_together': {('marka', 'model')},
            },
        ),
        migrations.AddField(
            model_name='guvenlikkamerasi',
            name='kamera_marka_model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bilgiislem.kameramarkamodel', to_field='deger', verbose_name='Marka/Model'),
        ),
        migrations.AddField(
            model_name='guvenlikkamerasi',
            name='kamera_tipi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bilgiislem.kameratip', to_field='deger', verbose_name='Kamera Tipi'),
        ),
    ]
