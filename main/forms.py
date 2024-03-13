# coding: utf-8
from django import forms
from .models import Doctor, Reception, Service
from django.contrib.admin import widgets

from django import forms
from .models import Reception

class ReceptionForm(forms.ModelForm):
    non_registered_patient_name = forms.CharField(
        max_length=255,
        required=False,
        label='Имя незарегистрированного пациента'
    )
    non_registered_patient_contact = forms.CharField(
        max_length=255,
        required=False,
        label='Контактная информация'
    )
    service = forms.ModelMultipleChoiceField(
        queryset=Service.objects.all(),
        required=False,
        label='Услуги',
        widget=forms.CheckboxSelectMultiple()
    )
    doctor = forms.ModelChoiceField(
        queryset=Doctor.objects.all(),
        required=False,
        label='Врач',
        empty_label="Выберите врача"
    )

    class Meta:
        model = Reception
        fields = ['date', 'service', 'doctor',
                  'non_registered_patient_name', 'non_registered_patient_contact']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'doctor': forms.Select()
        }

    def __init__(self, *args, **kwargs):
        super(ReceptionForm, self).__init__(*args, **kwargs)
        # Если у вас есть поле services, измените здесь на 'services'
        self.fields['service'].required = False
        self.fields['doctor'].required = False


class ReceptionEditForm(forms.ModelForm):
    class Meta:
        model = Reception
        fields = [
            'date', 'time', 'patient_name',
            'non_registered_patient_name', 'non_registered_patient_contact',
            'non_registered_patient_indevid_intevicat_nomer', 'services',
            'doctor', 'trainer', 'requires_massage', 'masseur',
            'comed', 'declined', 'no_show', 'is_confirmed', 'payment_confirmed'
        ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'services': forms.SelectMultiple(),
            'doctor': forms.Select(),
            'trainer': forms.Select(),
            'masseur': forms.Select()
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
from .models import PatientFeedback

class PatientFeedbackForm(forms.ModelForm):
    class Meta:
        model = PatientFeedback
        fields = ['feedback']
        widgets = {
            'feedback': forms.Textarea(attrs={'placeholder': 'Сообщение', 'required': 'required', 'rows': 5}),
        }
