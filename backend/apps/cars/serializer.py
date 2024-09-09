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
