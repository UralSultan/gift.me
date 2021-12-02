from django.contrib.auth.models import User
from rest_framework import serializers, validators
from rest_framework.authtoken.models import Token


class RegisterSerializer(serializers.Serializer):
    username = serializers.EmailField(
        required=True, validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )
    first_name = serializers.CharField(
        required=True, validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )
    last_name = serializers.CharField(
        required=True, validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(required=True, min_length=8)
    confirm_password = serializers.CharField(required=True, min_length=8, write_only=True)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        password = attrs["password"]
        confirm_password = attrs["confirm_password"]

        if password != confirm_password:
            raise serializers.ValidationError(detail="password does not match", code="password_match")

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            username=validated_data["username"],
            password=validated_data["password"]

        )

        Token.objects.create(user=user)
        return user

    def to_representation(self, instance):
        response = super().to_representation(instance)
        token = Token.objects.filter(user_id=instance.id).first()
        response["token"] = token.key
        return response