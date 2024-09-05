from django.db import IntegrityError

from rest_framework import serializers

from apps.cars.models import CarBrand, CarModel


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = ('id', 'name')


class CarSerializer(serializers.ModelSerializer):
    brand = serializers.SlugRelatedField(
        slug_field='name',
        queryset=CarBrand.objects.all()
    )

    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'model', 'year', 'body_type')

    def create(self, validated_data):
        brand = validated_data.pop('brand')
        car = CarModel.objects.create(brand=brand, **validated_data)
        return car

    def validate(self, data):
        if CarModel.objects.filter(
            brand=data['brand'],
            model=data['model'],
            year=data['year'],
            body_type=data['body_type']
        ).exists():
            raise serializers.ValidationError(
                "Автомобіль з такою ж маркою, моделлю, роком і типом кузова вже є в БД. Створення ще одного не потрібно."
            )
        return data

# class CarSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CarModel
#         fields = ('id', 'user', 'brand', 'model', 'price', 'year', 'body_type', 'created_at', 'updated_at')
#         read_only_fields = (
#             'user', 'created_at', 'updated_at'
#         )
#
#     def create(self, validated_data):
#         validated_data['user'] = self.context['request'].user
#         return super().create(validated_data)
