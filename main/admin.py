from django.contrib import admin
from .models import SpecializationCategory,\
    Doctor, Reception, \
     MedicalEquipment,\
     Service, Diagnosis, \
    Masseur, TrainingEquipment, \
    Trainer
from django.contrib.admin import TabularInline, ModelAdmin
from django.forms import ModelForm
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.forms import ModelForm, TimeInput
from modeltranslation.admin import TranslationAdmin
def duplicate_service(modeladmin, request, queryset):
    for object in queryset:
        object.id = None  # Удаление идентификатора объекта
        object.save()  # Создание новой копии объекта

duplicate_service.short_description = "Дублировать выбранные услуги"

@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    list_display = ['name', 'about', 'price']  # Предполагается, что у вас есть эти поля
    list_filter = ['price']  # Пример фильтра, настройте в соответствии с вашими полями
    search_fields = ['name', 'about']
    actions = [duplicate_service]

@admin.register(Masseur)
class MasseurAdmin(TranslationAdmin):
    list_display = ('masseur_name', 'age', 'specialization_category')
    list_filter = ('specialization_category',)
    search_fields = ('masseur_name',)

    @admin.display(description='Возраст')
    def age(self, obj):
        return obj.age

@admin.register(TrainingEquipment)
class TrainingEquipmentAdmin(TranslationAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(SpecializationCategory)
class SpecializationCategoryAdmin(TranslationAdmin):
    list_display = ('name',)

@admin.register(Doctor)
class DoctorAdmin(TranslationAdmin):
    list_display = ('doctors_name', 'specialization_category')

@admin.register(Trainer)
class TrainerAdmin(TranslationAdmin):
    list_display = ('trainer_name', 'specialization_category')

class ReceptionForm(ModelForm):
    class Meta:
        model = Reception
        fields = '__all__'
        widgets = {
            'time': TimeInput(format='%H:%M'),  # Установка формата времени
        }


# Admin for Reception
class ReceptionAdmin(admin.ModelAdmin):

    list_display = ['fullname_patient', 'date', 'time',"is_confirmed",  'patient_contact', 'doctor', 'comed', 'declined', 'no_show']
    list_editable = ["is_confirmed", 'comed', 'declined', 'no_show' ]
    list_filter = ['date', 'doctor']  # Добавление фильтров
    search_fields = ['fullname_patient', 'patient_contact']


@admin.register(Diagnosis)
class DiagnosisAdmin(TranslationAdmin):
    list_display = ['reception', 'date_prescribed', 'diagnosis_text']
    list_filter = ['date_prescribed']  # Фильтр по дате назначения
    search_fields = ['reception__fullname_patient', 'reception__patient_contact']

# Register Reception with its ModelAdmin
@admin.register(MedicalEquipment)
class MedicalEquipmentAdmin(TranslationAdmin):
    list_display = ['name', 'inventory_number', 'status', 'last_service_date', 'location', 'price']
    list_filter = ['status', 'location', 'last_service_date']
    search_fields = ['name', 'inventory_number', 'description']

admin.site.register(Reception, ReceptionAdmin)


admin.site.site_header = "Здоровый след - Панель управления"
admin.site.site_title = "Администрирование Здорового Следа"
admin.site.index_title = "Добро пожаловать в административную панель"
