from rest_framework import serializers
from rest_framework.serializers import (
    CharField, Serializer, ModelSerializer, IntegerField
)

class DistrictSerializer(Serializer):
    church_assembly_location = serializers.CharField()
    pastor_incharge = serializers.CharField()
    phone = serializers.CharField()
    tacstatename = serializers.CharField()
    created = serializers.DateTimeField()
    

    class Meta:
        fields = [
            'church_assembly_location', 'pastor_incharge', 'phone', 'tacstatename', 'created'
        ]
