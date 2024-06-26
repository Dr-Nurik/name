# Generated by Django 5.0 on 2024-04-08 21:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_alter_diagnosis_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='specializationcategory',
            options={'verbose_name': 'Специализация', 'verbose_name_plural': 'Специализаций'},
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='diagnosis_text_kz',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='diagnosis_text_ru',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='treatment_text_kz',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='treatment_text_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='bio_kz',
            field=models.TextField(default='', null=True, verbose_name='Информация о враче'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='bio_ru',
            field=models.TextField(default='', null=True, verbose_name='Информация о враче'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='doctors_name_kz',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to=settings.AUTH_USER_MODEL, verbose_name='Профиль пользователя'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='doctors_name_ru',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to=settings.AUTH_USER_MODEL, verbose_name='Профиль пользователя'),
        ),
        migrations.AddField(
            model_name='equipmentservicehistory',
            name='description_kz',
            field=models.TextField(null=True, verbose_name='Описание обслуживания'),
        ),
        migrations.AddField(
            model_name='equipmentservicehistory',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание обслуживания'),
        ),
        migrations.AddField(
            model_name='masseur',
            name='bio_kz',
            field=models.TextField(default='', null=True, verbose_name='Информация о враче'),
        ),
        migrations.AddField(
            model_name='masseur',
            name='bio_ru',
            field=models.TextField(default='', null=True, verbose_name='Информация о враче'),
        ),
        migrations.AddField(
            model_name='masseur',
            name='masseur_name_kz',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='masseur', to=settings.AUTH_USER_MODEL, verbose_name='Профиль пользователя'),
        ),
        migrations.AddField(
            model_name='masseur',
            name='masseur_name_ru',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='masseur', to=settings.AUTH_USER_MODEL, verbose_name='Профиль пользователя'),
        ),
        migrations.AddField(
            model_name='medicalequipment',
            name='description_kz',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='medicalequipment',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='medicalequipment',
            name='name_kz',
            field=models.CharField(max_length=255, null=True, verbose_name='Наименование оборудования'),
        ),
        migrations.AddField(
            model_name='medicalequipment',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Наименование оборудования'),
        ),
        migrations.AddField(
            model_name='reception',
            name='comed_kz',
            field=models.BooleanField(default=False, verbose_name='Пациент прибыл'),
        ),
        migrations.AddField(
            model_name='reception',
            name='comed_ru',
            field=models.BooleanField(default=False, verbose_name='Пациент прибыл'),
        ),
        migrations.AddField(
            model_name='reception',
            name='date_kz',
            field=models.DateField(blank=True, null=True, verbose_name='Дата приема'),
        ),
        migrations.AddField(
            model_name='reception',
            name='date_ru',
            field=models.DateField(blank=True, null=True, verbose_name='Дата приема'),
        ),
        migrations.AddField(
            model_name='reception',
            name='declined_kz',
            field=models.BooleanField(default=False, verbose_name='Пациент отказался'),
        ),
        migrations.AddField(
            model_name='reception',
            name='declined_ru',
            field=models.BooleanField(default=False, verbose_name='Пациент отказался'),
        ),
        migrations.AddField(
            model_name='reception',
            name='fullname_patient_kz',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ФИО пациента'),
        ),
        migrations.AddField(
            model_name='reception',
            name='fullname_patient_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ФИО пациента'),
        ),
        migrations.AddField(
            model_name='reception',
            name='is_confirmed_kz',
            field=models.BooleanField(default=False, verbose_name='Подтверждение записи'),
        ),
        migrations.AddField(
            model_name='reception',
            name='is_confirmed_ru',
            field=models.BooleanField(default=False, verbose_name='Подтверждение записи'),
        ),
        migrations.AddField(
            model_name='reception',
            name='no_show_kz',
            field=models.BooleanField(default=False, verbose_name='Пациент не пришел'),
        ),
        migrations.AddField(
            model_name='reception',
            name='no_show_ru',
            field=models.BooleanField(default=False, verbose_name='Пациент не пришел'),
        ),
        migrations.AddField(
            model_name='reception',
            name='patient_contact_kz',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Контакты пациента'),
        ),
        migrations.AddField(
            model_name='reception',
            name='patient_contact_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Контакты пациента'),
        ),
        migrations.AddField(
            model_name='reception',
            name='payment_confirmed_kz',
            field=models.BooleanField(default=False, verbose_name='Подтверждение оплаты'),
        ),
        migrations.AddField(
            model_name='reception',
            name='payment_confirmed_ru',
            field=models.BooleanField(default=False, verbose_name='Подтверждение оплаты'),
        ),
        migrations.AddField(
            model_name='reception',
            name='requires_massage_kz',
            field=models.BooleanField(default=False, verbose_name='Требуется массаж'),
        ),
        migrations.AddField(
            model_name='reception',
            name='requires_massage_ru',
            field=models.BooleanField(default=False, verbose_name='Требуется массаж'),
        ),
        migrations.AddField(
            model_name='reception',
            name='time_kz',
            field=models.CharField(max_length=5, null=True, verbose_name='Время приема'),
        ),
        migrations.AddField(
            model_name='reception',
            name='time_ru',
            field=models.CharField(max_length=5, null=True, verbose_name='Время приема'),
        ),
        migrations.AddField(
            model_name='service',
            name='about_kz',
            field=models.CharField(default='No description provided', max_length=500, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='service',
            name='about_ru',
            field=models.CharField(default='No description provided', max_length=500, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='service',
            name='name_kz',
            field=models.CharField(max_length=255, null=True, verbose_name='Наименование услуги'),
        ),
        migrations.AddField(
            model_name='service',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Наименование услуги'),
        ),
        migrations.AddField(
            model_name='specializationcategory',
            name='name_kz',
            field=models.CharField(max_length=100, null=True, verbose_name='Наименование категории'),
        ),
        migrations.AddField(
            model_name='specializationcategory',
            name='name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Наименование категории'),
        ),
        migrations.AddField(
            model_name='trainer',
            name='bio_kz',
            field=models.TextField(default='', null=True, verbose_name='Информация о инструктура'),
        ),
        migrations.AddField(
            model_name='trainer',
            name='bio_ru',
            field=models.TextField(default='', null=True, verbose_name='Информация о инструктура'),
        ),
        migrations.AddField(
            model_name='trainer',
            name='trainer_name_kz',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trainer', to=settings.AUTH_USER_MODEL, verbose_name='Профиль пользователя'),
        ),
        migrations.AddField(
            model_name='trainer',
            name='trainer_name_ru',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trainer', to=settings.AUTH_USER_MODEL, verbose_name='Профиль пользователя'),
        ),
        migrations.AddField(
            model_name='trainingequipment',
            name='description_kz',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='trainingequipment',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='trainingequipment',
            name='name_kz',
            field=models.CharField(max_length=255, null=True, verbose_name='Название тренажера'),
        ),
        migrations.AddField(
            model_name='trainingequipment',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Название тренажера'),
        ),
    ]
