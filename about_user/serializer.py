from rest_framework import serializers
from .models import About


class AboutSerializers(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ["id",
                  "first_name",
                  "last_name",
                  "country",
                  "date_of_birth",
                  "email",
                  "phone_number",
                  "image",
                  "about",
                  "size_l",
                  "size_d",
                  "hobbi",
                  "important"
                  ]

    def validate(self, attrs):
        attrs = super().validate(attrs)
        phone_number = attrs["phone_number"]

        if phone_number[0] != "+":
            raise serializers.ValidationError(detail="Формат ввода телефона: +996 555 555 555", code="Номер подходит")

        return attrs

# def validate_first_name(self, attrs):
# 	attrs = super().validate(attrs)
# 	first_name = attrs["first_name"]
#
# 	if first_name != RegisterSerializer.first_name:
# 		raise serializers.ValidationError(detail="Имена не подходят", code="Норм")
#
# 	return attrs
