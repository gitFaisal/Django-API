from rest_framework import serializers
from .models import VisitorsTable

class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorsTable
        fields = (
                'personId',
                'first_name',
                'last_name',
                'visits'
        )
