from rest_framework import serializers
from .models import Currency


class CurrencyModel:
    def __init__(self, auto_increment_id, name, sign, uah, countries):
        self.auto_increment_id = auto_increment_id
        self.name = name
        self.sign = sign
        self.uah = uah
        self.countries = countries


class CurrencySerializer(serializers.Serializer):

    name = serializers.CharField(max_length=50)
    sign = serializers.CharField(max_length=50)
    uah = serializers.FloatField()
    countries = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Currency.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.sign = validated_data.get("sign", instance.sign)
        instance.uah = validated_data.get("uah", instance.uah)
        instance.countries = validated_data.get("countries", instance.countries)
        instance.save()
        return instance


