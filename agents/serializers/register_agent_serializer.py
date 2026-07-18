from rest_framework import serializers

from agents.models import AgentProfile


class RegisterAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentProfile
        fields = [
            "agency_name",
            "license_number",
            "years_of_experience",
            "bio",
        ]

    def validate(self, attrs):
        user = self.context["request"].user

        if AgentProfile.objects.filter(user=user).exists():
            raise serializers.ValidationError(
                "You have already submitted an agent application."
            )

        return attrs

    def create(self, validated_data):
        user = self.context["request"].user

        return AgentProfile.objects.create(
            user=user,
            **validated_data,
        )