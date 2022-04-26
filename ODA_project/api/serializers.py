from rest_framework import serializers
# from django.contrib.auth import get_user_model
from . import models

class ConstantesSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Constantes
        fields='__all__'
        depth=1


# class PersonneAffilieeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PersonneAffiliee
#         fields = '__all__'
#         depth = 1


# class CustomUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = get_user_model()
#         fields = '__all__'
# class PersonneVulnerableSerializers(serializers.ModelSerializer):
#     class Meta: 
#         model=PersonneVulnerable
#         fields='__all__'
#         depth=1

# class TypeAntecedentMedicalSerializers(serializers.ModelSerializer):
#     class Meta: 
#         model=TypeAntecedentMedical
#         fields='__all__'
#         depth=1


#class EnregistrementVideo Serializers


class EnregistrementVideoSerializers(serializers.ModelSerializer):
    class Meta: 
        model=models.EnregistrementVideo
        fields='__all__'
        depth=1

    def update(self, instance, validated_data):
        instance.id_enregistrement_video = validated_data.get("id_enregistrement_video", instance.id_enregistrement_video)
        instance.heure_debut = validated_data.get("heure_debut", instance.heure_debut)
        instance.save()
        return instance
