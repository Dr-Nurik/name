from rest_framework import serializers
from .models import Reception, Doctor, Service, Masseur, TrainingEquipment
from django.conf import settings

class ReceptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reception
        fields = ['date',
                  'fullname_patient',
                  'patient_contact',
                  'doctor', 'services', 'masseur', 'trainer']

    def create(self, validated_data):
        # Обработка masseur_id
        masseur_id = validated_data.pop('masseur_id', None)
        if masseur_id is not None:
            try:
                masseur = Masseur.objects.get(id=masseur_id)
                validated_data['masseur'] = masseur
            except Masseur.DoesNotExist:
                raise serializers.ValidationError({"masseur_id": "Invalid masseur id"})

        # Обработка doctor_id
        doctor_id = validated_data.pop('doctor_id', None)
        if doctor_id is not None:
            try:
                doctor = Doctor.objects.get(id=doctor_id)
                validated_data['doctor'] = doctor
            except Doctor.DoesNotExist:
                raise serializers.ValidationError({"doctor_id": "Invalid doctor id"})

        return super().create(validated_data)

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'about', 'price']



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
        fields = ['id', 'masseur_name', 'specialization_category', 'birth_date', 'bio']

    def to_representation(self, instance):
        representation = super(MasseurSerializer, self).to_representation(instance)
        representation['masseur_name'] = instance.masseur_name.full_name
        # другие поля, если нужно
        return representation


class TrainingEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingEquipment
        fields = ['id', 'name']