from rest_framework import serializers
from property_images.models import PropertyImage


class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = "__all__"
        read_only_fields = ["listing", "uploaded_at"]