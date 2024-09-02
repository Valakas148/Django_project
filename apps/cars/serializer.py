from rest_framework import serializers

from apps.cars.models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'user', 'brand', 'model', 'price', 'year', 'body_type', 'created_at', 'updated_at')
        read_only_fields = (
            'user', 'created_at', 'updated_at'
        )

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)