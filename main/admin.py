from django.contrib import admin
from .models import SpecializationCategory,\
    Doctor, Reception, PatientFeedback,\
    PatientMedicalHistory, MedicalEquipment,\
    PatientFeedback, Service, Diagnosis, \
    Masseur, TrainingEquipment
from django.contrib.admin import TabularInline, ModelAdmin
from django.forms import ModelForm
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.forms import ModelForm, TimeInput




@admin.register(Masseur)
class MasseurAdmin(admin.ModelAdmin):
    list_display = ('masseur_name', 'age', 'specialization_category')
    list_filter = ('specialization_category',)
    search_fields = ('masseur_name',)

    @admin.display(description='Возраст')
    def age(self, obj):
        return obj.age

@admin.register(TrainingEquipment)
class TrainingEquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(SpecializationCategory)
class SpecializationCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('doctors_name', 'specialization_category')


class ReceptionForm(ModelForm):
    class Meta:
        model = Reception
        fields = '__all__'
        widgets = {
            'time': TimeInput(format='%H:%M'),  # Установка формата времени
        }


# Admin for Reception
class ReceptionAdmin(admin.ModelAdmin):

    list_display = ['date', 'time', 'patient_name', 'non_registered_patient_name', 'doctor', 'comed', 'declined', 'no_show']
    list_editable = ['comed', 'declined', 'no_show']


# Register Reception with its ModelAdmin
admin.site.register(Reception, ReceptionAdmin)
admin.site.register(PatientMedicalHistory)

admin.site.register(MedicalEquipment)
admin.site.register(PatientFeedback)
admin.site.register(Service)


admin.site.register(Diagnosis)



