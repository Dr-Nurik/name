# coding: utf-8
from django import forms
from .models import Doctor, Reception, Service
from django.contrib.admin import widgets

from django import forms
from .models import Reception

from django import forms
from .models import Reception, Doctor, Masseur, TrainingEquipment, Service

class ReceptionForm(forms.ModelForm):

    fullname_patient = forms.CharField(
        max_length=255,
        required=True,
        label='ФИО пациента'
    )
    patient_contact = forms.CharField(
        max_length=255,
        required=True,
        label='Контактная информация пациента'
    )
    doctor = forms.ModelChoiceField(
        queryset=Doctor.objects.all(),
        required=False,
        label='Врач',
        empty_label="Выберите врача"
    )
    masseur = forms.ModelChoiceField(
        queryset=Masseur.objects.all(),
        required=False,
        label='Массажист',
        empty_label="Выберите массажиста"
    )
    trainer = forms.ModelChoiceField(
        queryset=TrainingEquipment.objects.all(),
        required=False,
        label='Тренажер',
        empty_label="Выберите тренажер"
    )
    services = forms.ModelMultipleChoiceField(
        queryset=Service.objects.all(),
        required=True,
        label='Услуги',
        widget=forms.CheckboxSelectMultiple()
    )
    date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Reception
        fields = ['date', 'fullname_patient', 'patient_contact', 'doctor', 'masseur', 'trainer', 'services']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})

        }


    def __init__(self, *args, **kwargs):
        super(ReceptionForm, self).__init__(*args, **kwargs)
        # Если у вас есть поле services, измените здесь на 'services'
        self.fields['services'].required = False
        self.fields['doctor'].required = False


class ReceptionEditForm(forms.ModelForm):
    class Meta:
        model = Reception
        fields = [
            'date', 'time',
            'fullname_patient', 'patient_contact',
             'services',
            'doctor', 'trainer', "trainer_name", 'requires_massage', 'masseur',
            'comed', 'declined', 'no_show', 'is_confirmed', 'payment_confirmed'
        ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'services': forms.SelectMultiple(),
            'doctor': forms.Select(),
            'trainer': forms.Select(),
            'masseur': forms.Select(),
            "trainer_name": forms.Select()
        }

        def __init__(self, *args, **kwargs):
            super(ReceptionEditForm, self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'  # Добавление Bootstrap класса

from django import forms
from .models import  Service

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'about', 'price']
        labels = {
            'name': 'Наименование услуги',
            'about': 'Описание услуги',
            'price': 'Цена',
        }



from django import forms
from .models import Diagnosis
class DiagnosisForm(forms.ModelForm):
    class Meta:
        model = Diagnosis
        fields = ['diagnosis_text', 'treatment_text']

    def __init__(self, *args, **kwargs):
        super(DiagnosisForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class TimePeriodForm(forms.Form):
    TIME_PERIOD_CHOICES = [
        ('year', 'Год'),
        ('half_year', 'Полгода'),
        ('quarter', 'Квартал'),
        ('month', 'Месяц'),
        ('week', 'Неделя'),
        ('custom', 'Выбрать даты')
    ]
    period = forms.ChoiceField(choices=TIME_PERIOD_CHOICES)
    start_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)



from django import forms

class DateRangeForm(forms.Form):
    PERIOD_CHOICES = [
        ('year', 'Год'),
        ('half_year', 'Полгода'),
        ('quarter', 'Квартал'),
        ('month', 'Месяц'),
        ('week', 'Неделя'),
        ('custom', 'Выбрать даты'),
    ]

    period = forms.ChoiceField(choices=PERIOD_CHOICES, required=True, label='Период')
    start_date = forms.DateField(required=False, label='Начальная дата')
    end_date = forms.DateField(required=False, label='Конечная дата')

from django import forms
from .models import Diagnosis

class DiagnosisForm(forms.ModelForm):
    class Meta:
        model = Diagnosis
        fields = ['diagnosis_text', 'treatment_text', 'date_prescribed']
