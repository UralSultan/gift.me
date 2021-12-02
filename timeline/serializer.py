from rest_framework import serializers
from .models import Wish, Gift
from holidays.models import HolidayModel


class WishSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    image = serializers.ImageField()
    holiday = serializers.PrimaryKeyRelatedField(queryset=HolidayModel.objects.all())
    description = serializers.CharField(max_length=250)
    link = serializers.URLField(max_length=255, blank=True)

    def create(self, validated_data):
        wish = Wish.objects.create(**validated_data)
        return wish

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.image = validated_data.get('image', instance.image)
        instance.holiday = validated_data.get('holiday', instance.holiday)
        instance.description = validated_data.get('description', instance.description)
        instance.link = validated_data.get('link', instance.link)
        instance.save()
        return instance


class GiftSrializer(serializers.ModelSerializer):
    class Meta:
        model = Gift
        fields = ['name', 'country', 'category', 'sub_category', 'condition', 'image']
