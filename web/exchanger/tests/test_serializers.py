from django.test import TestCase
from exchanger.models import Currency
from exchanger.serializers import CurrencySerializer


class CurrencySerializerTestCase(TestCase):
    def test_serializer(self):
        print("-----------------Test Currency Serializer----------------")
        test_currency = Currency.objects.create(name="test", sign="test", uah=0, countries="test")
        data = CurrencySerializer(test_currency).data

        expected_data = {
                'name': "test",
                'sign': "test",
                 'uah': 0.0,
                 'countries': "test"
                 }

        self.assertEqual(expected_data, data)