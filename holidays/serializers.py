from rest_framework import serializers
from .models import HolidayModel


class HolidaySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    image = serializers.ImageField()
    date_of_holiday = serializers.DateField()

    def create(self, validated_data):
        holiday = HolidayModel.objects.create(**validated_data)
        return holiday

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.date_of_holiday = validated_data.get('date_of_holiday', instance.date_of_holiday)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance