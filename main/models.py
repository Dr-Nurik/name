from django.db import models
from users.models import UserProfile
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.core.exceptions import ValidationError
from .validators import validate_date, validate_time
from django.db import models
from datetime import date  # Добавьте этот импорт
from django.utils import timezone
import qrcode
from io import BytesIO
from django.core.files import File
from django.utils.translation import gettext_lazy as _

import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

def generate_qr_code(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    buffer = BytesIO()
    img.save(buffer)
    filename = f'{text}.png'
    file = File(buffer, filename)
    return file



class SpecializationCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Наименование категории'))

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = _("Специализация")
        verbose_name_plural = _("Специализаций")

class Doctor(models.Model):
    doctors_name = models.OneToOneField(UserProfile, on_delete=models.CASCADE, verbose_name=_('Профиль пользователя'), related_name='doctor')
    specialization_category = models.ForeignKey(SpecializationCategory, on_delete=models.CASCADE, verbose_name=_('Категория специальности'), related_name='doctors')
    birth_date = models.DateField(verbose_name=_('Дата рождения врача'), null=True)
    image = models.ImageField(verbose_name=_('Фотография врача'), upload_to='doctor_images/', default="", null=True)
    bio = models.TextField(verbose_name=_('Информация о враче'),default="", null=True)
    facebook_url = models.URLField(verbose_name='Facebook URL', max_length=200, blank=True, null=True)
    telegram_url = models.URLField(verbose_name='Telegram URL', max_length=200, blank=True, null=True)
    instagram_url = models.URLField(verbose_name='Instagram URL', max_length=200, blank=True, null=True)
    def __str__(self):
        return self.doctors_name.full_name
    @property
    def full_name(self):
        return f"{self.doctors_name.first_name} {self.doctors_name.last_name}"

    @property
    def age(self):
        if self.birth_date is None:
            return None  # or some default value if birth_date is not set
        today = date.today()
        return today.year - self.birth_date.year - (
                (today.month, today.day) < (self.birth_date.month, self.birth_date.day))

    class Meta:
        verbose_name = _("Врачи")
        verbose_name_plural = _("Врачи")

class Masseur(models.Model):
    masseur_name = models.OneToOneField(UserProfile, on_delete=models.CASCADE, verbose_name=_('Профиль пользователя'), related_name='masseur')
    specialization_category = models.ForeignKey(SpecializationCategory, on_delete=models.CASCADE,
                                                verbose_name=_('Категория специальности'), related_name='masseurs')
    birth_date = models.DateField(verbose_name=_('Дата рождения врача'), null=True)
    image = models.ImageField(verbose_name=_('Фотография врача'), upload_to='masseur_images/', default="", null=True)
    bio = models.TextField(verbose_name=_('Информация о враче'),default="", null=True)
    facebook_url = models.URLField(verbose_name='Facebook URL', max_length=200, blank=True, null=True)
    telegram_url = models.URLField(verbose_name='Telegram URL', max_length=200, blank=True, null=True)
    instagram_url = models.URLField(verbose_name='Instagram URL', max_length=200, blank=True, null=True)
    def __str__(self):
        return self.masseur_name.full_name
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    @property
    def age(self):
        if self.birth_date is None:
            return None  # or some default value if birth_date is not set
        today = date.today()
        return today.year - self.birth_date.year - (
                (today.month, today.day) < (self.birth_date.month, self.birth_date.day))
    class Meta:
        verbose_name = _("Массажист")
        verbose_name_plural = _("Массажисты")

class Trainer(models.Model):
    trainer_name = models.OneToOneField(UserProfile, on_delete=models.CASCADE, verbose_name=_('Профиль пользователя'),
                                        related_name='trainer')
    specialization_category = models.ForeignKey(SpecializationCategory, on_delete=models.CASCADE,
                                                verbose_name=_('Категория специальности'), related_name='trainers')
    birth_date = models.DateField(verbose_name=_('Дата рождения инструктура'), null=True)
    image = models.ImageField(verbose_name=_('Фотография инструктура'), upload_to='trainer_images/', default="", null=True)
    bio = models.TextField(verbose_name=_('Информация о инструктура'), default="", null=True)
    facebook_url = models.URLField(verbose_name='Facebook URL', max_length=200, blank=True, null=True)
    telegram_url = models.URLField(verbose_name='Telegram URL', max_length=200, blank=True, null=True)
    instagram_url = models.URLField(verbose_name='Instagram URL', max_length=200, blank=True, null=True)
    def __str__(self):
        return self.trainer_name.full_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self):
        if self.birth_date is None:
            return None  # or some default value if birth_date is not set
        today = date.today()
        return today.year - self.birth_date.year - (
                (today.month, today.day) < (self.birth_date.month, self.birth_date.day))

    class Meta:
        verbose_name = _("Инструктор")
        verbose_name_plural = "Инструкторы"

class TrainingEquipment(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Название тренажера'))
    description = models.TextField(verbose_name=_('Описание'))
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = _("Зал")
        verbose_name_plural = _("Зал")

class Service(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Наименование услуги'))
    image = models.ImageField(verbose_name=_('Фотография услуг'), upload_to='service_images/', default="", null=True)
    about = models.CharField(max_length=500, verbose_name=_('Описание'), default=_("No description provided"))  # Default value for existing rows
    price = models.CharField(max_length=100, verbose_name=_('Цена'), default=_('Уточняйте у администратора'))
    def __str__(self):
        return f"{self.name} - {self.price} тенге."

    class Meta:
        verbose_name = _("Услуга")
        verbose_name_plural = _("Услуги")

from django.utils import timezone  # Импортируйте необходимые модели

class Reception(models.Model):
    date = models.DateField(verbose_name=_('Дата приема'), null=True, blank=True)
    time = models.CharField(verbose_name=_('Время приема'), max_length=5)
    fullname_patient = models.CharField(max_length=255, verbose_name=_('ФИО пациента'), null=True, blank=True)
    patient_contact = models.CharField(max_length=255, verbose_name=_('Контакты пациента'), null=True, blank=True)
    services = models.ManyToManyField(Service, verbose_name=_('Услуги'), null=True, blank=True)
    doctor = models.ForeignKey(Doctor, verbose_name=_('Доктор'), on_delete=models.CASCADE, blank=True, null=True)
    trainer_name = models.ForeignKey(Trainer, verbose_name=_('Инструктор'), on_delete=models.CASCADE, blank=True, null=True)
    trainer = models.ForeignKey(TrainingEquipment, verbose_name=_('Тренажер'), on_delete=models.CASCADE, null=True, blank=True)
    requires_massage = models.BooleanField(verbose_name=_('Требуется массаж'), default=False)
    masseur = models.ForeignKey(Masseur, verbose_name=_('Массажист'), on_delete=models.CASCADE, null=True, blank=True)
    comed = models.BooleanField(verbose_name=_('Пациент прибыл'), default=False)
    declined = models.BooleanField(verbose_name=_('Пациент отказался'), default=False)
    no_show = models.BooleanField(verbose_name=_('Пациент не пришел'), default=False)
    is_confirmed = models.BooleanField(verbose_name=_('Подтверждение записи'), default=False)
    payment_confirmed = models.BooleanField(verbose_name=_('Подтверждение оплаты'), default=False)

    def __str__(self):
        fullname_patient = self.fullname_patient if self.fullname_patient else "Неизвестный пациент"
        doctor_name = self.doctor.doctors_name.full_name if self.doctor else "Нет врача"
        return f'Прием №{self.id} - {doctor_name} для {fullname_patient}'

    class Meta:
        verbose_name_plural = _("Приемы")
        verbose_name = _("Прием")



class Diagnosis(models.Model):
    reception = models.ForeignKey(Reception, on_delete=models.CASCADE, verbose_name=_('Прием'))
    diagnosis_text = models.TextField(verbose_name=_('Текст'))
    treatment_text = models.TextField(verbose_name=_('Описание'), blank=True, null=True)
    date_prescribed = models.DateTimeField(default=timezone.now, verbose_name=_('Дата назначения'))

    def __str__(self):
        return f'Примечание для {self.reception.fullname_patient}'
    class Meta:
        verbose_name = _("Примечание")
        verbose_name_plural = _("Примечаний")

STATUS_CHOICES = [
    ('рабочий', 'Рабочее'),
    ('на ремонте', 'На ремонте'),
    ('не работает', 'Выведено из эксплуатации'),
]

class MedicalEquipment(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Наименование оборудования'))
    inventory_number = models.CharField(max_length=255, unique=True, verbose_name=_('Инвентарный номер'), null=True)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=_('Рабочее'), verbose_name=_('Статус'))
    last_service_date = models.DateField(null=True, blank=True, verbose_name=_('Дата последнего обслуживания'))
    image = models.ImageField(upload_to='equipment_images/', null=True, blank=True, verbose_name=_('Изображение'))
    location = models.CharField(max_length=255, verbose_name=('Местоположение') ,null=True)
    quantity = models.IntegerField(verbose_name=_('Количество'))
    description = models.TextField(verbose_name=_('Описание'))
    data_cupil = models.CharField(max_length=255, verbose_name=_('Дата приобретение'), default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr_data = f"Наименования: {self.name}, Код инвентаризации: {self.inventory_number}, Статус: {self.status}"
        qr.add_data(qr_data)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        buffer = BytesIO()
        img.save(buffer)
        filename = f'qr_code_{self.inventory_number}.png'
        file = File(buffer, name=filename)
        self.qr_code.save(filename, file, save=False)

        super().save(*args, **kwargs)
    def __str__(self):
        return self.name + ": $" + str(self.price)

    class Meta:
        verbose_name = _("Инвентарь")
        verbose_name_plural = _("Инвентаризация")

class EquipmentServiceHistory(models.Model):
    equipment = models.ForeignKey(MedicalEquipment, on_delete=models.CASCADE)
    service_date = models.DateField(verbose_name=_('Дата обслуживания'))
    description = models.TextField(verbose_name=_('Описание обслуживания'))
    class Meta:
        verbose_name = _("Обслуживание")
        verbose_name_plural = _("Обслуживании")
