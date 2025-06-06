# Generated by Django 5.2.1 on 2025-05-30 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkbahce', '0011_parkyol'),
    ]

    operations = [
        migrations.AddField(
            model_name='donatitip',
            name='deger',
            field=models.SlugField(blank=True, help_text='Donatı tipi için benzersiz bir değer giriniz.', null=True, unique=True, verbose_name='Değer'),
        ),
        migrations.AddField(
            model_name='elektrikbaglantitip',
            name='deger',
            field=models.SlugField(blank=True, help_text='Elektrik bağlantı tipi için benzersiz bir değer giriniz.', null=True, unique=True, verbose_name='Değer'),
        ),
        migrations.AddField(
            model_name='elektrikhattip',
            name='deger',
            field=models.SlugField(blank=True, help_text='Elektrik hat tipi için benzersiz bir değer giriniz.', null=True, unique=True, verbose_name='Değer'),
        ),
        migrations.AddField(
            model_name='elektrikkablotip',
            name='deger',
            field=models.SlugField(blank=True, help_text='Elektrik kablo tipi için benzersiz bir değer giriniz.', null=True, unique=True, verbose_name='Değer'),
        ),
        migrations.AddField(
            model_name='elektriknoktatip',
            name='deger',
            field=models.SlugField(blank=True, help_text='Elektrik noktası tipi için benzersiz bir değer giriniz.', null=True, unique=True, verbose_name='Değer'),
        ),
        migrations.AddField(
            model_name='habitattip',
            name='deger',
            field=models.SlugField(blank=True, help_text='Habitat tipi için benzersiz bir değer giriniz.', null=True, unique=True, verbose_name='Değer'),
        ),
        migrations.AddField(
            model_name='kanalborutip',
            name='deger',
            field=models.SlugField(blank=True, help_text='Kanalizasyon boru tipi için benzersiz bir değer giriniz.', null=True, unique=True, verbose_name='Değer'),
        ),
        migrations.AddField(
            model_name='kaplamatip',
            name='deger',
            field=models.SlugField(blank=True, help_text='Kaplama tipi için benzersiz bir değer giriniz.', null=True, unique=True, verbose_name='Değer'),
        ),
        migrations.AddField(
            model_name='oyungrupmodel',
            name='deger',
            field=models.SlugField(blank=True, help_text='Oyun grubu modeli için benzersiz bir değer giriniz.', null=True, unique=True, verbose_name='Değer'),
        ),
        migrations.AddField(
            model_name='oyungruptip',
            name='deger',
            field=models.SlugField(blank=True, help_text='Oyun grubu tipi için benzersiz bir değer giriniz.', null=True, unique=True, verbose_name='Değer'),
        ),
        migrations.AddField(
            model_name='parkbinakullanimtip',
            name='deger',
            field=models.SlugField(blank=True, help_text='Bina kullanım tipi için benzersiz bir değer giriniz.', null=True, unique=True, verbose_name='Değer'),
        ),
        migrations.AddField(
            model_name='parktip',
            name='deger',
            field=models.SlugField(blank=True, help_text='Park tipi için benzersiz bir değer giriniz.', null=True, unique=True, verbose_name='Değer'),
        ),
        migrations.AddField(
            model_name='sporalantip',
            name='deger',
            field=models.SlugField(blank=True, help_text='Spor alanı tipi için benzersiz bir değer giriniz.', null=True, unique=True, verbose_name='Değer'),
        ),
        migrations.AddField(
            model_name='sporaletigrup',
            name='deger',
            field=models.SlugField(blank=True, help_text='Spor aleti grubu için benzersiz bir değer giriniz.', null=True, unique=True, verbose_name='Değer'),
        ),
        migrations.AddField(
            model_name='sulamaborutip',
            name='deger',
            field=models.SlugField(blank=True, help_text='Boru tipi için benzersiz bir değer giriniz.', null=True, unique=True, verbose_name='Değer'),
        ),
        migrations.AddField(
            model_name='sulamakaynak',
            name='deger',
            field=models.SlugField(blank=True, help_text='Sulama kaynağı için benzersiz bir değer giriniz.', null=True, unique=True, verbose_name='Değer'),
        ),
        migrations.AddField(
            model_name='sulamanoktatip',
            name='deger',
            field=models.SlugField(blank=True, help_text='Sulama noktası tipi için benzersiz bir değer giriniz.', null=True, unique=True, verbose_name='Değer'),
        ),
        migrations.AddField(
            model_name='sulamatip',
            name='deger',
            field=models.SlugField(blank=True, help_text='Sulama tipi için benzersiz bir değer giriniz.', null=True, unique=True, verbose_name='Değer'),
        ),
    ]
