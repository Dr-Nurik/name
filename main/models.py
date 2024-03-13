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
    name = models.CharField(max_length=100, verbose_name='Наименование категории')

    def __str__(self):
        return self.name

class Doctor(models.Model):
    doctors_name = models.OneToOneField(UserProfile, on_delete=models.CASCADE, verbose_name='Профиль пользователя', related_name='doctor')
    specialization_category = models.ForeignKey(SpecializationCategory, on_delete=models.CASCADE, verbose_name='Категория специальности', related_name='doctors')
    birth_date = models.DateField(verbose_name='Дата рождения врача', null=True)
    image = models.ImageField(verbose_name='Фотография врача', upload_to='doctor_images/', default="", null=True)
    bio = models.TextField(verbose_name='Информация о враче',default="", null=True)
    achievements = models.CharField(max_length=255, verbose_name='Достижения врача', default="", null=True)
    certificates = models.CharField(max_length=255, verbose_name='Сертификаты врача', default="", null=True)

    def __str__(self):
        return self.doctors_name.full_name

    @property
    def age(self):
        if self.birth_date is None:
            return None  # or some default value if birth_date is not set
        today = date.today()
        return today.year - self.birth_date.year - (
                (today.month, today.day) < (self.birth_date.month, self.birth_date.day))


class Masseur(models.Model):
    masseur_name = models.OneToOneField(UserProfile, on_delete=models.CASCADE, verbose_name='Профиль пользователя', related_name='masseur')
    specialization_category = models.ForeignKey(SpecializationCategory, on_delete=models.CASCADE,
                                                verbose_name='Категория специальности', related_name='masseurs')
    birth_date = models.DateField(verbose_name='Дата рождения врача', null=True)
    image = models.ImageField(verbose_name='Фотография врача', upload_to='doctor_images/', default="", null=True)
    bio = models.TextField(verbose_name='Информация о враче',default="", null=True)

    def __str__(self):
        return self.masseur_name.full_name
    @property
    def age(self):
        if self.birth_date is None:
            return None  # or some default value if birth_date is not set
        today = date.today()
        return today.year - self.birth_date.year - (
                (today.month, today.day) < (self.birth_date.month, self.birth_date.day))
    class Meta:
        verbose_name = "Массажист"
        verbose_name_plural = "Массажисты"


class TrainingEquipment(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название тренажера')
    description = models.TextField(verbose_name='Описание')
    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование услуги')
    about = models.CharField(max_length=500, verbose_name='Описание', default="No description provided")  # Default value for existing rows
    price = models.CharField(max_length=100, verbose_name='Цена', default='Уточняйте у администратора')
    def __str__(self):
        return f"{self.name} - {self.price} руб."


from django.utils import timezone  # Импортируйте необходимые модели

class Reception(models.Model):
    date = models.DateField(verbose_name='Дата приема')
    time = models.CharField(verbose_name='Время приема', max_length=5)
    patient_name = models.ForeignKey(UserProfile, verbose_name='Пациент', on_delete=models.CASCADE, null=True, blank=True)
    non_registered_patient_name = models.CharField(max_length=255, verbose_name='Имя незарегистрированного пациента', null=True, blank=True)
    non_registered_patient_contact = models.CharField(max_length=255, verbose_name='Контакт незарегистрированного пациента', null=True, blank=True)
    non_registered_patient_indevid_intevicat_nomer = models.IntegerField(
        verbose_name='ИИН ПАЦИЕНТА',
        validators=[MaxValueValidator(999999999999), MinValueValidator(000000000000)],
        null=True, blank=True
    )
    services = models.ManyToManyField(Service, verbose_name='Услуги', null=True, blank=True)
    doctor = models.ForeignKey(Doctor, verbose_name='Доктор', on_delete=models.CASCADE, blank=True, null=True)
    trainer = models.ForeignKey(TrainingEquipment, verbose_name='Тренажер', on_delete=models.CASCADE, null=True, blank=True)
    requires_massage = models.BooleanField(verbose_name='Требуется массаж', default=False)
    masseur = models.ForeignKey(Masseur, verbose_name='Массажист', on_delete=models.CASCADE, null=True, blank=True)
    comed = models.BooleanField(verbose_name='Пациент прибыл', default=False)
    declined = models.BooleanField(verbose_name='Пациент отказался', default=False)
    no_show = models.BooleanField(verbose_name='Пациент не пришел', default=False)
    is_confirmed = models.BooleanField(verbose_name='Подтверждение записи', default=False)
    payment_confirmed = models.BooleanField(verbose_name='Подтверждение оплаты', default=False)

    def __str__(self):
        patient_name = self.patient_name.full_name if self.patient_name else self.non_registered_patient_name
        doctor_name = self.doctor.doctors_name.full_name if self.doctor else "Нет врача"
        return f'Прием №{self.id} - {doctor_name} для {patient_name}'

    class Meta:
        verbose_name_plural = "Приемы"
        verbose_name = "Прием"


class PatientMedicalHistory(models.Model):
    patient = models.OneToOneField(UserProfile, on_delete=models.CASCADE, verbose_name='Пациент')
    medical_history = models.TextField(verbose_name='История болезни')
    # Additional fields as necessary

    def __str__(self):
        return f'История болезни {self.patient.full_name}'

class Diagnosis(models.Model):
    reception = models.ForeignKey(Reception, on_delete=models.CASCADE, verbose_name='Прием')
    diagnosis_text = models.TextField(verbose_name='Текст диагноза')
    treatment_text = models.TextField(verbose_name='Описание лечения', blank=True, null=True)
    date_prescribed = models.DateTimeField(default=timezone.now, verbose_name='Дата назначения')

    def __str__(self):
        return f'Диагноз для {self.reception.patient_name}'

STATUS_CHOICES = [
    ('рабочий', 'Рабочее'),
    ('на ремонте', 'На ремонте'),
    ('не работает', 'Выведено из эксплуатации'),
]

class MedicalEquipment(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование оборудования')
    inventory_number = models.CharField(max_length=255, unique=True, verbose_name='Инвентарный номер', null=True)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Рабочее', verbose_name='Статус')
    last_service_date = models.DateField(null=True, blank=True, verbose_name='Дата последнего обслуживания')
    image = models.ImageField(upload_to='equipment_images/', null=True, blank=True, verbose_name='Изображение')
    location = models.CharField(max_length=255, verbose_name='Местоположение' ,null=True)
    quantity = models.IntegerField(verbose_name='Количество')
    description = models.TextField(verbose_name='Описание')
    data_cupil = models.CharField(max_length=255, verbose_name='Дата приобретение', default='')
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

class EquipmentServiceHistory(models.Model):
    equipment = models.ForeignKey(MedicalEquipment, on_delete=models.CASCADE)
    service_date = models.DateField(verbose_name='Дата обслуживания')
    description = models.TextField(verbose_name='Описание обслуживания')



class PatientFeedback(models.Model):
    patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='Пациент')
    feedback = models.TextField(verbose_name='Отзыв')
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Отзыв от {self.patient.full_name}'
