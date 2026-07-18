from rest_framework import serializers
from ..models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "password",
        ]

    def validate_email(self, value):
        """
        Ensure the email is unique.
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "A user with this email already exists."
            )
        return value

    def create(self, validated_data):
        """
        Create a new user using the custom manager.
        """
        return User.objects.create_user(**validated_data)