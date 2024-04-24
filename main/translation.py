from modeltranslation.translator import register, TranslationOptions
from .models import (SpecializationCategory, Doctor, Masseur, MedicalEquipment,
                     TrainingEquipment, Trainer, Reception, Diagnosis, Service,
                     EquipmentServiceHistory)

@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('name', 'about', "price")  # List the fields of Service to be translated

@register(SpecializationCategory)
class SpecializationCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)  # List the fields of SpecializationCategory to be translated

@register(Doctor)
class DoctorTranslationOptions(TranslationOptions):
    fields = ('bio',)  # Ensure this is a tuple with a trailing comma


@register(Masseur)
class MasseurTranslationOptions(TranslationOptions):
    fields = ('bio',)  # Ensure this is a tuple with a trailing comma

@register(MedicalEquipment)
class MedicalEquipmentTranslationOptions(TranslationOptions):
    fields = ('name', 'description')  # List the fields of MedicalEquipment to be translated

@register(TrainingEquipment)
class TrainingEquipmentTranslationOptions(TranslationOptions):
    fields = ('name', 'description')  # List the fields of TrainingEquipment to be translated

@register(Trainer)
class TrainerTranslationOptions(TranslationOptions):
    fields = ('bio',)  # Ensure this is a tuple with a trailing comma

@register(Diagnosis)
class DiagnosisTranslationOptions(TranslationOptions):
    fields = ('diagnosis_text', 'treatment_text')  # List the fields of Diagnosis to be translated


@register(EquipmentServiceHistory)
class EquipmentServiceHistoryTranslationOptions(TranslationOptions):
    fields = ('description',)  # List the fields of EquipmentServiceHistory to be translated
