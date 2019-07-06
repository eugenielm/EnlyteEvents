from .models import Event
from rest_framework import serializers


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('name', 'organization', 'start_date', 'cost')

    # https://www.django-rest-framework.org/api-guide/validators/#validation-in-rest-framework
    # https://www.django-rest-framework.org/api-guide/serializers/#field-level-validation
    def validate_name(self, value):
        """
        Check that the name of the event is at least 5 characters long.
        """
        if len(value) < 5:
            raise serializers.ValidationError("The name of an event must contain at least 5 characters.")
        return value

    def validate_organization(self, value):
        """
        Check that the name of the organization is at least 3 characters long.
        """
        if len(value) < 3:
            raise serializers.ValidationError(
                "The organization name of an event must contain at least 3 characters.")
        return value