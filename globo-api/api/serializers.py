from rest_framework import serializers
from .models import Inquiry

class InquirySerializer(serializers.ModelSerializer):
    """ Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Inquiry
        fields = (
            'id',
            'name',
            'email',
            'remarks',
        )