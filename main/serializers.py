from rest_framework import serializers
from .models import Reception, Doctor, Service, Masseur, TrainingEquipment

class ReceptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reception
        fields = ['date', 'patient_name',
                  'non_registered_patient_name',
                  'non_registered_patient_contact',
                  'doctor', 'services', 'masseur', 'training_equipment']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name']


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'doctors_name', 'specialization_category']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['doctors_name'] = instance.doctors_name.full_name
        representation['specialization_category'] = instance.specialization_category.name
        # Вы можете добавить другие поля или настроить их представление по вашему усмотрению
        return representation

class MasseurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Masseur
        fields = ['id', 'masseur_name']

class TrainingEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingEquipment
        fields = ['id', 'name',]